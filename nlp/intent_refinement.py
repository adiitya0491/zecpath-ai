"""
Day 54 - Intent Refinement
Zecpath AI
"""


def refined_intent_detection(text):

    text = text.lower()

    # Experience Intent

    if any(
        word in text
        for word in [
            "built",
            "developed",
            "implemented"
        ]
    ):
        return "experience"

    # Education Intent

    if any(
        word in text
        for word in [
            "learned",
            "studied",
            "course"
        ]
    ):
        return "education"

    # Future Intent

    if any(
        word in text
        for word in [
            "will",
            "plan",
            "future"
        ]
    ):
        return "future_intent"

    return "generic"


if __name__ == "__main__":

    text = "I developed an AI application"

    print(
        refined_intent_detection(
            text
        )
    )