"""
Day 51
Cross Round Aggregation Tests
"""

from ai_core.cross_round_engine import (
    calculate_final_score
)

from ai_core.aggregation_pipeline import (
    aggregation_pipeline
)

from ai_core.hiring_fit_calculator import (
    calculate_hiring_fit
)


def test_final_score():

    scores = {

        "ats": 70,

        "screening": 70,

        "hr": 70,

        "technical": 70,

        "machine_test": 70
    }

    weights = {

        "ats": 0.20,

        "screening": 0.20,

        "hr": 0.20,

        "technical": 0.20,

        "machine_test": 0.20
    }

    score = calculate_final_score(
        scores,
        weights
    )

    assert score == 70


def test_hiring_fit():

    result = calculate_hiring_fit(85)

    assert (
        result["fit_category"]
        == "Excellent Fit"
    )


def test_aggregation_pipeline():

    scores = {

        "ats": 75,

        "screening": 70,

        "hr": 80,

        "technical": 85,

        "machine_test": 78
    }

    result = aggregation_pipeline(
        "C9001",
        scores,
        "technical"
    )

    assert "final_score" in result

    assert "decision" in result

    assert "hiring_fit" in result


if __name__ == "__main__":

    test_final_score()

    test_hiring_fit()

    test_aggregation_pipeline()

    print("All tests passed")