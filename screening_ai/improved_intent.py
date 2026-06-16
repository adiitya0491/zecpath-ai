# -----------------------------------
# Improved Intent Classification
# -----------------------------------

INTENT_KEYWORDS = {

    "experience": [
        "experience",
        "worked",
        "years",
        "role",
        "project",
        "developer",
        "engineer"
    ],

    "skills": [
        "skills",
        "tools",
        "technologies",
        "stack",
        "python",
        "java",
        "react",
        "django",
        "sql"
    ],

    "salary": [
        "salary",
        "ctc",
        "expected",
        "pay",
        "package",
        "lpa"
    ],

    "availability": [
        "join",
        "notice",
        "immediate",
        "available"
    ],

    "introduction": [
        "introduce",
        "background",
        "about",
        "myself"
    ]
}


def improved_intent_classification(text):

    text = text.lower()

    scores = {}

    for intent, words in INTENT_KEYWORDS.items():

        scores[intent] = sum(
            word in text
            for word in words
        )

    best_intent = max(
        scores,
        key=scores.get
    )

    if scores[best_intent] > 0:
        return best_intent

    return "unknown"