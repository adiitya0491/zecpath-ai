ERROR_RESPONSES = {
    "missing":
        "I didn't receive your response. Could you please answer?",

    "poor_audio":
        "The audio is unclear. Could you please repeat?",

    "unclear":
        "Can you explain that a little more clearly?",

    "language_mix":
        "Would you prefer to continue in another language?",

    "incomplete":
        "Could you provide a bit more detail?",

    "fallback":
        "Let's move on to the next question."
}


def get_error_response(issue):
    """
    Return recruiter-friendly fallback message.
    """
    return ERROR_RESPONSES.get(
        issue,
        ERROR_RESPONSES["fallback"]
    )


def fallback_strategy(issue, retry_count):
    """
    Retry strategy to avoid infinite loops.
    """

    if retry_count >= 2:
        return "skip_question"

    if issue in ["missing", "poor_audio"]:
        return "retry"

    if issue == "language_mix":
        return "switch_language"

    return "clarify"