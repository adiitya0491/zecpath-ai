from ai_core.stable_system import (
    stable_pipeline,
    safe_score
)


def test_stable_pipeline():

    result = stable_pipeline(
        "C1",
        {
            "ats": 120,
            "hr": -10
        }
    )

    assert result["final_score"] <= 100


def test_safe_score_upper():

    assert safe_score(150) == 100


def test_safe_score_lower():

    assert safe_score(-50) == 0


def test_safe_score_invalid():

    assert safe_score("abc") == 0


if __name__ == "__main__":

    test_stable_pipeline()
    test_safe_score_upper()
    test_safe_score_lower()
    test_safe_score_invalid()

    print("All tests passed")