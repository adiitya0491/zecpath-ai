"""
Day 52
Explainable Output Generator
"""


def generate_explanation(
    scores,
    decision
):

    strengths = []
    weaknesses = []

    if scores.get("technical", 0) > 80:
        strengths.append(
            "Strong technical skills"
        )

    if scores.get("communication", 0) > 75:
        strengths.append(
            "Good communication"
        )

    if scores.get("machine_test", 0) > 75:
        strengths.append(
            "Good practical performance"
        )

    if scores.get("behavior", 100) < 60:
        weaknesses.append(
            "Behavioral concerns detected"
        )

    if scores.get("integrity", 100) < 60:
        weaknesses.append(
            "Integrity risks detected"
        )

    if decision == "Selected":

        reason = (
            "Strong overall performance "
            "with acceptable risk levels."
        )

    elif decision == "Hold / Review":

        reason = (
            "Moderate performance. "
            "Requires recruiter review."
        )

    else:

        reason = (
            "Low performance and/or "
            "high risk indicators."
        )

    return {

        "reason": reason,

        "strengths": strengths,

        "weaknesses": weaknesses
    }


if __name__ == "__main__":

    sample_scores = {

        "technical": 85,

        "communication": 80,

        "machine_test": 78,

        "behavior": 70,

        "integrity": 80
    }

    print(
        generate_explanation(
            sample_scores,
            "Selected"
        )
    )