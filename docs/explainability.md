# AI Explainability Documentation

## Objective

To ensure that every hiring recommendation produced by Zecpath AI can be understood and reviewed by recruiters.

---

# Explainability Framework

Each score includes:

* ATS Score Explanation
* Screening Explanation
* HR Explanation
* Final Hiring Explanation

---

# Example Explainable Output

```json
{
  "candidate_id": "C101",
  "final_score": 78,
  "decision": "Hire",
  "explanation": {
    "ats": "Strong resume match",
    "screening": "Good response relevance",
    "hr": "High communication and confidence"
  }
}
```

---

# Explainability Features

## ATS Layer

Provides explanation for:

* Skill matching
* Experience matching
* Education relevance

## Screening Layer

Provides explanation for:

* Intent detection
* Answer relevance
* Candidate responses

## HR Layer

Provides explanation for:

* Communication quality
* Confidence indicators
* Behavioral analysis

## Unified Layer

Provides explanation for:

* Final score calculation
* Weight usage
* Hiring recommendation

---

# Recruiter Benefits

* Easier decision validation
* Increased trust in AI
* Better auditability
* Transparent candidate evaluation

---

# Future Improvements

* Interactive explainability dashboard
* Visual scoring breakdowns
* LLM-generated explanations

---

# Conclusion

Explainability ensures that AI decisions remain understandable, auditable, and trustworthy for recruiters and candidates.
