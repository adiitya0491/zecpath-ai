import re

def mask_personal_info(text):

    text = re.sub(r'\S+@\S+', '[EMAIL]', text)
    text = re.sub(r'\+?\d[\d\s\-]{8,}', '[PHONE]', text)

    return text