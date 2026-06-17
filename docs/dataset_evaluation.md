Dataset Evaluation Strategy

Purpose

MindCare requires datasets that support behavioral signal detection, explainable AI, and temporal risk analysis. Multiple datasets were evaluated before selecting a preferred training source.

⸻

Datasets Evaluated

RSD-15K

Strengths:

* User-level histories
* Temporal information
* Mental health and suicidality context
* Supports longitudinal behavioral analysis

Limitations:

* Access request required
* Public availability could not be confirmed

⸻

CLPsych Datasets

Strengths:

* Widely used in mental health NLP research
* Clinically relevant language signals
* Research community familiarity

Limitations:

* Dataset accessibility may vary
* Temporal analysis support may be limited depending on dataset version

⸻

Public Kaggle Alternatives

Strengths:

* Easier accessibility
* Useful for experimentation and pipeline development

Limitations:

* Often lack user-level histories
* Limited temporal information
* Variable clinical quality

⸻

Evaluation Criteria

The following criteria were used when assessing candidate datasets:

* Clinical relevance
* Temporal information availability
* Accessibility and governance
* Ethical considerations
* Explainability support
* Suitability for behavioral signal analysis

⸻

Preferred Dataset

RSD-15K was identified as the preferred dataset because it appears to provide user-level histories and temporal information that align with MindCare’s focus on behavioral signal progression and escalation analysis.

⸻

Current Limitation

At the time of evaluation, access to RSD-15K required a request process and availability could not be guaranteed.

⸻

Backup Strategy

MindCare follows a build-first approach:

* Continue pursuing access to RSD-15K
* Evaluate alternative datasets in parallel
* Build system architecture independently of final dataset selection
* Maintain flexibility in the training pipeline

