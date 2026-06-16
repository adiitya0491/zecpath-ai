"""
Day 57
Stable AI Core System
Zecpath AI
"""


def safe_score(value):
    """
    Convert score safely into range 0-100.
    """

    try:
        value = float(value)

    except (TypeError, ValueError):
        return 0

    return max(min(value, 100), 0)


def stable_aggregate(scores):
    """
    Aggregate scores safely.
    """

    cleaned = {
        key: safe_score(value)
        for key, value in scores.items()
    }

    if not cleaned:
        return 0

    avg = sum(cleaned.values()) / len(cleaned)

    return round(avg, 2)


def stable_decision(score):
    """
    Stable decision thresholds.
    """

    if score >= 75:
        return "Selected"

    if score >= 55:
        return "Hold / Review"

    return "Rejected"


def stable_pipeline(candidate_id, scores):
    """
    Final stable pipeline.
    """

    final_score = stable_aggregate(scores)

    decision = stable_decision(final_score)

    return {
        "candidate_id": candidate_id,
        "final_score": final_score,
        "decision": decision,
        "status": "stable"
    }


if __name__ == "__main__":

    result = stable_pipeline(
        "C1001",
        {
            "ats": 120,
            "screening": 75,
            "hr": -10,
            "technical": 90
        }
    )

    print(result)