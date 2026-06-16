"""
Day 47
Technical Scoring Tests
"""

from technical_ai.technical_scoring_engine import (
    calculate_technical_score
)

from technical_ai.technical_pipeline import (
    technical_pipeline
)


def test_technical_score():

    result = (
        calculate_technical_score(
            "This is a correct answer",
            True
        )
    )

    assert (
        result["technical_score"] > 0
    )


def test_depth_classification():

    result = (
        calculate_technical_score(
            """
            First I design architecture
            because scalable production
            systems require optimization
            and performance tuning.
            """,
            True
        )
    )

    assert (
        result["depth_classification"]
        in [
            "shallow",
            "moderate",
            "deep"
        ]
    )


def test_pipeline():

    result = technical_pipeline(

        answer="""
        First I design architecture,
        then optimize performance
        because production systems
        must scale.
        """,

        difficulty="advanced",

        is_correct=True
    )

    assert (
        result["final_score"] > 0
    )


if __name__ == "__main__":

    test_technical_score()

    test_depth_classification()

    test_pipeline()

    print("All tests passed")