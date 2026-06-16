from screening_ai.transcript_normalizer import (
    normalize_transcript
)

def test_normalization():

    text = (
        "Um I have 3 years "
        "experience"
    )

    result = normalize_transcript(
        text
    )

    assert "um" not in result