import re 

def speech_to_text(audio_input):

    return {
        "text": audio_input,
        "confidence": 0.92
    }

FILLER_WORDS = [
    "um",
    "uh",
    "like",
    "you know",
    "hmm"
]

def remove_fillers(text):

    for word in FILLER_WORDS:

        text = re.sub(
            rf"\b{word}\b",
            "",
            text,
            flags=re.IGNORECASE
        )

    return text

def fix_punctuation(text):

    text = text.strip()

    if text:
        text = (
            text[0].upper()
            + text[1:]
        )

    if not text.endswith(
        (".", "!", "?")
    ):
        text += "."

    return text

def normalize_text(text):

    text = text.lower()

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()

def handle_interruptions(text):

    text = re.sub(
        r"(.)\1{2,}",
        r"\1",
        text
    )

    return text

def detect_silence(text):

    if not text:

        return True

    if len(text.strip()) < 2:

        return True

    return False

def clean_transcript(audio_input):

    stt_result = speech_to_text(
        audio_input
    )

    raw_text = stt_result["text"]

    confidence = stt_result[
        "confidence"
    ]

    if detect_silence(raw_text):

        return {
            "clean_text":"",
            "confidence":confidence,
            "status":"silence_detected"
        }

    text = remove_fillers(raw_text)

    text = handle_interruptions(text)

    text = normalize_text(text)

    text = fix_punctuation(text)

    return {
        "clean_text":text,
        "confidence":confidence,
        "status":"processed"
    }

