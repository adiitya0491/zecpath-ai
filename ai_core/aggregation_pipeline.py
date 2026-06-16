"""
Day 51
Aggregation Pipeline
"""

from ai_core.cross_round_engine import (
    calculate_final_score,
    get_weights
)

from ai_core.hiring_fit_calculator import (
    calculate_hiring_fit,
    get_hiring_decision
)


# ----------------------------------
# Normalization
# ----------------------------------

def normalize_scores(scores):

    normalized = {}

    for key, value in scores.items():

        normalized[key] = max(
            min(value, 100),
            0
        )

    return normalized


# ----------------------------------
# Main Aggregation Pipeline
# ----------------------------------

def aggregation_pipeline(
    candidate_id,
    scores,
    role_type="technical"
):

    normalized_scores = normalize_scores(
        scores
    )

    weights = get_weights(
        role_type
    )

    final_score = calculate_final_score(
        normalized_scores,
        weights
    )

    fit = calculate_hiring_fit(
        final_score
    )

    decision = get_hiring_decision(
        final_score
    )

    explanation = {

        "ats":
            "Resume matched job requirements.",

        "screening":
            "Screening responses evaluated.",

        "hr":
            "Communication and behavioral assessment completed.",

        "technical":
            "Technical knowledge evaluated.",

        "machine_test":
            "Practical task performance evaluated."
    }

    return {

        "candidate_id":
            candidate_id,

        "scores":
            normalized_scores,

        "weights":
            weights,

        "final_score":
            final_score,

        "decision":
            decision,

        "hiring_fit":
            fit,

        "explanation":
            explanation
    }


if __name__ == "__main__":

    scores = {

        "ats": 75,

        "screening": 70,

        "hr": 80,

        "technical": 85,

        "machine_test": 78
    }

    result = aggregation_pipeline(
        "C9001",
        scores,
        "technical"
    )

    print(result)