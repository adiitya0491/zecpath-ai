from technical_ai.technical_scoring_engine import (
    calculate_technical_score
)


# -----------------------------------
# Difficulty Normalization
# -----------------------------------

def normalize_difficulty(
    score,
    difficulty
):

    multipliers = {

        "basic": 1.0,

        "intermediate": 1.1,

        "advanced": 1.2
    }

    adjusted_score = (
        score *
        multipliers.get(
            difficulty,
            1.0
        )
    )

    return min(
        round(adjusted_score, 2),
        100
    )


# -----------------------------------
# Technical Pipeline
# -----------------------------------

def technical_pipeline(
    answer,
    difficulty,
    is_correct=True
):

    base_result = (
        calculate_technical_score(
            answer,
            is_correct
        )
    )

    normalized_score = (
        normalize_difficulty(
            base_result["technical_score"],
            difficulty
        )
    )

    return {

        "final_score":
            normalized_score,

        "difficulty":
            difficulty,

        "details":
            base_result
    }


if __name__ == "__main__":

    sample = """
    First I design architecture,
    then optimize performance
    because production systems
    need scalability.
    """

    result = technical_pipeline(
        sample,
        "advanced",
        True
    )

    print(result)