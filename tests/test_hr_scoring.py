from interview_ai.hr_scoring_engine import (
    hr_scoring_pipeline
)


def test_hr_score():

    answers = [

        {
            "question_id": "Q1",
            "relevance_score": 0.9,
            "communication_score": 85,
            "confidence_score": 80,
            "contradiction": False,
            "is_vague": False
        }
    ]

    result = hr_scoring_pipeline(
        answers,
        "fresher"
    )

    assert "hr_interview_score" in result
    assert "decision" in result
    assert result["hr_interview_score"] > 0