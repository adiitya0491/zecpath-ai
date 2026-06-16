"""
Day 49
Integrity Risk Engine
"""


def calculate_integrity_score(events):

    score = 100

    score -= events.get("tab_switch", 0) * 5
    score -= events.get("focus_loss", 0) * 3
    score -= events.get("voice_detect", 0) * 10
    score -= events.get("gaze_off", 0) * 4
    score -= events.get("idle_time", 0) * 0.5

    return max(round(score, 2), 0)


def risk_flagging(score):

    if score < 50:
        return "High Risk"

    elif score < 75:
        return "Moderate Risk"

    return "Low Risk"


if __name__ == "__main__":

    events = {
        "tab_switch": 2,
        "focus_loss": 1,
        "voice_detect": 0,
        "gaze_off": 2,
        "idle_time": 10
    }

    score = calculate_integrity_score(events)

    print(score)
    print(risk_flagging(score))