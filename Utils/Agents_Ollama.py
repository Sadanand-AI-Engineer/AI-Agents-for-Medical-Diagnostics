from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama


class Agent:
    """
    Base agent that:
    - Builds a role-specific prompt (PromptTemplate)
    - Calls a local Ollama model via ChatOllama
    """

    def __init__(self, medical_report=None, role=None, extra_info=None, model_name="llama3.2"):
        self.medical_report = medical_report
        self.role = role
        self.extra_info = extra_info or {}

        # Local LLM (Ollama)
        self.model = ChatOllama(model=model_name,temperature=0,base_url="http://localhost:11434")


        # Prompt template depends on agent role
        self.prompt_template = self.create_prompt_template()

    def create_prompt_template(self) -> PromptTemplate:
        """
        Creates a PromptTemplate for the given agent role.
        """
        if self.role == "MultidisciplinaryTeam":
            template = """
Act like a multidisciplinary team of healthcare professionals.

You will receive a medical report of a patient visited by a Cardiologist, Psychologist, and Pulmonologist.

Task:
- Review the reports from the Cardiologist, Psychologist, and Pulmonologist
- Analyze them and come up with a list of 3 possible health issues
- For each issue, provide a short reason

Return ONLY bullet points (exactly 3).

Cardiologist Report:
{cardiologist_report}

Psychologist Report:
{psychologist_report}

Pulmonologist Report:
{pulmonologist_report}
"""
            return PromptTemplate.from_template(template)

        templates = {
            "Cardiologist": """
Act like a cardiologist. You will receive a medical report of a patient.

Task:
- Review the patient's cardiac workup, including ECG, blood tests, Holter monitor results, and echocardiogram.

Focus:
- Determine if there are any subtle signs of cardiac issues that could explain the patient’s symptoms.
- Rule out underlying heart conditions (arrhythmias, structural abnormalities) that might be missed on routine testing.

Recommendation:
- Provide guidance on further cardiac testing or monitoring if needed.
- Suggest potential management strategies if a cardiac issue is identified.

Return ONLY:
1) Possible cardiac causes
2) Recommended next steps

Medical Report:
{medical_report}
""",
            "Psychologist": """
Act like a psychologist. You will receive a patient's report.

Task:
- Review the patient's report and provide a psychological assessment.

Focus:
- Identify potential mental health issues (anxiety, depression, trauma) affecting the patient.

Recommendation:
- Provide guidance on addressing these concerns (therapy, counseling, interventions).

Return ONLY:
1) Possible mental health issues
2) Recommended next steps

Patient's Report:
{medical_report}
""",
            "Pulmonologist": """
Act like a pulmonologist. You will receive a patient's report.

Task:
- Review the patient's report and provide a pulmonary assessment.

Focus:
- Identify potential respiratory issues (asthma, COPD, lung infections) affecting breathing.

Recommendation:
- Suggest next steps (PFTs, imaging, other interventions).

Return ONLY:
1) Possible respiratory issues
2) Recommended next steps

Patient's Report:
{medical_report}
"""
        }

        if self.role not in templates:
            raise ValueError(f"Unknown role: {self.role}")

        return PromptTemplate.from_template(templates[self.role])

    def run(self):
        """
        Executes the agent:
        - Formats the prompt
        - Sends prompt to the Ollama model
        - Returns response text
        """
        print(f"{self.role} is running...")

        try:
            if self.role == "MultidisciplinaryTeam":
                prompt = self.prompt_template.format(
                    cardiologist_report=self.extra_info.get("cardiologist_report", ""),
                    psychologist_report=self.extra_info.get("psychologist_report", ""),
                    pulmonologist_report=self.extra_info.get("pulmonologist_report", ""),
                )
            else:
                prompt = self.prompt_template.format(medical_report=self.medical_report)

            response = self.model.invoke(prompt)
            return response.content

        except Exception as e:
            print("Error occurred:", e)
            return None


class Cardiologist(Agent):
    def __init__(self, medical_report, model_name="llama3.2"):
        super().__init__(medical_report=medical_report, role="Cardiologist", model_name=model_name)


class Psychologist(Agent):
    def __init__(self, medical_report, model_name="llama3.2"):
        super().__init__(medical_report=medical_report, role="Psychologist", model_name=model_name)


class Pulmonologist(Agent):
    def __init__(self, medical_report, model_name="llama3.2"):
        super().__init__(medical_report=medical_report, role="Pulmonologist", model_name=model_name)


class MultidisciplinaryTeam(Agent):
    def __init__(self, cardiologist_report, psychologist_report, pulmonologist_report, model_name="llama3.2"):
        extra_info = {
            "cardiologist_report": cardiologist_report or "",
            "psychologist_report": psychologist_report or "",
            "pulmonologist_report": pulmonologist_report or "",
        }
        super().__init__(role="MultidisciplinaryTeam", extra_info=extra_info, model_name=model_name)
