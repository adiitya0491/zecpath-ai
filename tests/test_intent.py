import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)


from screening_ai.improved_intent import (
    improved_intent_classification
)


def test_intent():

    text = (
        "I worked as a backend developer "
        "for 2 years"
    )

    result = improved_intent_classification(
        text
    )

    assert result == "experience"


if __name__ == "__main__":

    test_intent()

    print("Intent Test Passed")