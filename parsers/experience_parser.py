import re
from datetime import datetime


# =========================================================
# EDUCATION FILTER
# =========================================================

EDUCATION_KEYWORDS = [
    "bachelor",
    "master",
    "degree",
    "university",
    "college",
    "b.sc",
    "m.sc",
    "btech",
    "mtech",
    "phd"
]


# =========================================================
# DATE PARSER
# =========================================================

def parse_date(date_str):

    if not date_str or not isinstance(date_str, str):
        return None

    date_str = date_str.strip()

    if "present" in date_str.lower():
        return datetime.now()

    formats = [
        "%m/%Y",
        "%b %Y",
        "%B %Y",
        "%Y"
    ]

    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except:
            continue

    return None


# =========================================================
# NORMALIZE ROLES (Structured Input)
# =========================================================

def normalize_roles(experience_list):

    roles = []

    if not isinstance(experience_list, list):
        return roles

    for item in experience_list:

        if not isinstance(item, dict):
            continue

        role_title = item.get("role") or item.get("role_title")

        if not role_title or not isinstance(role_title, str):
            continue

        role_lower = role_title.lower()

        # 🚫 Skip education entries
        if any(word in role_lower for word in EDUCATION_KEYWORDS):
            continue

        start_str = item.get("start_date")
        end_str = item.get("end_date")

        start_date = parse_date(start_str)
        end_date = parse_date(end_str)

        if start_date and end_date:
            months = (end_date.year - start_date.year) * 12 + \
                     (end_date.month - start_date.month)

            # Prevent negative durations
            if months < 0:
                months = 0
        else:
            months = 0

        roles.append({
            "role": role_title.strip(),
            "start_date": start_str,
            "end_date": end_str,
            "duration_months": months,
            "duration_years": round(months / 12, 2)
        })

    return roles


# =========================================================
# TOTAL EXPERIENCE
# =========================================================

def calculate_total_experience(roles):

    total_months = sum(r.get("duration_months", 0) for r in roles)

    return {
        "total_experience_months": total_months,
        "total_experience_years": round(total_months / 12, 2)
    }


# =========================================================
# ROLE KEYWORDS
# =========================================================

ROLE_KEYWORDS = {
    "cloud engineer": [
        "cloud", "aws", "azure", "gcp",
        "devops", "platform", "sre",
        "infrastructure"
    ]
}


# =========================================================
# RELEVANCE SCORE
# =========================================================

def relevance_score(roles, target_role):

    if not target_role:
        return 0

    keywords = ROLE_KEYWORDS.get(target_role.lower(), [])

    if not roles or not keywords:
        return 0

    score = 0

    for r in roles:

        role_text = r.get("role")

        if not role_text:
            continue

        role_text = role_text.lower()

        if any(keyword in role_text for keyword in keywords):
            score += 1

    return round(score / len(roles), 2)


# =========================================================
# MAIN PARSER
# =========================================================

def parse_experience(sectioned_resume, target_role="cloud engineer"):

    if not isinstance(sectioned_resume, dict):
        return {
            "total_experience_months": 0,
            "total_experience_years": 0.0,
            "roles": [],
            "relevance_score": 0
        }

    experience_data = sectioned_resume.get("experience", [])

    roles = normalize_roles(experience_data)

    total_exp = calculate_total_experience(roles)

    rel_score = relevance_score(roles, target_role)

    return {
        **total_exp,
        "roles": roles,
        "relevance_score": rel_score
    }