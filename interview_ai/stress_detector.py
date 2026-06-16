# ==========================================================
# STRESS PATTERNS
# ==========================================================

STRESS_PATTERNS = [
    "not sure",
    "sorry",
    "i guess",
    "maybe",
    "probably",
    "nervous",
    "confused"
]


# ==========================================================
# STRESS SCORING
# ==========================================================

def stress_score(text):
    text = text.lower()

    count = sum(
        pattern in text
        for pattern in STRESS_PATTERNS
    )

    if count == 0:
        return 1.0

    elif count == 1:
        return 0.7

    else:
        return 0.4