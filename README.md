# MindCare

An India-contextualized suicide risk intelligence MVP focused on early behavioral signal detection, temporal risk analysis, and explainable AI for mental health research.

## Project Goals

- Detect suicide risk patterns from text data
- Analyze temporal behavioral escalation
- Prioritize interpretability and ethical AI reasoning
- Incorporate Indian mental health context using NCRB and public reports

## Core Stack

- MentalBERT
- LSTM
- XGBoost
- SHAP
- FastAPI

## Ethical and Clinical Considerations

MindCare is a research-oriented suicide risk intelligence MVP focused on early behavioral signal detection, temporal risk analysis, and model interpretability.

This project does NOT diagnose psychiatric conditions and is not intended to replace licensed mental health professionals.

Key principles followed during development:

- Prioritized patient safety and high-recall risk detection
- Avoided deterministic or judgmental language
- Emphasized explainability over black-box predictions
- Considered ethical limitations of public mental health data
- Acknowledged the scarcity of publicly available Indian psychiatric datasets
- Incorporated Indian epidemiological context using NCRB and mental health reports

Important:
This system is intended strictly for educational and research purposes and should never be used as a standalone clinical diagnostic tool.

## Environment Setup

MindCare uses a dedicated Conda environment named `mindcare`
for dependency isolation and reproducibility.

### Create Environment

```bash
conda create -n mindcare python=3.11