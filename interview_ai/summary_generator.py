"""
Day 39 - Interview Summary Generator

Generates recruiter-ready interview summaries
from HR, communication, and behavioral analysis.
"""


def generate_natural_summary(
    strengths,
    weaknesses,
    risks,
    culture_fit,
    decision
):
    """
    Generate a human-readable summary.
    """

    strengths_text = (
        ", ".join(strengths[:2])
        if strengths
        else "some positive qualities"
    )

    weaknesses_text = (
        ", ".join(weaknesses[:2])
        if weaknesses
        else "no major weaknesses"
    )

    risks_text = (
        ", ".join(risks)
        if risks
        else "no major risks"
    )

    return (
        f"The candidate demonstrates {strengths_text}. "
        f"However, there are concerns such as {weaknesses_text}. "
        f"Risk factors include {risks_text}. "
        f"Cultural fit is assessed as {culture_fit}. "
        f"Final Recommendation: {decision}."
    )


def generate_interview_summary(
    candidate_id,
    hr_scores,
    communication,
    behavior,
    answers
):
    """
    Main summary generator.
    """

    strengths = []
    weaknesses = []
    risks = []
    inconsistencies = []

    # --------------------------------
    # HR Score Analysis
    # --------------------------------

    for item in hr_scores:

        score = item.get("final_score", 0)

        if score >= 80:
            strengths.append(
                f"Strong performance in {item['question_id']}"
            )

        elif score < 50:
            weaknesses.append(
                f"Weak response in {item['question_id']}"
            )

    # --------------------------------
    # Communication Analysis
    # --------------------------------

    communication_score = communication.get(
        "communication_score",
        0
    )

    if communication_score >= 80:
        strengths.append(
            "Excellent communication skills"
        )

    elif communication_score < 50:
        weaknesses.append(
            "Poor communication clarity"
        )

    # --------------------------------
    # Behavior Analysis
    # --------------------------------

    confidence_score = (
        behavior.get("confidence", {})
        .get("confidence_score", 0)
    )

    if confidence_score < 60:
        risks.append(
            "Low confidence detected"
        )

    if behavior.get("contradiction", False):
        inconsistencies.append(
            "Contradictory statements observed"
        )

    # --------------------------------
    # Cultural Fit
    # --------------------------------

    culture_fit = "Good"

    all_answers = " ".join(
        str(answer) for answer in answers
    ).lower()

    teamwork_keywords = [
        "team",
        "collaboration",
        "together",
        "group"
    ]

    if any(
        keyword in all_answers
        for keyword in teamwork_keywords
    ):
        strengths.append(
            "Shows teamwork orientation"
        )
    else:
        culture_fit = "Moderate"

    # --------------------------------
    # HR Average Score
    # --------------------------------

    if hr_scores:
        avg_hr_score = (
            sum(
                item["final_score"]
                for item in hr_scores
            )
            / len(hr_scores)
        )
    else:
        avg_hr_score = 0

    # --------------------------------
    # Overall Score
    # --------------------------------

    overall_score = (
        communication_score * 0.30
        + behavior.get("behavioral_score", 0) * 0.30
        + avg_hr_score * 0.40
    )

    # --------------------------------
    # Hiring Decision
    # --------------------------------

    if overall_score >= 75:
        decision = "Strong Hire"

    elif overall_score >= 55:
        decision = "Consider"

    else:
        decision = "Reject"

    # --------------------------------
    # Natural Language Summary
    # --------------------------------

    summary_text = generate_natural_summary(
        strengths,
        weaknesses,
        risks,
        culture_fit,
        decision
    )

    return {
        "candidate_id": candidate_id,
        "overall_score": round(overall_score, 2),
        "decision": decision,
        "summary": {
            "strengths": strengths,
            "weaknesses": weaknesses,
            "risks": risks,
            "inconsistencies": inconsistencies,
            "cultural_fit": culture_fit
        },
        "natural_language_summary": summary_text
    }