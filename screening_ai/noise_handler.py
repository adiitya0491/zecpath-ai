import re


def clean_noise(text):
    """
    Remove noise markers and repeated characters.
    """

    text = re.sub(r"\[.*?\]", "", text)

    text = re.sub(
        r"(.)\1{2,}",
        r"\1",
        text
    )

    return text.strip()


def detect_language_mix(text):
    """
    Detect local-language words mixed with English.
    """

    local_words = [
        "hai",
        "enna",
        "chetta",
        "bhai"
    ]

    text = text.lower()

    for word in local_words:
        if word in text:
            return True

    return False