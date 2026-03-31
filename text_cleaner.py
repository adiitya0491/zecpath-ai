import re


def clean_resume_text(text: str) -> str:

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # Remove powered by junk
    text = re.sub(r"powered by.*", "", text, flags=re.IGNORECASE)

    # Normalize bullet points
    text = text.replace("•", "\n")
    text = text.replace("▪", "\n")
    text = text.replace("●", "\n")

    # Remove multiple spaces
    text = re.sub(r"[ \t]+", " ", text)

    # Remove excessive newlines
    text = re.sub(r"\n+", "\n", text)

    return text.strip()