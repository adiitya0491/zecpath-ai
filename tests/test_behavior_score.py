"""
Day 48
Behavioral AI Tests
"""

from behavior_ai.signal_mapping import (
    calculate_behavior_score,
    analyze_behavior,
    detect_behavior_risk
)


def test_behavior_score():

    result = calculate_behavior_score({

        "eye_focus": 0.7,

        "head_stability": 0.7,

        "engagement": 0.7,

        "distraction": 0.3
    })

    assert result > 0


def test_behavior_analysis():

    result = analyze_behavior({

        "eye_focus": 0.8,

        "head_stability": 0.8,

        "engagement": 0.9,

        "distraction": 0.2
    })

    assert "behavior_score" in result

    assert "insights" in result


def test_risk_detection():

    assert detect_behavior_risk(85) == "Low Risk"

    assert detect_behavior_risk(60) == "Moderate Risk"

    assert detect_behavior_risk(40) == "High Risk"


if __name__ == "__main__":

    test_behavior_score()

    test_behavior_analysis()

    test_risk_detection()

    print("All tests passed")