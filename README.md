# Zecpath AI – Intelligent Hiring Platform

## Overview

Zecpath AI is an end-to-end AI-powered hiring platform that automates the entire recruitment lifecycle, from resume screening to final hiring decisions.

The platform combines multiple AI modules to evaluate candidates fairly, consistently, and efficiently while reducing manual effort and hiring bias.

The system automates:

* Resume Parsing
* ATS Scoring
* AI Screening Interviews
* HR Interview Evaluation
* Technical Interview Evaluation
* Machine Test Evaluation
* Behavioral Analysis
* Integrity Analysis
* Cross-Round Aggregation
* Final Hiring Decisions
* Hiring Intelligence Reports

---

# Project Workflow

```text
Resume Upload

↓

Resume Parsing

↓

ATS Scoring

↓

Screening AI

↓

HR Interview AI

↓

Technical AI

↓

Machine Test Evaluation

↓

Behavior + Integrity Analysis

↓

Cross-Round Aggregation

↓

Decision AI

↓

Hiring Intelligence Report
```

---

# System Architecture

```text
User (Frontend)

↓

Backend API Layer

↓

AI Microservices Layer

------------------------------------

Resume Parser

ATS Engine

Screening AI

HR Interview AI

Technical AI

Machine Test AI

Behavior AI

Integrity AI

Aggregation Engine

Decision AI

Hiring Report Generator

------------------------------------

↓

Database

↓

Storage

↓

Monitoring & Observability
```

---

# Core AI Modules

| Module                  | Description                                   |
| ----------------------- | --------------------------------------------- |
| Resume Parser           | Extracts structured information from resumes  |
| ATS Engine              | Calculates resume-job compatibility           |
| Screening AI            | Evaluates candidate screening responses       |
| HR Interview AI         | Evaluates communication and confidence        |
| Technical AI            | Evaluates technical skills                    |
| Machine Test AI         | Evaluates practical coding ability            |
| Behavior AI             | Detects engagement and behavioral signals     |
| Integrity AI            | Detects potential cheating or integrity risks |
| Aggregation Engine      | Combines scores across all stages             |
| Decision AI             | Generates final hiring recommendations        |
| Hiring Report Generator | Produces recruiter-friendly reports           |

---

# Features

* End-to-end hiring automation
* Explainable AI decisions
* Multi-stage candidate evaluation
* Risk analysis
* Candidate ranking
* Security & governance
* Monitoring & observability
* Performance optimization
* Production-ready architecture
* Scalable design

---

# Project Structure

```text
zecpath-ai/

├── ai_core/

├── ai_engine/

├── api/

├── ats_engine/

├── behavior_ai/

├── data/

├── demo/

├── docs/

├── future/

├── handover/

├── integrity_ai/

├── interview_ai/

├── machine_test/

├── observability/

├── parsers/

├── portfolio/

├── presentation/

├── ranking/

├── review/

├── scoring/

├── screening_ai/

├── security/

├── technical_ai/

├── tests/

├── uploads/

├── utils/

├── README.md

└── requirements.txt
```

---

# Scoring Logic

Final Score Calculation:

```text
Final Score =

ATS (20%)

+

Screening (15%)

+

HR (20%)

+

Technical (25%)

+

Machine Test (20%)

↓

Decision AI
```

---

# Environment Setup

## Clone Repository

```bash
git clone https://github.com/your-repo/zecpath-ai.git
```

## Create Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running Demo

Run:

```bash
python demo/full_pipeline_simulation.py
```

Run tests:

```bash
pytest tests/
```

---

# Technologies Used

## Programming Language

* Python

## AI & NLP

* spaCy
* sentence-transformers
* scikit-learn

## Document Processing

* pdfplumber
* python-docx
* pytesseract
* pdf2image

## Testing

* pytest

## Security

* Access Control
* Audit Logging
* Encryption

---

# Future Roadmap

## Short-Term (0–6 Months)

* Improve AI accuracy
* Reduce latency
* Add real-time feedback

## Mid-Term (6–12 Months)

* AI Video Analysis
* Emotion Detection
* AI Coaching System
* Analytics Dashboard

## Long-Term (1–2 Years)

* Autonomous Hiring AI
* Predictive Hiring Success
* Multi-language AI
* Continuous Learning AI

---

# Project Status

| Feature          | Status |
| ---------------- | ------ |
| Resume Parsing   | ✅      |
| ATS System       | ✅      |
| Screening AI     | ✅      |
| HR Interview AI  | ✅      |
| Technical AI     | ✅      |
| Machine Test AI  | ✅      |
| Behavior AI      | ✅      |
| Integrity AI     | ✅      |
| Decision AI      | ✅      |
| Hiring Reports   | ✅      |
| Security         | ✅      |
| Monitoring       | ✅      |
| Production Ready | ✅      |

---

# Author

**Zecpath AI – 70-Day AI Internship Project**

Developer: Your Name

Duration: 70 Days

Project Type: End-to-End Intelligent Hiring Platform

Status: Production Ready 🚀
