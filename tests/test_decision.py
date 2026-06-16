"""
Day 52
Decision AI Tests
"""

from ai_core.decision_engine import (
    generate_decision,
    calculate_decision_confidence
)

from ai_core.recommendation_pipeline import (
    recommendation_pipeline
)


def test_decision():

    decision, score = generate_decision(
        85
    )

    assert decision == "Selected"


def test_confidence():

    confidence = (
        calculate_decision_confidence(
            [80, 82, 85, 81]
        )
    )

    assert confidence > 0


def test_recommendation_pipeline():

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

        integrity_risk="Low Risk"
    )

    assert "decision" in result

    assert "confidence_score" in result

    assert "explanation" in result


if __name__ == "__main__":

    test_decision()

    test_confidence()

    test_recommendation_pipeline()

    print("All tests passed")