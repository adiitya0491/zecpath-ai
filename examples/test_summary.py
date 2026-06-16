from interview_ai.summary_generator import (
    generate_interview_summary
)

result = generate_interview_summary(
    candidate_id="C101",

    hr_scores=[
        {
            "question_id": "Q1",
            "final_score": 85
        }
    ],

    communication={
        "communication_score": 80
    },

    behavior={
        "confidence": {
            "confidence_score": 75
        },
        "behavioral_score": 78,
        "contradiction": False
    },

    answers=[
        "I worked in a team to deliver projects."
    ]
)

print(result)