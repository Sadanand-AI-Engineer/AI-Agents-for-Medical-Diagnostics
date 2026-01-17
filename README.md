# AI-Agents-for-Medical-Diagnostics

**Author:** Sadanand Katukuri  
**Location:** Houston, Texas, USA  
**Email:** sadanandkatukuri999@gmail.com  

---
## Disclaimer

This project is intended for **research and educational purposes only**.
It is **not a medical device** and must not be used for clinical diagnosis,
treatment, or real-world medical decision-making.

## Overview

**AI-Agents-for-Medical-Diagnostics** is a research-oriented Python project that demonstrates how **autonomous, role-specialized AI agents** can collaboratively analyze complex medical case narratives and synthesize multidisciplinary diagnostic insights.

The system uses **local Large Language Models (LLMs) via Ollama** and a **multi-agent orchestration architecture** built with LangChain. Each agent simulates the reasoning process of a medical specialist and contributes domain-specific analysis that is later aggregated into a final multidisciplinary assessment.

---

## Key Features

- **Multi-Agent Architecture**
  - Independent AI agents representing medical specialists
  - Role-specific prompt engineering and reasoning isolation

- **Local LLM Execution**
  - Runs entirely offline using **Ollama**
  - No API keys required for core functionality

- **Deterministic & Explainable Outputs**
  - Temperature-controlled inference
  - Clear reasoning traces per specialist

- **Extensible Design**
  - Easy to add new specialists (e.g., Neurology, Endocrinology)
  - Modular provider support (local or cloud-based LLMs)

---

## System Architecture

### Specialist Agents

1. **Cardiologist Agent**
   - Evaluates cardiovascular symptoms
   - Identifies potential cardiac causes such as arrhythmias or ischemic indicators
   - Suggests diagnostic follow-ups and monitoring strategies

2. **Psychologist Agent**
   - Analyzes behavioral, emotional, and stress-related symptoms
   - Identifies anxiety, panic disorders, or psychosomatic contributors
   - Recommends psychological evaluation or therapy pathways

3. **Pulmonologist Agent**
   - Assesses respiratory and pulmonary indicators
   - Evaluates breathing irregularities and lung-related conditions
   - Suggests pulmonary testing or respiratory interventions

4. **Multidisciplinary Team Agent**
   - Aggregates all specialist reports
   - Produces a consolidated diagnostic assessment with reasoning

---

## Repository Structure

---
```text
AI-Agents-for-Medical-Diagnostics/
├─ Utils/
│  ├─ Agents.py           # Cloud-based agent definitions (optional)
│  └─ Agents_Ollama.py    # Local Ollama-based agents
├─ Medical Reports/       # Synthetic medical case reports (optional)
├─ Results/               # Generated outputs (ignored by git)
├─ Main.py                # Entry point
├─ requirements.txt
├─ README.md
├─ LICENSE
└─ .gitignore


---
## Configuration

This project runs locally using Ollama and does not require API keys.


## Prerequisites

- **Python 3.11+**
- **Git**
- **Ollama** (local LLM runtime)

---

## Installation & Setup

### 1️⃣ Install Ollama

Download and install Ollama for your operating system.

Verify installation:

ollama --version


2️⃣ Pull a Supported Model

This project is tested with:

llama3.2 (recommended)

ollama pull llama3.2
ollama list

3️⃣ Clone the Repository
git clone https://github.com/Sadanand-AI-Engineer/AI-Agents-for-Medical-Diagnostics.git
cd AI-Agents-for-Medical-Diagnostics

4️⃣ Create & Activate Virtual Environment

Windows (PowerShell):

python -m venv venv
.\venv\Scripts\Activate.ps1


macOS / Linux:

python3 -m venv venv
source venv/bin/activate

5️⃣ Install Dependencies
pip install -r requirements.txt




##Running the Project
python Main.py

##Output

A consolidated diagnostic summary is written to:

Results/final_diagnosis.txt

Ollama Configuration Notes

Ollama runs locally at:
http://localhost:11434

The base URL is explicitly configured in:

Utils/Agents_Ollama.py


To switch models, update:

model="llama3.2"


Supported alternatives:

mistral

phi3

llama3

##Research & Academic Context

This project reflects applied research in: Agentic AI Systems, Multi-Agent Reasoning, Prompt Engineering, LLM-Orchestrated Decision Pipelines

It aligns with graduate-level coursework and professional experience in:

Generative AI, Cloud-native AI architectures, Data-driven decision automation

##Future Enhancements

Planned and potential extensions:

Additional specialist agents (Neurology, Endocrinology, Immunology)

Structured JSON outputs with schema validation

Confidence scoring per agent

RAG-based medical knowledge augmentation

Evaluation benchmarks and automated testing

Provider switching (Ollama ↔ OpenAI ↔ AWS Bedrock)





Copyright © 2026
Sadanand Katukuri


Contact

For academic collaboration, research discussion, or system design inquiries:

Sadanand Katukuri
📍 Houston, Texas, USA
📧 sadanandkatukuri999@gmail.com
Linkedin: https://www.linkedin.com/in/sadanand-katukuri-49ba1120b/
