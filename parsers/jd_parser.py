import re
from typing import Dict, List


# ==========================================================
# NORMALIZE TEXT
# ==========================================================

def normalize_text(text: str) -> str:
    text = text.replace("•", "\n")
    text = text.replace("●", "\n")
    text = text.replace("▪", "\n")
    text = re.sub(r"\r", "\n", text)
    text = re.sub(r"\n+", "\n", text)
    return text.strip()


# ==========================================================
# SECTION DETECTION
# ==========================================================

def extract_section(text: str, section_names: List[str]) -> str:

    pattern = r"|".join(section_names)

    match = re.search(
        rf"({pattern})(.*?)(\n[A-Z][^\n]+|$)",
        text,
        re.IGNORECASE | re.DOTALL
    )

    if match:
        return match.group(2).strip()

    return ""


# ==========================================================
# ROLE DETECTION (FIRST LINE BASED)
# ==========================================================

def extract_role(text: str) -> str:

    lines = text.split("\n")

    # Usually first meaningful line is role
    for line in lines:
        if len(line.strip()) > 3:
            return line.strip()

    return "Unknown Role"


# ==========================================================
# EXPERIENCE EXTRACTION
# ==========================================================

def extract_experience(text: str) -> Dict:

    # Range: 2-5 years
    range_match = re.search(r"(\d+)\s*-\s*(\d+)\s*years", text, re.IGNORECASE)
    if range_match:
        return {
            "min_years": int(range_match.group(1)),
            "max_years": int(range_match.group(2))
        }

    # Plus: 3+ years
    plus_match = re.search(r"(\d+)\+?\s*years", text, re.IGNORECASE)
    if plus_match:
        return {
            "min_years": int(plus_match.group(1)),
            "max_years": None
        }

    return {"min_years": None, "max_years": None}


# ==========================================================
# GENERIC SKILL EXTRACTION ENGINE
# ==========================================================

def extract_skills(text: str) -> list:

    skills = set()

    # 1️⃣ Extract only Required Skills section
    match = re.search(
        r"required skills(.*?)(experience|qualification|$)",
        text,
        re.IGNORECASE | re.DOTALL
    )

    if not match:
        return []

    section = match.group(1)

    # 2️⃣ Split by bullet or newline
    lines = re.split(r"\n|•|-", section)

    for line in lines:
        line = line.strip().lower()

        if len(line) < 3:
            continue

        # 3️⃣ Extract bracket skills (Datadog, Cloudwatch, New Relic)
        bracket_skills = re.findall(r"\((.*?)\)", line)

        for item in bracket_skills:
            for skill in re.split(r",|/", item):
                skills.add(skill.strip().lower())

        # Remove bracket content from line
        line = re.sub(r"\(.*?\)", "", line)

        # 4️⃣ Keep meaningful multi-word phrases
        skills.add(line.strip())

    # 5️⃣ Remove noise words
    STOPWORDS = {
        "and", "or", "with", "for", "the", "of",
        "best practices", "operational"
    }

    cleaned = []

    for skill in skills:
        skill = skill.strip()

        if skill in STOPWORDS:
            continue

        if len(skill) < 3:
            continue

        cleaned.append(skill)

    return sorted(list(set(cleaned)))

# ==========================================================
# RESPONSIBILITIES
# ==========================================================

def extract_responsibilities(text: str) -> List[str]:

    section = extract_section(
        text,
        ["Responsibilities", "Key Responsibilities"]
    )

    if not section:
        return []

    lines = re.split(r"\n|\- ", section)
    lines = [line.strip() for line in lines if len(line.strip()) > 5]

    return lines


# ==========================================================
# QUALIFICATIONS
# ==========================================================

def extract_qualifications(text: str) -> str:

    if re.search(r"bachelor|b\.tech|degree", text, re.IGNORECASE):
        return "Bachelor's Degree Required"

    if re.search(r"master|m\.tech", text, re.IGNORECASE):
        return "Master's Preferred"

    return "Not Mentioned"


# ==========================================================
# MAIN PARSER
# ==========================================================

def parse_job_description(jd_text: str) -> Dict:

    clean_text = normalize_text(jd_text)

    return {
        "job_title": extract_role(clean_text),
        "key_responsibilities": extract_responsibilities(clean_text),
        "required_skills": extract_skills(clean_text),
        "experience_required": extract_experience(clean_text),
        "qualifications": extract_qualifications(clean_text),
        "raw_text": jd_text
    }