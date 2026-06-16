from interview_ai.followup_engine import (
    detect_answer_quality,
    generate_followup
)

from interview_ai.adaptive_engine import (
    adapt_question_level,
    generate_adaptive_question
)


def followup_pipeline(
    question,
    answer,
    confidence_score
):

    # Step 1
    quality = detect_answer_quality(
        answer
    )

    # Step 2
    followup = generate_followup(
        question,
        quality
    )

    # Step 3
    mode = adapt_question_level(
        quality,
        confidence_score
    )

    # Step 4
    adaptive_question = (
        generate_adaptive_question(
            question,
            mode
        )
    )

    return {
        "quality": quality,
        "followup": followup,
        "next_question": adaptive_question
    }


if __name__ == "__main__":

    result = followup_pipeline(
        question="Tell me about teamwork",
        answer="I worked in a team",
        confidence_score=0.6
    )

    print(result)