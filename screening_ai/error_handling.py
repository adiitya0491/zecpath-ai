RETRY_MESSAGES = {
    "silence":
        "Sorry, I didn't hear anything. Could you please respond?",

    "confusion":
        "Let me clarify the question for you.",

    "repeat":
        "Could you provide more details?"
}


def detect_issue(answer):

    if not answer:
        return "silence"

    answer = answer.strip()

    if len(answer) == 0:
        return "silence"

    words = answer.split()

    if len(words) < 2:
        return "confusion"

    unique_words = set(words)

    if len(unique_words) < len(words) / 2:
        return "repeat"

    return "valid"


def handle_response(state_machine, answer):

    issue = detect_issue(answer)

    if issue == "silence":

        state_machine.handle_silence()

    elif issue == "confusion":

        state_machine.handle_confusion()

    elif issue == "repeat":

        state_machine.handle_repeat()

    else:

        state_machine.next()

    return issue

# -----------------------------------
# Adaptive Retry Logic
# -----------------------------------

def adaptive_retry_logic(
    issue,
    retry_count
):

    if issue == "silence":

        if retry_count == 0:

            return "retry"

        elif retry_count == 1:

            return "simplify_question"

        else:

            return "skip_question"

    if issue == "confusion":

        return "clarify"

    if issue == "repeat":

        return "ask_example"

    return "next"