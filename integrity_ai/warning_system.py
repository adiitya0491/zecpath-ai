"""
Day 49
Real-Time Warning System
"""


def generate_warning(events):

    warnings = []

    if events.get("tab_switch", 0) > 2:
        warnings.append(
            "Please stay on the interview screen."
        )

    if events.get("voice_detect", 0) > 1:
        warnings.append(
            "External voice detected. Please ensure you are alone."
        )

    if events.get("focus_loss", 0) > 3:
        warnings.append(
            "You seem distracted. Please focus on the interview."
        )

    if events.get("gaze_off", 0) > 4:
        warnings.append(
            "Please maintain attention during the interview."
        )

    return warnings


if __name__ == "__main__":

    sample = {
        "tab_switch": 4,
        "focus_loss": 5,
        "voice_detect": 2,
        "gaze_off": 6
    }

    print(generate_warning(sample))