import re
from datetime import datetime

EDUCATION_WORDS = {"bachelor","master","degree","university",
                   "college","b.sc","btech","mtech","phd","b.e"}

ROLE_KEYWORDS = {
    "cloud engineer":    ["cloud","aws","azure","gcp","devops","platform","sre","infrastructure"],
    "devops engineer":   ["devops","ci/cd","docker","kubernetes","pipeline","automation"],
    "software engineer": ["software","developer","backend","frontend","fullstack"],
    "data engineer":     ["data","etl","pipeline","spark","bigquery"],
}

def _parse_date(s):
    if not s: return None
    s = s.strip()
    if s.lower() in ("present","now","current"): return datetime.now()
    for fmt in ("%m/%Y","%Y","%b %Y","%B %Y"):
        try: return datetime.strptime(s, fmt)
        except: pass
    return None

def _months(s1, s2):
    a, b = _parse_date(s1), _parse_date(s2)
    if not a or not b: return 0
    return max(0, (b.year-a.year)*12+(b.month-a.month))

def _is_relevant(role_text, target_role):
    keywords = ROLE_KEYWORDS.get(target_role.lower(), [])
    rt = role_text.lower()
    return any(k in rt for k in keywords)

def parse_experience(sectioned_resume: dict, target_role: str = "cloud engineer") -> dict:

    """
    Input:  dict from classify_sections()
    Output: {"jobs": [...], "total_months": N, "total_years": N}
    Each job: {role, company, duration_months, is_relevant}
    """
    if not isinstance(sectioned_resume, dict):
        return {"jobs": [], "total_months": 0, "total_years": 0.0}

    exp_list = sectioned_resume.get("experience", [])
    jobs = []

    for item in exp_list:
        if not isinstance(item, dict): continue
        role = (item.get("role") or "").strip()
        if any(w in role.lower() for w in EDUCATION_WORDS): continue

        months = _months(item.get("start_date"), item.get("end_date"))
        # Try to extract company from role string "Role @ Company" or "Role - Company"
        company = ""
        for sep in (" @ ", " at ", " - ", " | "):
            if sep in role:
                parts = role.split(sep, 1)
                role, company = parts[0].strip(), parts[1].strip()
                break

        jobs.append({
            "role":             role,
            "company":          company,
            "start_date":       item.get("start_date"),
            "end_date":         item.get("end_date"),
            "duration_months":  months,
            "duration_years":   round(months/12, 2),
            "is_relevant":      _is_relevant(role, target_role),
        })

    total_months = sum(j["duration_months"] for j in jobs)
    return {
        "jobs":         jobs,
        "total_months": total_months,
        "total_years":  round(total_months/12, 2),
    }