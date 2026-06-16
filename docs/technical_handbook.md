# Zecpath AI Technical Handbook

## Project Overview

Zecpath AI is an AI-powered intelligent hiring platform that automates the entire recruitment process from resume upload to final hiring decisions.

The system evaluates candidates through multiple stages and generates recruiter-friendly hiring recommendations.

---

# System Features

The platform can perform:

- Resume parsing
- ATS scoring
- Candidate screening
- HR interviews
- Technical interviews
- Machine test evaluation
- Behavioral analysis
- Integrity analysis
- Cross-round score aggregation
- Final hiring decisions
- Hiring intelligence reporting

---

# Complete Hiring Workflow

Resume Upload

↓

ATS Scoring

↓

Screening AI

↓

HR Interview AI

↓

Technical Interview AI

↓

Machine Test AI

↓

Behavioral AI

↓

Integrity AI

↓

Cross-Round Aggregation Engine

↓

Decision AI

↓

Hiring Report Generator

---

# Core Modules

## 1. Resume Parser

Extracts candidate information from resumes.

Outputs:

- Skills
- Experience
- Education
- Projects

---

## 2. ATS Engine

Matches resumes with job descriptions.

Produces ATS scores.

---

## 3. Screening AI

Conducts initial candidate screening.

Evaluates:

- Communication
- Clarity
- Relevance

---

## 4. HR Interview AI

Evaluates:

- Communication
- Confidence
- HR responses

---

## 5. Technical Interview AI

Evaluates:

- Technical knowledge
- Problem solving
- Real-world applicability

---

## 6. Machine Test AI

Evaluates:

- Coding ability
- Debugging
- Practical skills

---

## 7. Behavioral AI

Analyzes:

- Focus
- Attention
- Engagement

---

## 8. Integrity AI

Detects:

- Tab switching
- External voice
- Gaze deviation
- Screen focus loss

---

## 9. Cross-Round Aggregation Engine

Combines scores from all stages.

---

## 10. Decision AI

Generates:

- Selected
- Hold / Review
- Rejected

---

## 11. Hiring Report Generator

Creates recruiter-friendly reports.

---

# API Summary

POST /resume/parse

POST /ats/score

POST /screening/run

POST /interview/run

POST /technical/run

POST /machine/evaluate

POST /decision/final

GET /report/{candidate_id}

---

# Scoring Logic

Final Score =

ATS × 20%

+

Screening × 15%

+

HR × 20%

+

Technical × 25%

+

Machine Test × 20%

Additional Adjustments:

- Behavior Risk
- Integrity Risk
- Consistency Score

---

# Data Models

## Candidate Object

```json
{
  "candidate_id": "C1",

  "profile": {},

  "scores": {},

  "behavior": {},

  "decision": ""
}
```

## Report Object

```json
{
  "candidate_id": "C1",

  "final_score": 80,

  "decision": "Selected",

  "summary": {}
}
```

---

# Setup Guide

1. Clone repository

2. Create virtual environment

3. Install requirements

4. Configure environment variables

5. Run backend

6. Run AI services

---

# Deployment Architecture

Docker

↓

AWS / GCP

↓

Kubernetes

↓

Load Balancer

↓

Monitoring

---

# Troubleshooting

| Problem | Solution |
|---------|----------|
| API failure | Check logs |
| Wrong score | Validate inputs |
| Slow response | Check caching |
| Missing data | Check database |

---

# Future Improvements

- AI anomaly detection
- Predictive monitoring
- Emotion detection
- AI coaching
- Video analysis
- Multi-language support

---

# Conclusion

Zecpath AI is a scalable end-to-end AI hiring platform that automates recruitment while maintaining transparency, fairness, and explainability.