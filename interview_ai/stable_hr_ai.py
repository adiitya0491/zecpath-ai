"""
Stable HR AI
Zecpath AI - Day 42

Provides:
- Score smoothing
- Stable hiring decisions
- Outlier handling
"""

DECISION_THRESHOLDS = {
    "hire": 75,
    "consider": 55
}


def smooth_score(scores):
    """
    Remove extreme outliers and
    calculate stable average.
    """

    if not scores:
        return 0

    avg = sum(scores) / len(scores)

    filtered = [
        s for s in scores
        if abs(s - avg) <= 20
    ]

    if filtered:
        return round(
            sum(filtered) / len(filtered),
            2
        )

    return round(avg, 2)


def stable_decision(score):
    """
    Stable decision logic.
    """

    if score >= DECISION_THRESHOLDS["hire"]:
        return "Hire"

    if score >= DECISION_THRESHOLDS["consider"]:
        return "Consider"

    return "Reject"


def stable_hr_evaluation(scores):
    """
    Final stable HR evaluation.
    """

    smoothed = smooth_score(scores)

    decision = stable_decision(smoothed)

    return {
        "stable_score": smoothed,
        "decision": decision
    }


if __name__ == "__main__":

    result = stable_hr_evaluation(
        [50, 60, 90, 30]
    )

    print(result)