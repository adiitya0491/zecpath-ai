from screening_ai.stt_processor import (
    clean_transcript
)

def test_cleaning():

    text = (
        "um i am a cloud engineer"
    )

    result = clean_transcript(
        text
    )

    assert (
        "um"
        not in result["clean_text"]
    )

    assert (
        result["clean_text"]
        .startswith("I")
    )