from typing import Union


def check_bias(skill_score: float, experience_score: float) -> str:
    """Used by ats_engine.py internally."""
    if skill_score > 0.9 and experience_score < 0.3:
        return "Possible keyword stuffing bias"
    if skill_score < 0.2 and experience_score > 0.8:
        return "Experienced candidate — low keyword match"
    return "No bias detected"


def detect_bias_flags(parsed: dict) -> list[str]:

    """
    Called by API routes.
    Input:  parsed resume dict
    Output: list of flag strings (empty = clean)
    """
    flags = []
    skills  = parsed.get("skills", [])
    exp     = parsed.get("experience", [])
    edu     = parsed.get("education", [])

    # Flag 1: Suspiciously long skill list
    if len(skills) > 40:
        flags.append("skill_list_unusually_long")

    # Flag 2: Skills but zero experience
    if len(skills) > 10 and len(exp) == 0:
        flags.append("skills_without_experience")

    # Flag 3: No education detected
    if len(edu) == 0:
        flags.append("no_education_detected")

    # Flag 4: Very short resume
    if parsed.get("raw_text_length", 9999) < 200:
        flags.append("resume_text_too_short")

    return flags