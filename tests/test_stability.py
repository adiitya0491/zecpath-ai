from interview_ai.stable_hr_ai import (
    stable_hr_evaluation
)

from interview_ai.refined_scoring import (
    normalize_scores
)

from interview_ai.followup_stability import (
    stable_followup
)

from screening_ai.optimized_cleaner import (
    advanced_clean
)


def test_stability():

    result = stable_hr_evaluation(
        [50, 60, 90, 30]
    )

    assert result["stable_score"] > 0


def test_normalization():

    result = normalize_scores(
        [10, 20, 30]
    )

    assert len(result) == 3


def test_followup():

    result = stable_followup(
        "too_short",
        1
    )

    assert result == "clarify"


def test_cleaner():

    cleaned = advanced_clean(
        "um um python python !!!"
    )

    assert "um" not in cleaned