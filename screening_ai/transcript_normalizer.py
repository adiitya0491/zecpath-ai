import re

def normalize_transcript(text):

    text = text.lower()

    fillers = [
        "um",
        "uh",
        "like",
        "you know"
    ]

    for filler in fillers:

        text = re.sub(
            rf"\b{filler}\b",
            "",
            text
        )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()

def process_transcript(raw_answers):

    processed = []

    for ans in raw_answers:

        normalized = normalize_transcript(
            ans["text"]
        )

        processed.append({

            "question_id":
            ans["question_id"],

            "answer_text":
            normalized,

            "confidence_score":
            ans.get(
                "confidence",
                0.9
            )
        })

    return processed