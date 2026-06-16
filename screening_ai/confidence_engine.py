import re

HESITATION_WORDS = [

    "um",

    "uh",

    "hmm",

    "maybe",

    "not sure",

    "i think"
]

def detect_hesitation(text):

    text = text.lower()

    count = sum(
        text.count(word)
        for word in HESITATION_WORDS
    )

    return min(
        count / 5,
        1.0
    )

def response_length_score(text):

    word_count = len(
        text.split()
    )

    if word_count > 12:
        return 1.0

    elif word_count > 6:
        return 0.7

    elif word_count > 2:
        return 0.4

    return 0.1

def pace_score(
    text,
    duration_seconds
):

    if duration_seconds == 0:
        return 0

    words_per_second = (
        len(text.split())
        / duration_seconds
    )

    if 1.5 <= words_per_second <= 3:
        return 1.0

    elif (
        1.0 <= words_per_second < 1.5
        or
        3 < words_per_second <= 4
    ):
        return 0.7

    return 0.4

def calculate_confidence(
    text,
    duration_seconds
):

    hesitation = detect_hesitation(text)

    length = response_length_score(text)

    pace = pace_score(
        text,
        duration_seconds
    )

    confidence = (

        length * 0.4

        +

        pace * 0.4

        +

        (1 - hesitation) * 0.2
    )

    return {

        "confidence_score":
        round(confidence, 2),

        "signals": {

            "hesitation":
            round(hesitation, 2),

            "length_score":
            round(length, 2),

            "pace_score":
            round(pace, 2)
        }
    }

