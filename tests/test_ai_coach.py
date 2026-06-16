from future.ai_coach import generate_feedback


def test_ai_coach():

    feedback = generate_feedback(
        {
            "communication": 60,
            "technical": 80,
            "confidence": 50
        }
    )

    assert len(feedback) > 0


def test_good_candidate():

    feedback = generate_feedback(
        {
            "communication": 90,
            "technical": 90,
            "confidence": 90
        }
    )

    assert len(feedback) > 0


if __name__ == "__main__":

    test_ai_coach()

    test_good_candidate()

    print("All tests passed")