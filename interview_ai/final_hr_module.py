"""
Day 45 Final Production HR Module
Zecpath AI
"""

from interview_ai.hr_scoring_engine import hr_scoring_pipeline
from interview_ai.summary_generator import generate_interview_summary
from ai_core.unified_scoring_engine import calculate_unified_score


DEFAULT_WEIGHTS = {
    "ats": 0.30,
    "screening": 0.30,
    "hr": 0.40
}


def run_hr_interview(
    candidate_id,
    answers,
    communication,
    behavior,
    ats_score=70,
    screening_score=75
):
    """
    Complete HR Interview Pipeline
    """

    hr_result = hr_scoring_pipeline(
        answers,
        candidate_type="fresher"
    )

    final_score = calculate_unified_score(
        ats_score=ats_score,
        screening_score=screening_score,
        hr_score=hr_result["hr_score"],
        weights=DEFAULT_WEIGHTS
    )

    summary = generate_interview_summary(
        candidate_id=candidate_id,
        hr_scores=hr_result["details"],
        communication=communication,
        behavior=behavior,
        answers=answers
    )

    return {
        "candidate_id": candidate_id,
        "ats_score": ats_score,
        "screening_score": screening_score,
        "hr_score": hr_result["hr_score"],
        "final_score": final_score,
        "decision": summary["decision"],
        "summary": summary
    }


if __name__ == "__main__":

    sample_answers = [
        {
            "question_id": "Q1",
            "relevance_score": 0.90,
            "communication_score": 85,
            "confidence_score": 80,
            "contradiction": False,
            "is_vague": False
        }
    ]

    communication = {
        "communication_score": 82
    }

    behavior = {
        "confidence": {
            "confidence_score": 78
        },
        "behavioral_score": 80,
        "contradiction": False
    }

    result = run_hr_interview(
        candidate_id="C1001",
        answers=sample_answers,
        communication=communication,
        behavior=behavior
    )

    print(result)