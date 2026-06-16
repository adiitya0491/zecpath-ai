from screening_ai.question_templates import (
    generate_skill_question
)

def test_template():

    q = generate_skill_question(
        "Backend Developer"
    )

    assert (
        "Backend Developer"
        in q
    )