"""
Day 52
Final Recommendation AI
Decision Engine
"""

# ----------------------------------
# Decision Thresholds
# ----------------------------------

THRESHOLDS = {
    "selected": 80,
    "hold": 60
}


# ----------------------------------
# Risk Adjustment Logic
# ----------------------------------

def adjust_for_risk(
    score,
    behavior_risk,
    integrity_risk
):

    penalty = 0

    if behavior_risk == "High Risk":
        penalty += 10

    elif behavior_risk == "Moderate Risk":
        penalty += 5

    if integrity_risk == "High Risk":
        penalty += 15

    elif integrity_risk == "Moderate Risk":
        penalty += 7

    return max(score - penalty, 0)


# ----------------------------------
# Decision Logic
# ----------------------------------

def generate_decision(
    final_score,
    behavior_risk="Low Risk",
    integrity_risk="Low Risk"
):

    adjusted_score = adjust_for_risk(
        final_score,
        behavior_risk,
        integrity_risk
    )

    if adjusted_score >= THRESHOLDS["selected"]:

        decision = "Selected"

    elif adjusted_score >= THRESHOLDS["hold"]:

        decision = "Hold / Review"

    else:

        decision = "Rejected"

    return decision, adjusted_score


# ----------------------------------
# Decision Confidence
# ----------------------------------

def calculate_decision_confidence(
    scores
):

    if not scores:
        return 0

    variance = max(scores) - min(scores)

    confidence = max(
        100 - variance,
        50
    )

    return round(confidence, 2)


if __name__ == "__main__":

    decision, score = generate_decision(
        85,
        "Low Risk",
        "Moderate Risk"
    )

    print(decision)
    print(score)