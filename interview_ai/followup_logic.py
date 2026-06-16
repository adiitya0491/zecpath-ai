def should_trigger_followup(answer):
    """
    Decide if follow-up question is needed.
    """

    if not answer:
        return True

    answer = answer.strip().lower()

    if len(answer.split()) < 5:
        return True

    if "not sure" in answer:
        return True

    if "maybe" in answer:
        return True

    if "i don't know" in answer:
        return True

    return False


def generate_followup(question):
    return f"Could you please elaborate more on: {question}"


if __name__ == "__main__":

    answer = "Not sure"

    if should_trigger_followup(answer):
        print(
            generate_followup(
                "What are your strengths?"
            )
        )