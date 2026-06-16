import re
from functools import lru_cache

@lru_cache(maxsize=1000)
def clean_text_cached(text):
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()