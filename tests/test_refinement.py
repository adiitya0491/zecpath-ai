"""
Day 54 - Refinement Tests
"""

from ai_core.optimized_ai_engine import adjust_decision
from ai_core.refined_scoring_logic import (
    consistency_adjustment,
    refined_final_score
)
from nlp.intent_refinement import refined_intent_detection


def test_false_positive_fix():
    """
    High score but high integrity risk
    should not be auto-selected.
    """

    decision = adjust_decision(
        score=85,
        technical=90,
        integrity_risk="High Risk"
    )

    assert decision == "Hold / Review"


def test_false_negative_fix():
    """
    Strong technical candidate should
    not be directly rejected.
    """

    decision = adjust_decision(
        score=58,
        technical=90,
        integrity_risk="Low Risk"
    )

    assert decision == "Hold / Review"


def test_consistency_reward():

    scores = {
        "ats": 80,
        "hr": 82,
        "technical": 78
    }

    assert consistency_adjustment(scores) == 5


def test_consistency_penalty():

    scores = {
        "ats": 95,
        "hr": 40,
        "technical": 90
    }

    assert consistency_adjustment(scores) == -5


def test_refined_final_score():

    scores = {
        "ats": 80,
        "hr": 82,
        "technical": 78
    }

    result = refined_final_score(
        scores=scores,
        base_score=75
    )

    assert result == 80


def test_experience_intent():

    result = refined_intent_detection(
        "I developed a machine learning project."
    )

    assert result == "experience"


def test_education_intent():

    result = refined_intent_detection(
        "I studied data structures in a course."
    )

    assert result == "education"


def test_future_intent():

    result = refined_intent_detection(
        "I plan to learn cloud computing in future."
    )

    assert result == "future_intent"


def test_generic_intent():

    result = refined_intent_detection(
        "Hello, nice to meet you."
    )

    assert result == "generic"