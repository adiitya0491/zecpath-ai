"""
Day 53
Hiring Report Pipeline
"""

from ai_core.hiring_report_generator import (
    generate_hiring_report
)


def hiring_report_pipeline(data):
    """
    Main report generation pipeline.
    """

    report = generate_hiring_report(

        candidate_id=data["candidate_id"],

        ats=data["ats"],

        screening=data["screening"],

        hr=data["hr"],

        technical=data["technical"],

        machine_test=data["machine_test"],

        behavior=data["behavior"],

        decision=data["decision"]
    )

    return report


if __name__ == "__main__":

    sample_data = {

        "candidate_id": "C12001",

        "ats": 78,

        "screening": 72,

        "hr": 80,

        "technical": 85,

        "machine_test": 76,

        "behavior": {

            "confidence": 82,

            "risk_level": "Low Risk",

            "integrity": "Moderate Risk"
        },

        "decision": "Selected"
    }

    result = hiring_report_pipeline(
        sample_data
    )

    print(result)