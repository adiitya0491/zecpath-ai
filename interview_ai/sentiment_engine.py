# ==========================================================
# SENTIMENT WORDS
# ==========================================================

POSITIVE_WORDS = [
    "confident",
    "strong",
    "good",
    "success",
    "successful",
    "achieved",
    "achievement",
    "improved",
    "excellent"
]

NEGATIVE_WORDS = [
    "difficult",
    "problem",
    "struggle",
    "failed",
    "fail",
    "weak",
    "issue",
    "challenge"
]


# ==========================================================
# SENTIMENT ANALYZER
# ==========================================================

def sentiment_score(text):
    text = text.lower()

    positive_count = sum(
        word in text
        for word in POSITIVE_WORDS
    )

    negative_count = sum(
        word in text
        for word in NEGATIVE_WORDS
    )

    if positive_count > negative_count:
        sentiment = "Positive"
        score = min(positive_count / 5, 1.0)

    elif negative_count > positive_count:
        sentiment = "Negative"
        score = min(negative_count / 5, 1.0)

    else:
        sentiment = "Neutral"
        score = 0.5

    return {
        "sentiment": sentiment,
        "sentiment_score": round(score, 2)
    }