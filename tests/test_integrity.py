"""
Day 49
Integrity Detection Tests
"""

from integrity_ai.risk_engine import (
    calculate_integrity_score,
    risk_flagging
)

from integrity_ai.detection_logic import (
    detect_malpractice
)

from integrity_ai.integration import (
    integrity_pipeline
)


def test_integrity_score():

    score = calculate_integrity_score({

        "tab_switch": 2,

        "focus_loss": 1,

        "voice_detect": 0,

        "gaze_off": 2,

        "idle_time": 10
    })

    assert score > 0


def test_risk_level():

    level = risk_flagging(85)

    assert level == "Low Risk"


def test_flag_detection():

    flags = detect_malpractice({

        "tab_switch": 5,

        "focus_loss": 6,

        "voice_detect": 3,

        "gaze_off": 7,

        "idle_time": 40
    })

    assert len(flags) > 0


def test_pipeline():

    result = integrity_pipeline(

        "C4001",

        {

            "tab_switch": 2,

            "focus_loss": 1,

            "voice_detect": 0,

            "gaze_off": 1,

            "idle_time": 5
        },

        80
    )

    assert "integrity_score" in result

    assert "risk_level" in result


if __name__ == "__main__":

    test_integrity_score()

    test_risk_level()

    test_flag_detection()

    test_pipeline()

    print("All tests passed")