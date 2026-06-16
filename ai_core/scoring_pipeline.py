"""
Unified Scoring Pipeline
Zecpath AI - Day 41
"""

from ai_core.unified_scoring_engine import (
    calculate_unified_score,
    get_weights
)

from ai_core.hiring_fit import (
    calculate_hiring_fit
)


# ==========================================================
# DECISION LOGIC
# ==========================================================

def get_hiring_decision(score):

    if score >= 75:
        return "Hire"

    elif score >= 55:
        return "Consider"

    return "Reject"


# ==========================================================
# PIPELINE
# ==========================================================

def unified_scoring_pipeline(
    candidate_id,
    ats,
    screening,
    hr,
    candidate_type="fresher"
):
    """
    Main Unified Scoring Pipeline
    """

    weights = get_weights(candidate_type)

    final_score = calculate_unified_score(
        ats_score=ats,
        screening_score=screening,
        hr_score=hr,
        weights=weights
    )

    fit = calculate_hiring_fit(final_score)

    decision = get_hiring_decision(final_score)

    return {
        "candidate_id": candidate_id,

        "scores": {
            "ats": ats,
            "screening": screening,
            "hr": hr
        },

        "weights_used": weights,

        "final_score": final_score,

        "decision": decision,

        "fit": fit,

        "explanation": {
            "ats": "Resume match and ATS evaluation",
            "screening": "AI screening performance",
            "hr": "HR interview performance"
        }
    }


# ==========================================================
# EXAMPLE EXECUTION
# ==========================================================

if __name__ == "__main__":

    result = unified_scoring_pipeline(
        candidate_id="C101",
        ats=80,
        screening=70,
        hr=85,
        candidate_type="technical"
    )

    print(result)