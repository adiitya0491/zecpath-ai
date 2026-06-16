import re

INTENT_MAP = {

    "introduction":[
        "introduce",
        "about myself",
        "background"
    ],

    "experience":[
        "experience",
        "years",
        "worked",
        "role"
    ],

    "skills":[
        "skills",
        "technologies",
        "tools"
    ],

    "salary":[
        "salary",
        "ctc",
        "pay",
        "lpa"
    ],

    "availability":[
        "notice period",
        "available",
        "join",
        "immediate"
    ]
}

def classify_intent(text):

    text_lower = text.lower()

    for intent, keywords in INTENT_MAP.items():

        for keyword in keywords:

            if keyword in text_lower:
                return intent

    return "unknown"

SKILL_DB = [

    "python",
    "java",
    "aws",
    "docker",
    "kubernetes",
    "terraform",
    "react",
    "sql"
]

def extract_skills(text):

    text = text.lower()

    return [

        skill

        for skill in SKILL_DB

        if skill in text
    ]

def extract_experience(text):

    match = re.search(
        r"(\d+)\s*(years|year)",
        text.lower()
    )

    if match:
        return int(match.group(1))

    return 0

def extract_salary(text):

    match = re.search(
        r"(\d+)\s*(lpa|lakhs|k)",
        text.lower()
    )

    if match:
        return match.group(0)

    return None

def extract_availability(text):

    text = text.lower()

    if "immediate" in text:
        return "Immediate"

    elif "notice" in text:
        return "Notice Period"

    return "Unknown"

def is_off_topic(intent):

    return intent == "unknown"

def is_vague(text):

    vague_words = [

        "maybe",

        "not sure",

        "don't know",

        "possibly"
    ]

    return any(
        word in text.lower()
        for word in vague_words
    )

def detect_missing_answer(text):

    return (
        not text
        or len(text.strip()) < 3
    )

def process_answer(
    question_id,
    answer_text
):

    intent = classify_intent(
        answer_text
    )

    structured = {

        "question_id":
        question_id,

        "original_text":
        answer_text,

        "intent":
        intent,

        "skills":
        extract_skills(
            answer_text
        ),

        "experience_years":
        extract_experience(
            answer_text
        ),

        "salary":
        extract_salary(
            answer_text
        ),

        "availability":
        extract_availability(
            answer_text
        ),

        "off_topic":
        is_off_topic(
            intent
        ),

        "is_vague":
        is_vague(
            answer_text
        ),

        "missing_answer":
        detect_missing_answer(
            answer_text
        )
    }

    return structured

def process_answers_batch(
    answers
):

    results = []

    for ans in answers:

        result = process_answer(
            ans["question_id"],
            ans["text"]
        )

        results.append(result)

    return results