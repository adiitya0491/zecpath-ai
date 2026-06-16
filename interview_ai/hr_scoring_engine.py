from interview_ai.hr_weights import get_weights


# ==========================================================
# DEFAULT WEIGHTS
# ==========================================================

DEFAULT_WEIGHTS = {
    "relevance": 0.30,
    "communication": 0.25,
    "confidence": 0.25,
    "consistency": 0.20
}


# ==========================================================
# CONSISTENCY SCORE
# ==========================================================

def score_consistency(answer):
    """
    Evaluates answer consistency.
    """

    if answer.get("contradiction", False):
        return 0.3

    if answer.get("is_vague", False):
        return 0.6

    return 1.0


# ==========================================================
# PER QUESTION SCORING
# ==========================================================

def score_hr_answer(answer, weights=DEFAULT_WEIGHTS):

    relevance = answer.get("relevance_score", 0.7)

    communication = (
        answer.get("communication_score", 70) / 100
    )

    confidence = (
        answer.get("confidence_score", 70) / 100
    )

    consistency = score_consistency(answer)

    final_score = (
        relevance * weights["relevance"] +
        communication * weights["communication"] +
        confidence * weights["confidence"] +
        consistency * weights["consistency"]
    )

    return {
        "question_id": answer.get("question_id"),

        "scores": {
            "relevance": round(relevance, 2),
            "communication": round(communication, 2),
            "confidence": round(confidence, 2),
            "consistency": round(consistency, 2)
        },

        "final_score": round(final_score * 100, 2)
    }


# ==========================================================
# AGGREGATE HR SCORE
# ==========================================================

def aggregate_hr_scores(scored_answers):

    if not scored_answers:
        return 0

    total = sum(
        item["final_score"]
        for item in scored_answers
    )

    return round(
        total / len(scored_answers),
        2
    )


# ==========================================================
# NORMALIZATION
# ==========================================================

def normalize_interview_score(score, total_questions):

    if total_questions == 0:
        return 0

    return round(score, 2)


# ==========================================================
# EXPLAINABLE SCORING
# ==========================================================

def generate_explanation(answer):

    explanation = {}

    if answer.get("relevance_score", 0) >= 0.8:
        explanation["relevance"] = (
            "Answer directly addressed the question."
        )
    else:
        explanation["relevance"] = (
            "Answer partially addressed the question."
        )

    if answer.get("communication_score", 0) >= 80:
        explanation["communication"] = (
            "Clear and well-structured response."
        )
    else:
        explanation["communication"] = (
            "Communication could be improved."
        )

    if answer.get("confidence_score", 0) >= 80:
        explanation["confidence"] = (
            "Strong confidence indicators detected."
        )
    else:
        explanation["confidence"] = (
            "Some hesitation detected."
        )

    if answer.get("contradiction"):
        explanation["consistency"] = (
            "Contradiction detected in answer."
        )
    elif answer.get("is_vague"):
        explanation["consistency"] = (
            "Answer appears vague."
        )
    else:
        explanation["consistency"] = (
            "No contradictions detected."
        )

    return explanation


# ==========================================================
# SUMMARY CALCULATOR
# ==========================================================

def build_summary(scored_answers):

    if not scored_answers:
        return {
            "avg_relevance": 0,
            "avg_communication": 0,
            "avg_confidence": 0,
            "avg_consistency": 0
        }

    total_questions = len(scored_answers)

    avg_relevance = sum(
        s["scores"]["relevance"]
        for s in scored_answers
    ) / total_questions

    avg_communication = sum(
        s["scores"]["communication"]
        for s in scored_answers
    ) / total_questions

    avg_confidence = sum(
        s["scores"]["confidence"]
        for s in scored_answers
    ) / total_questions

    avg_consistency = sum(
        s["scores"]["consistency"]
        for s in scored_answers
    ) / total_questions

    return {
        "avg_relevance": round(avg_relevance, 2),
        "avg_communication": round(avg_communication, 2),
        "avg_confidence": round(avg_confidence, 2),
        "avg_consistency": round(avg_consistency, 2)
    }


# ==========================================================
# MAIN HR SCORING PIPELINE
# ==========================================================

def hr_scoring_pipeline(
        answers,
        candidate_type="fresher",
        candidate_id="UNKNOWN"
):

    weights = get_weights(candidate_type)

    scored_answers = []

    for answer in answers:

        result = score_hr_answer(
            answer,
            weights
        )

        result["explanation"] = (
            generate_explanation(answer)
        )

        scored_answers.append(result)

    final_score = aggregate_hr_scores(
        scored_answers
    )

    final_score = normalize_interview_score(
        final_score,
        len(scored_answers)
    )

    if final_score >= 75:
        decision = "Strong Hire"

    elif final_score >= 55:
        decision = "Consider"

    else:
        decision = "Reject"

    return {

        "candidate_id": candidate_id,

        "hr_interview_score": final_score,

        "decision": decision,

        "breakdown": scored_answers,

        "summary": build_summary(
            scored_answers
        )
    }


# ==========================================================
# DEMO EXECUTION
# ==========================================================

if __name__ == "__main__":

    sample_answers = [

        {
            "question_id": "Q1",
            "relevance_score": 0.9,
            "communication_score": 85,
            "confidence_score": 80,
            "contradiction": False,
            "is_vague": False
        },

        {
            "question_id": "Q2",
            "relevance_score": 0.8,
            "communication_score": 78,
            "confidence_score": 75,
            "contradiction": False,
            "is_vague": False
        }
    ]

    report = hr_scoring_pipeline(
        sample_answers,
        "experienced",
        "C123"
    )

    from pprint import pprint
    pprint(report)