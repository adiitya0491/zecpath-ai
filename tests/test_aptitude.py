from interview_ai.aptitude_scoring import calculate_aptitude_score
from interview_ai.scenario_evaluator import evaluate_scenario
from interview_ai.aptitude_pipeline import aptitude_pipeline


def test_aptitude_score():
    result = calculate_aptitude_score(
        "First I analyze the problem then solve it."
    )

    assert result["aptitude_score"] > 0


def test_scenario_evaluation():
    text = (
        "I would communicate with the team, "
        "understand the issue and resolve it."
    )

    score = evaluate_scenario(
        text,
        "team_conflict"
    )

    assert score > 0


def test_aptitude_pipeline():
    result = aptitude_pipeline(
        "First I analyze the problem and then create a solution.",
        "deadline_pressure"
    )

    assert "aptitude_score" in result