"""
Day 52
Recommendation Pipeline
"""

from ai_core.decision_engine import (
    generate_decision,
    calculate_decision_confidence
)

from ai_core.explanation_generator import (
    generate_explanation
)


def recommendation_pipeline(
    candidate_id,
    scores,
    behavior_risk,
    integrity_risk
):

    final_score = scores.get(
        "final_score",
        0
    )

    decision, adjusted_score = generate_decision(
        final_score,
        behavior_risk,
        integrity_risk
    )

    confidence = (
        calculate_decision_confidence(
            list(scores.values())
        )
    )

    explanation = generate_explanation(
        scores,
        decision
    )

    return {

        "candidate_id":
            candidate_id,

        "final_score":
            final_score,

        "adjusted_score":
            adjusted_score,

        "decision":
            decision,

        "confidence_score":
            confidence,

        "risks": {

            "behavior":
                behavior_risk,

            "integrity":
                integrity_risk
        },

        "explanation":
            explanation
    }


if __name__ == "__main__":

    sample_scores = {

        "ats": 75,

        "screening": 70,

        "communication": 80,

        "technical": 85,

        "machine_test": 78,

        "behavior": 80,

        "integrity": 85,

        "final_score": 82
    }

    result = recommendation_pipeline(

        candidate_id="C10001",

        scores=sample_scores,

        behavior_risk="Low Risk",

        integrity_risk="Moderate Risk"
    )

    print(result)