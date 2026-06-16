from interview_ai.followup_engine import (
    detect_answer_quality
)


def test_followup():

    result = detect_answer_quality(
        "I worked"
    )

    assert result == "too_short"


def test_uncertain_answer():

    result = detect_answer_quality(
        "Maybe I can do it"
    )

    assert result == "uncertain"


def test_good_answer():

    result = detect_answer_quality(
        "I worked with a team of developers and successfully completed multiple projects."
    )

    assert result == "good"