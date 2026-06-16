"""
Day 51
Cross Round Aggregation Engine
"""

# ----------------------------------
# Default Weights
# ----------------------------------

DEFAULT_WEIGHTS = {
    "ats": 0.20,
    "screening": 0.15,
    "hr": 0.20,
    "technical": 0.25,
    "machine_test": 0.20
}

# ----------------------------------
# Role-Based Weights
# ----------------------------------

ROLE_WEIGHTS = {

    "fresher": {
        "ats": 0.20,
        "screening": 0.20,
        "hr": 0.25,
        "technical": 0.20,
        "machine_test": 0.15
    },

    "experienced": {
        "ats": 0.25,
        "screening": 0.10,
        "hr": 0.20,
        "technical": 0.25,
        "machine_test": 0.20
    },

    "technical": {
        "ats": 0.15,
        "screening": 0.10,
        "hr": 0.15,
        "technical": 0.35,
        "machine_test": 0.25
    },

    "non_technical": {
        "ats": 0.25,
        "screening": 0.20,
        "hr": 0.35,
        "technical": 0.10,
        "machine_test": 0.10
    }
}


def get_weights(role_type=None):

    return ROLE_WEIGHTS.get(
        role_type,
        DEFAULT_WEIGHTS
    )


# ----------------------------------
# Final Score Calculation
# ----------------------------------

def calculate_final_score(
    scores,
    weights
):

    final_score = 0

    for stage, weight in weights.items():

        final_score += (
            scores.get(stage, 0) * weight
        )

    return round(final_score, 2)


if __name__ == "__main__":

    sample_scores = {
        "ats": 75,
        "screening": 70,
        "hr": 80,
        "technical": 85,
        "machine_test": 78
    }

    weights = get_weights("technical")

    score = calculate_final_score(
        sample_scores,
        weights
    )

    print(score)