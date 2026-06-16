from interview_ai.communication_engine import (
    calculate_communication_score
)


def test_communication_score():
    text = (
        "I have experience in Python because I worked "
        "on backend systems and developed REST APIs."
    )

    result = calculate_communication_score(text)

    assert result["communication_score"] > 0
    assert "breakdown" in result
    assert result["level"] in [
        "Poor",
        "Average",
        "Good",
        "Excellent"
    ]