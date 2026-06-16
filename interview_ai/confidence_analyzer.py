import re

# ==========================================================
# HESITATION & UNCERTAINTY CONFIG
# ==========================================================

HESITATION_WORDS = [
    "um",
    "uh",
    "hmm",
    "er",
    "ah"
]

UNCERTAINTY_PHRASES = [
    "not sure",
    "maybe",
    "i think",
    "probably",
    "i guess",
    "possibly"
]


# ==========================================================
# REPEATED WORD SCORE
# ==========================================================

def repeated_word_score(text):
    words = text.lower().split()

    if not words:
        return 0.0

    repeats = len(words) - len(set(words))
    ratio = repeats / len(words)

    if ratio < 0.10:
        return 1.0
    elif ratio < 0.30:
        return 0.7
    else:
        return 0.4


# ==========================================================
# HESITATION SCORE
# ==========================================================

def hesitation_score(text):
    text = text.lower()

    count = sum(
        text.count(word)
        for word in HESITATION_WORDS
    )

    penalty = min(count * 0.2, 1.0)

    return max(0.0, 1.0 - penalty)


# ==========================================================
# UNCERTAINTY SCORE
# ==========================================================

def uncertainty_score(text):
    text = text.lower()

    count = sum(
        phrase in text
        for phrase in UNCERTAINTY_PHRASES
    )

    if count == 0:
        return 1.0
    elif count == 1:
        return 0.6
    else:
        return 0.3


# ==========================================================
# PAUSE SCORE
# ==========================================================

def pause_score(duration, word_count):
    if word_count == 0:
        return 0.0

    if duration <= 0:
        return 1.0

    words_per_second = word_count / duration

    if 1.5 <= words_per_second <= 3:
        return 1.0

    elif (
        1.0 <= words_per_second < 1.5
        or
        3.0 < words_per_second <= 4.0
    ):
        return 0.7

    return 0.4


# ==========================================================
# CONFIDENCE CALCULATOR
# ==========================================================

def calculate_confidence(text, duration):
    word_count = len(text.split())

    repeat = repeated_word_score(text)
    hesitation = hesitation_score(text)
    uncertainty = uncertainty_score(text)
    pause = pause_score(duration, word_count)

    confidence = (
        repeat * 0.25 +
        hesitation * 0.25 +
        uncertainty * 0.25 +
        pause * 0.25
    )

    return {
        "confidence_score": round(confidence * 100, 2),
        "signals": {
            "repeat": round(repeat, 2),
            "hesitation": round(hesitation, 2),
            "uncertainty": round(uncertainty, 2),
            "pause": round(pause, 2)
        }
    }