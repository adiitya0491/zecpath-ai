"""
Day 50
Time Based Scoring
"""

def time_score(
    time_taken,
    limit
):

    if limit == 0:
        return 0

    ratio = time_taken / limit

    if ratio <= 0.5:
        return 1.0

    elif ratio <= 1.0:
        return 0.7

    return 0.4


def classify_speed(
    time_taken,
    limit
):

    ratio = time_taken / limit

    if ratio <= 0.5:
        return "Fast"

    elif ratio <= 1.0:
        return "On Time"

    return "Slow"


if __name__ == "__main__":

    print(
        time_score(
            20,
            30
        )
    )

    print(
        classify_speed(
            20,
            30
        )
    )