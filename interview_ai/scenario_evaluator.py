# interview_ai/scenario_evaluator.py

IDEAL_PATTERNS = {
    "team_conflict": [
        "communicate",
        "understand",
        "resolve"
    ],
    "deadline_pressure": [
        "prioritize",
        "plan",
        "execute"
    ],
    "learning": [
        "research",
        "practice",
        "apply"
    ]
}


def evaluate_scenario(text, scenario_type):
    """
    Evaluate candidate answer against ideal patterns.
    """

    text = text.lower()

    patterns = IDEAL_PATTERNS.get(
        scenario_type,
        []
    )

    if not patterns:
        return 0.4

    matches = sum(
        1 for pattern in patterns
        if pattern in text
    )

    if matches == len(patterns):
        return 1.0

    elif matches > 0:
        return 0.7

    return 0.4