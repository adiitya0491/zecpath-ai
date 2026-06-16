WEIGHTS = {

    "clarity":0.25,

    "relevance":0.30,

    "completeness":0.25,

    "consistency":0.20
}

def score_clarity(answer):

    text = answer.get(
        "original_text",
        ""
    )

    length = len(
        text.split()
    )

    if length > 8:
        return 1.0

    elif length > 4:
        return 0.7

    elif length > 1:
        return 0.4

    return 0.0

def score_relevance(
    answer,
    expected_intent
):

    return (

        1.0

        if answer.get("intent")
        == expected_intent

        else 0.3
    )

def score_completeness(
    answer
):

    score = 0

    if answer.get("skills"):
        score += 0.4

    if (
        answer.get(
            "experience_years",
            0
        ) > 0
    ):
        score += 0.3

    if (
        answer.get(
            "availability"
        )
        != "Unknown"
    ):
        score += 0.3

    return min(
        score,
        1.0
    )

def score_consistency(
    answer
):

    if answer.get(
        "is_vague"
    ):
        return 0.3

    if answer.get(
        "off_topic"
    ):
        return 0.2

    return 1.0

def score_answer(
    answer,
    expected_intent
):

    clarity = score_clarity(
        answer
    )

    relevance = score_relevance(
        answer,
        expected_intent
    )

    completeness = score_completeness(
        answer
    )

    consistency = score_consistency(
        answer
    )

    final = (

        clarity
        * WEIGHTS["clarity"]

        +

        relevance
        * WEIGHTS["relevance"]

        +

        completeness
        * WEIGHTS["completeness"]

        +

        consistency
        * WEIGHTS["consistency"]
    )

    return {
        "question_id": answer["question_id"],

        "scores": {
            "clarity": round(clarity, 2),
            "relevance": round(relevance, 2),
            "completeness": round(completeness, 2),
            "consistency": round(consistency, 2)
        },

        "final_score": round(final * 100, 2),

        "explanation": {

            "clarity":
            "Answer is detailed and understandable"
            if clarity >= 0.7
            else "Answer is too short",

            "relevance":
            "Matches expected question intent"
            if relevance >= 1.0
            else "Answer is not fully relevant",

            "completeness":
            "Contains important candidate information"
            if completeness >= 0.7
            else "Some required details are missing",

            "consistency":
            "No vague or off-topic indicators"
            if consistency >= 1.0
            else "Answer appears vague or off-topic"
        }
    }

def aggregate_scores(
    scored_answers
):

    if not scored_answers:
        return 0

    total = sum(

        a["final_score"]

        for a in scored_answers
    )

    avg = (
        total /
        len(scored_answers)
    )

    return round(
        avg,
        2
    )

def screening_scoring_pipeline(
    answers,
    intent_map
):

    scored_answers = []

    for ans in answers:

        expected_intent = (

            intent_map.get(
                ans["question_id"],
                "unknown"
            )
        )

        scored = score_answer(
            ans,
            expected_intent
        )

        scored_answers.append(
            scored
        )

    final_score = aggregate_scores(
        scored_answers
    )

    decision = (

        "Pass"

        if final_score >= 60

        else

        "Review"

        if final_score >= 40

        else

        "Reject"
    )

    return {

        "screening_score":
        final_score,

        "decision":
        decision,

        "details":
        scored_answers
    }

def normalize_score(
    score,
    max_score=100
):

    return round(

        (score / max_score)
        * 100,

        2
    )

