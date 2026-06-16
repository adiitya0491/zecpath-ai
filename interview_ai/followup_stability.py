"""
Follow-Up Stability Engine
Zecpath AI - Day 42

Prevents endless follow-ups.
"""


def stable_followup(
    answer_quality,
    retry_count
):
    """
    Decide next action.
    """

    if retry_count >= 2:
        return "skip"

    if answer_quality in [
        "empty",
        "too_short"
    ]:
        return "clarify"

    if answer_quality == "uncertain":
        return "simplify"

    return "continue"


if __name__ == "__main__":

    print(
        stable_followup(
            "too_short",
            1
        )
    )