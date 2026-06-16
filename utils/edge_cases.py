"""
Day 57
Edge Case Validation
"""


def handle_edge_cases(answer):
    """
    Validate answer quality.
    """

    if answer is None:
        return "empty"

    answer = str(answer).strip()

    if len(answer) == 0:
        return "empty"

    if len(answer.split()) < 3:
        return "too_short"

    if len(answer) > 1000:
        return "too_long"

    return "valid"


if __name__ == "__main__":

    print(handle_edge_cases(""))
    print(handle_edge_cases("Yes"))
    print(handle_edge_cases("I worked on backend APIs"))