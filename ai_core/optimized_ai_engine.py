"""
Day 54 - Optimized AI Engine
Zecpath AI
"""

# ---------------------------------
# Dynamic Threshold Optimization
# ---------------------------------

THRESHOLDS = {
    "selected": 78,
    "hold": 58
}


# ---------------------------------
# False Positive / Negative Fix
# ---------------------------------

def adjust_decision(score, technical, integrity_risk):
    """
    Improve decision accuracy by correcting edge cases.
    """

    # Prevent false positives
    if score > 80 and integrity_risk == "High Risk":
        return "Hold / Review"

    # Prevent false negatives
    if score < 60 and technical > 85:
        return "Hold / Review"

    # Standard decision logic
    if score >= THRESHOLDS["selected"]:
        return "Selected"

    elif score >= THRESHOLDS["hold"]:
        return "Hold / Review"

    return "Rejected"


if __name__ == "__main__":

    print(
        adjust_decision(
            score=85,
            technical=90,
            integrity_risk="High Risk"
        )
    )