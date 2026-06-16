from technical_ai.experience_logic import get_experience_level


def test_fresher():

    assert get_experience_level(1) == "0-2"


def test_mid_level():

    assert get_experience_level(3) == "3-5"


def test_senior():

    assert get_experience_level(7) == "5+"


if __name__ == "__main__":

    test_fresher()
    test_mid_level()
    test_senior()

    print("All tests passed")