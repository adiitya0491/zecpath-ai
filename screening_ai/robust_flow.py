from screening_ai.error_handling import detect_issue


def detect_edge_case(answer, confidence=1.0):
    """
    Detect common real-world interview issues.
    """

    if not answer or len(answer.strip()) == 0:
        return "missing"

    if confidence < 0.6:
        return "poor_audio"

    if any(word in answer.lower() for word in ["um", "uh"]):
        if len(answer.split()) < 3:
            return "unclear"

    if any(word in answer.lower() for word in ["hai", "enna", "chetta", "bhai"]):
        return "language_mix"

    if len(answer.split()) < 2:
        return "incomplete"

    return "valid"


def handle_edge_case(
    state_machine,
    answer,
    confidence,
    retry_count
):
    """
    Decide next action based on detected issue.
    """

    issue = detect_edge_case(answer, confidence)

    if issue == "missing":
        return "retry"

    elif issue == "poor_audio":
        return "ask_repeat_audio"

    elif issue == "unclear":
        return "simplify_question"

    elif issue == "language_mix":
        return "switch_language"

    elif issue == "incomplete":
        return "ask_detail"

    return "next"