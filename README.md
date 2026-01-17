##AI-Agents-for-Medical-Diagnostics

Author: Sadanand Katukuri
Location: Houston, Texas, USA
Contact: sadanandkatukuri999@gmail.com

LinkedIn: https://www.linkedin.com/in/sadanand-katukuri-49ba1120b/

##Disclaimer

This project is intended strictly for research and educational purposes.
It is not a medical device and must not be used for clinical diagnosis, treatment, or real-world medical decision-making.

##Overview

AI-Agents-for-Medical-Diagnostics is a research-driven Python project that demonstrates how autonomous, role-specialized AI agents can collaboratively analyze complex medical case narratives and produce a multidisciplinary diagnostic assessment.

The system is built around a multi-agent orchestration architecture, where each agent simulates the reasoning process of a medical specialist. All agents operate using local Large Language Models (LLMs) via Ollama, enabling fully offline execution with no dependency on external APIs.

This project reflects applied work in agentic AI systems, LLM-driven reasoning pipelines, and distributed decision synthesis, and is designed with extensibility and clarity in mind.

##Key Features
Multi-Agent Architecture

Independent AI agents representing medical specialists

Role-specific prompts and reasoning isolation

Parallel execution with consolidated aggregation

Local LLM Execution

Runs entirely offline using Ollama

No API keys required for core functionality

Deterministic inference settings for reproducibility

Explainable Outputs

Each specialist produces transparent reasoning

Final assessment aggregates and reconciles domain insights

Extensible Design

Easy to add new specialist agents (e.g., Neurology, Endocrinology)

Modular support for local or cloud-based LLM providers

##System Architecture
Specialist Agents

1. Cardiologist Agent

Evaluates cardiovascular symptoms

Identifies potential cardiac risk factors and abnormalities

Suggests diagnostic follow-ups and monitoring strategies

2. Psychologist Agent

Analyzes behavioral, emotional, and stress-related indicators

Identifies anxiety disorders, panic conditions, or psychosomatic contributors

Recommends psychological evaluation pathways

3. Pulmonologist Agent

Assesses respiratory and pulmonary symptoms

Evaluates breathing irregularities and lung-related conditions

Suggests pulmonary testing or respiratory interventions

4. Multidisciplinary Team Agent

Aggregates all specialist outputs

Produces a consolidated diagnostic assessment with structured reasoning

##Repository Structure
AI-Agents-for-Medical-Diagnostics/
├─ Utils/
│  ├─ Agents.py            # Cloud-based agent definitions (optional)
│  └─ Agents_Ollama.py     # Local Ollama-based agents
├─ Medical Reports/        # Synthetic medical case reports (optional)
├─ Results/                # Generated outputs (ignored by git)
├─ Main.py                 # Entry point
├─ requirements.txt
├─ README.md
├─ LICENSE
└─ .gitignore

##Configuration

This project runs locally using Ollama and does not require API keys.

The Ollama service is expected to be available at:

http://localhost:11434


Model configuration is defined in:

Utils/Agents_Ollama.py

Prerequisites

Python 3.11+

Git

Ollama (local LLM runtime)

##Installation & Setup
1. Install Ollama

Download and install Ollama for your operating system.

Verify installation:

ollama --version

2. Pull a Supported Model

This project is tested with:

llama3.2 (recommended)

ollama pull llama3.2
ollama list

3. Clone the Repository
git clone https://github.com/Sadanand-AI-Engineer/AI-Agents-for-Medical-Diagnostics.git
cd AI-Agents-for-Medical-Diagnostics

4. Create and Activate a Virtual Environment

Windows (PowerShell):

python -m venv venv
.\venv\Scripts\Activate.ps1


macOS / Linux:

python3 -m venv venv
source venv/bin/activate

5. Install Dependencies
pip install -r requirements.txt

Running the Project
python Main.py

Output

A consolidated diagnostic summary is written to:

Results/final_diagnosis.txt


(Generated outputs are excluded from version control.)

Model Configuration

To switch models, update the following in Agents_Ollama.py:

model="llama3.2"


Supported alternatives include:

mistral

phi3

llama3

###Research and Professional Context

##This project reflects applied work in:

Agentic AI Systems

Multi-Agent Reasoning Architectures

Prompt Engineering for Role-Specialized LLMs

LLM-Orchestrated Decision Pipelines

It aligns with graduate-level coursework and professional experience in:

Generative AI

Cloud-native AI architectures

Intelligent automation and decision systems

###Future Enhancements

Planned and potential extensions include:

Additional specialist agents (Neurology, Endocrinology, Immunology)

Structured JSON outputs with schema validation

Confidence scoring per agent

Retrieval-Augmented Generation (RAG) for medical knowledge grounding

Evaluation benchmarks and automated testing

Provider switching (Ollama ↔ OpenAI ↔ AWS Bedrock)

##License

This project is licensed under the Apache License 2.0.
See the LICENSE
 file for details.

###Contact

For research collaboration, technical discussion, or system design inquiries:

Sadanand Katukuri
📍 Houston, Texas, USA
📧 sadanandkatukuri999@gmail.com

🔗 https://www.linkedin.com/in/sadanand-katukuri-49ba1120b/
