"""
Transcript Cleanup Optimizer
Zecpath AI - Day 42
"""

import re


def advanced_clean(text):
    """
    Advanced transcript cleanup.
    """

    text = text.lower()

    # Remove filler words
    text = re.sub(
        r"\b(um|uh|hmm|like|you know)\b",
        "",
        text
    )

    # Remove repeated words
    text = re.sub(
        r"\b(\w+)( \1\b)+",
        r"\1",
        text
    )

    # Remove symbols
    text = re.sub(
        r"[^\w\s]",
        "",
        text
    )

    # Remove extra spaces
    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


def batch_process(data, func):
    """
    Faster batch processing.
    """

    return [
        func(item)
        for item in data
    ]


if __name__ == "__main__":

    sample = (
        "Um um I worked worked "
        "on Python!!!"
    )

    print(
        advanced_clean(sample)
    )