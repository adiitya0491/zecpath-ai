"""
Day 49
Malpractice Detection Logic
"""

THRESHOLDS = {
    "tab_switch": 3,
    "focus_loss": 5,
    "voice_detect": 2,
    "gaze_off": 5,
    "idle_time": 30
}


def detect_malpractice(events):
    """
    Detect threshold violations.
    """

    flags = []

    if events.get("tab_switch", 0) > THRESHOLDS["tab_switch"]:
        flags.append("High Tab Switching")

    if events.get("focus_loss", 0) > THRESHOLDS["focus_loss"]:
        flags.append("Screen Focus Loss")

    if events.get("voice_detect", 0) > THRESHOLDS["voice_detect"]:
        flags.append("Multiple Voices Detected")

    if events.get("gaze_off", 0) > THRESHOLDS["gaze_off"]:
        flags.append("Frequent Gaze Deviation")

    if events.get("idle_time", 0) > THRESHOLDS["idle_time"]:
        flags.append("Long Idle Time")

    return flags


def detect_patterns(events):
    """
    Detect suspicious behavior combinations.
    """

    patterns = []

    if (
        events.get("tab_switch", 0) >= 3 and
        events.get("focus_loss", 0) >= 3
    ):
        patterns.append(
            "Possible External Search Activity"
        )

    if (
        events.get("voice_detect", 0) >= 2 and
        events.get("idle_time", 0) >= 20
    ):
        patterns.append(
            "Possible External Assistance"
        )

    if (
        events.get("gaze_off", 0) >= 5 and
        events.get("idle_time", 0) >= 15
    ):
        patterns.append(
            "Possible Note Reading"
        )

    return patterns


if __name__ == "__main__":

    sample_events = {
        "tab_switch": 5,
        "focus_loss": 2,
        "voice_detect": 1,
        "gaze_off": 6,
        "idle_time": 35
    }

    print(detect_malpractice(sample_events))
    print(detect_patterns(sample_events))