from interview_ai.behavior_analyzer import (
    analyze_behavior
)


def test_behavior():
    result = analyze_behavior(
        "I am confident and successfully completed projects",
        5
    )

    assert result["behavioral_score"] > 0


def test_sentiment():
    result = analyze_behavior(
        "I achieved success in my project",
        5
    )

    assert result["sentiment"]["sentiment"] == "Positive"


def test_contradiction():
    result = analyze_behavior(
        "I don't know Python but I have experience in Python",
        5
    )

    assert result["contradiction"] is True


def test_confidence():
    result = analyze_behavior(
        "I am confident in my skills and experience",
        5
    )

    assert result["confidence"]["confidence_score"] > 0