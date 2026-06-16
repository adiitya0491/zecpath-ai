from interview_ai.question_generator import generate_questions
from interview_ai.followup_logic import should_trigger_followup


def test_question_generation():

    questions = generate_questions(
        role_type="technical",
        experience_level="fresher"
    )

    assert len(questions) > 0


def test_followup_trigger():

    result = should_trigger_followup(
        "not sure"
    )

    assert result is True


def test_no_followup_needed():

    result = should_trigger_followup(
        "I have strong teamwork and communication skills developed through multiple projects."
    )

    assert result is False