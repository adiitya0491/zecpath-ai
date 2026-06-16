from screening_ai.answer_engine import (
    process_answer
)

def test_answer_processing():

    text = (
        "I have 2 years "
        "experience in Python"
    )

    result = process_answer(
        "Q3",
        text
    )

    assert (
        result["intent"]
        == "experience"
    )

    assert (
        result["experience_years"]
        == 2
    )

    assert (
        "python"
        in result["skills"]
    )