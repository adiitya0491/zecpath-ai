# ==========================================================
# CONTRADICTION DETECTOR
# ==========================================================

def detect_contradiction(text):
    text = text.lower()

    contradiction_keywords = [
        "but",
        "however",
        "although",
        "yet"
    ]

    if any(
        keyword in text
        for keyword in contradiction_keywords
    ):
        return True

    if (
        "i don't know" in text
        and
        "experience" in text
    ):
        return True

    if (
        "no experience" in text
        and
        "worked on" in text
    ):
        return True

    return False