# ----------------------------------
# Behavioral Score Calculation
# ----------------------------------

def calculate_behavior_score(signals):
    """
    signals = {
        "eye_focus": 0-1,
        "head_stability": 0-1,
        "engagement": 0-1,
        "distraction": 0-1
    }
    """

    focus = signals.get("eye_focus", 0.5)
    head = signals.get("head_stability", 0.5)
    engagement = signals.get("engagement", 0.5)
    distraction = signals.get("distraction", 0.5)

    score = (
        focus * 0.30 +
        head * 0.20 +
        engagement * 0.30 +
        (1 - distraction) * 0.20
    )

    return round(score * 100, 2)


# ----------------------------------
# Focus Level
# ----------------------------------

def detect_focus_level(score):

    if score >= 85:
        return "High"

    elif score >= 70:
        return "Medium"

    return "Low"


# ----------------------------------
# Engagement Level
# ----------------------------------

def detect_engagement_level(engagement):

    if engagement >= 0.8:
        return "Strong"

    elif engagement >= 0.6:
        return "Moderate"

    return "Weak"


# ----------------------------------
# Risk Detection
# ----------------------------------

def detect_behavior_risk(score):

    if score < 50:
        return "High Risk"

    elif score < 70:
        return "Moderate Risk"

    return "Low Risk"


# ----------------------------------
# Full Behavioral Analysis
# ----------------------------------

def analyze_behavior(signals):

    score = calculate_behavior_score(signals)

    return {
        "behavior_score": score,

        "signals": signals,

        "insights": {

            "focus_level":
                detect_focus_level(score),

            "engagement":
                detect_engagement_level(
                    signals.get(
                        "engagement",
                        0.5
                    )
                ),

            "risk":
                detect_behavior_risk(score)
        }
    }


# ----------------------------------
# Example Run
# ----------------------------------

if __name__ == "__main__":

    sample_signals = {

        "eye_focus": 0.8,

        "head_stability": 0.7,

        "engagement": 0.9,

        "distraction": 0.2
    }

    result = analyze_behavior(
        sample_signals
    )

    print(result)