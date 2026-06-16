"""
Day 44 API Format Tests
Zecpath AI
"""


def test_start_response():

    response = {
        "session_id": "S123",
        "questions": [
            "Tell me about yourself"
        ]
    }

    assert "session_id" in response
    assert "questions" in response


def test_answer_response():

    response = {
        "follow_up": "Can you explain more?",
        "next_question": "Describe teamwork experience"
    }

    assert "next_question" in response


def test_report_response():

    response = {
        "candidate_id": "C1",
        "final_score": 80,
        "decision": "Hire"
    }

    assert "candidate_id" in response
    assert "final_score" in response


def test_error_response():

    response = {
        "error_code": "INVALID_INPUT",
        "status": 400
    }

    assert response["status"] == 400