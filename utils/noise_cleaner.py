import re

def clean_noisy_resume(text):

    text = re.sub(r"\s+"," ",text)

    text = re.sub(
        r"(.)\1{3,}",
        r"\1",
        text
    )

    text = re.sub(
        r"[^a-zA-Z0-9\s\.,\-]",
        "",
        text
    )

    return text