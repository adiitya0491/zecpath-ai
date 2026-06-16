from interview_ai.summary_generator import (
    generate_interview_summary
)


def test_summary():

    result = generate_interview_summary(
        candidate_id="C1",

        hr_scores=[],

        communication={
            "communication_score": 50
        },

        behavior={
            "confidence": {
                "confidence_score": 50
            },
            "behavioral_score": 50,
            "contradiction": False
        },

        answers=[]
    )

    assert "overall_score" in result
    assert "decision" in result
    assert "summary" in result