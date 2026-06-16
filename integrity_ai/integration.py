"""
Day 49
Integrity + Behavioral Integration
"""

from integrity_ai.detection_logic import (
    detect_malpractice,
    detect_patterns
)

from integrity_ai.risk_engine import (
    calculate_integrity_score,
    risk_flagging
)

from integrity_ai.warning_system import (
    generate_warning
)


def combined_risk(
    behavior_score,
    integrity_score
):
    """
    Combine behavioral and integrity scores.
    """

    final = (
        behavior_score * 0.4 +
        integrity_score * 0.6
    )

    return round(final, 2)


def integrity_pipeline(
    candidate_id,
    events,
    behavior_score=75
):

    flags = detect_malpractice(events)

    patterns = detect_patterns(events)

    integrity_score = calculate_integrity_score(
        events
    )

    risk_level = risk_flagging(
        integrity_score
    )

    warnings = generate_warning(events)

    combined_score = combined_risk(
        behavior_score,
        integrity_score
    )

    return {

        "candidate_id": candidate_id,

        "integrity_score": integrity_score,

        "combined_score": combined_score,

        "risk_level": risk_level,

        "flags": flags,

        "patterns": patterns,

        "warnings": warnings
    }


if __name__ == "__main__":

    sample_events = {

        "tab_switch": 5,

        "focus_loss": 3,

        "voice_detect": 1,

        "gaze_off": 6,

        "idle_time": 25
    }

    result = integrity_pipeline(
        "C4001",
        sample_events,
        80
    )

    print(result)