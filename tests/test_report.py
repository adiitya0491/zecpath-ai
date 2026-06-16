"""
Day 53
Hiring Report Tests
"""

from ai_core.hiring_report_generator import (
    generate_hiring_report
)

from ai_core.report_pipeline import (
    hiring_report_pipeline
)


def test_report_generator():

    result = generate_hiring_report(

        candidate_id="C1",

        ats=70,

        screening=70,

        hr=70,

        technical=70,

        machine_test=70,

        behavior={

            "risk_level":
                "Low Risk",

            "integrity":
                "Low Risk"
        },

        decision="Selected"
    )

    assert "candidate_id" in result


def test_pipeline():

    data = {

        "candidate_id": "C1",

        "ats": 70,

        "screening": 70,

        "hr": 70,

        "technical": 70,

        "machine_test": 70,

        "behavior": {

            "risk_level":
                "Low Risk",

            "integrity":
                "Low Risk"
        },

        "decision":
            "Selected"
    }

    result = hiring_report_pipeline(
        data
    )

    assert (
        result["candidate_id"]
        == "C1"
    )


if __name__ == "__main__":

    test_report_generator()

    test_pipeline()

    print("All tests passed")