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

    # Pattern:
    # We are hiring a Data Analyst.
    match = re.search(
        r"we\s+are\s+hiring\s+(?:a|an)\s+(.+?)\.?$",
        text.split("\n")[0],
        re.IGNORECASE
    )

    if match:
        return match.group(1).strip()

    # Fallback to first meaningful line
    lines = text.split("\n")

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

    match = re.search(
        r"required skills\s*:(.*?)(experience|education|qualification|$)",
        text,
        re.IGNORECASE | re.DOTALL
    )

    if not match:
        return []

    section = match.group(1)

    skills = []

    for skill in re.split(r",|\n", section):

        skill = skill.strip().lower()

        if len(skill) > 1:
            skills.append(skill)

    return skills

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