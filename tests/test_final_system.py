"""
Day 45 Final System Test
"""


def test_final_system():

    result = {
        "candidate_id": "C1001",
        "final_score": 82,
        "decision": "Hire"
    }

    assert "candidate_id" in result
    assert "final_score" in result
    assert "decision" in result


def test_final_score():

    score = 80

    assert score > 0
    assert score <= 100


def test_decision():

    decision = "Hire"

    assert decision in [
        "Hire",
        "Consider",
        "Reject"
    ]