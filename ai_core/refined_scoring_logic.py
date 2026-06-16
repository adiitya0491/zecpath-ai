"""
Day 54 - Refined Scoring Logic
Zecpath AI
"""


# ---------------------------------
# Consistency Adjustment
# ---------------------------------

def consistency_adjustment(scores):

    values = list(scores.values())

    if not values:
        return 0

    variance = max(values) - min(values)

    # Penalize inconsistency
    if variance > 30:
        return -5

    # Reward consistency
    elif variance < 10:
        return 5

    return 0


# ---------------------------------
# Final Refined Score
# ---------------------------------

def refined_final_score(scores, base_score):

    adjustment = consistency_adjustment(scores)

    final_score = base_score + adjustment

    return max(
        min(final_score, 100),
        0
    )


if __name__ == "__main__":

    scores = {
        "ats": 80,
        "hr": 82,
        "technical": 78
    }

    print(
        refined_final_score(
            scores,
            75
        )
    )