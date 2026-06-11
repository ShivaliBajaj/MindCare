# MindCare Architecture

## Overview

MindCare is a clinically informed behavioral risk intelligence system designed to analyze mental health–related text and generate interpretable behavioral assessments.

The system is intended to support understanding of behavioral signals through explainable machine learning and clinically informed interpretation. It is not a diagnosis, treatment, or suicide prediction system.

---

## High-Level Workflow

User Text
    ↓
MentalBERT
    ↓
Behavioral Signal Probabilities
    ↓
Severity Mapping Layer
    ↓
Risk Engine
    ↓
Clinical Explanation Layer

---

## Component Descriptions

### 1. Input Layer

The system receives free-text content for analysis.

Examples may include social media posts, journal-style entries, forum discussions, or other mental health–related text.

---

### 2. MentalBERT

MentalBERT serves as the primary language model.

The model identifies behavioral signals associated with the following categories:

- Distress
- Hopelessness
- Isolation
- Burdensomeness
- Help-Seeking
- Suicidal Ideation

For each category, the model produces a probability score rather than a direct decision.

---

### 3. Severity Mapping Layer

Probability scores are translated into clinically interpretable severity levels such as Low, Moderate, and High.

This layer separates model outputs from downstream interpretation logic.

---

### 4. Risk Engine

The Risk Engine combines severity levels using transparent, clinically informed rules.

The engine is designed to support explainability and allows reasoning to remain visible rather than hidden inside a model.

Help-Seeking is treated as a protective factor and may reduce overall concern rather than increase it.

---

### 5. Clinical Explanation Layer

The explanation layer converts system outputs into human-readable interpretations.

The objective is to communicate which behavioral signals contributed to the assessment and why.

---

## Escalation Analysis

Escalation is not directly predicted by MentalBERT.

Because escalation is inherently temporal, it requires multiple observations across time.

Current versions of MindCare treat escalation as a derived concept based on behavioral patterns observed across multiple inputs.

Future work may explore escalation forecasting using longitudinal datasets.

---

## Human-in-the-Loop Design

MindCare is designed to support human judgment.

The system provides interpretable behavioral assessments and explanations, while final decisions remain the responsibility of qualified humans.

The system is not intended to replace clinical evaluation or professional decision-making.
