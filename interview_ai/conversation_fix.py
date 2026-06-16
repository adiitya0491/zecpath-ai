"""
Day 57
Conversation Stabilization
"""


def next_step(
    answer_quality,
    retry_count
):
    """
    Prevent conversation loops.
    """

    if retry_count > 2:
        return "skip_question"

    if answer_quality == "empty":
        return "ask_again"

    if answer_quality == "too_short":
        return "clarify"

    return "continue"


if __name__ == "__main__":

    print(
        next_step(
            "empty",
            1
        )
    )

    print(
        next_step(
            "too_short",
            1
        )
    )

    print(
        next_step(
            "valid",
            1
        )
    )