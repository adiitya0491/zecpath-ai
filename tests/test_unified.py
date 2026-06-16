from ai_core.unified_scoring_engine import (
    calculate_unified_score,
    get_weights
)

from ai_core.hiring_fit import (
    calculate_hiring_fit
)

from ai_core.scoring_pipeline import (
    unified_scoring_pipeline
)


def test_unified_score():

    result = calculate_unified_score(
        80,
        70,
        85,
        {
            "ats": 0.30,
            "screening": 0.30,
            "hr": 0.40
        }
    )

    assert result > 0


def test_weights():

    weights = get_weights("technical")

    assert weights["ats"] == 0.40


def test_hiring_fit():

    fit = calculate_hiring_fit(82)

    assert fit["fit_category"] == "Excellent Fit"


def test_pipeline():

    result = unified_scoring_pipeline(
        candidate_id="C101",
        ats=80,
        screening=75,
        hr=85,
        candidate_type="technical"
    )

    assert "final_score" in result
    assert "decision" in result