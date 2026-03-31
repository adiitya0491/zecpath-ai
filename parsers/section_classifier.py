import re
from datetime import datetime

# ===============================
# DATE REGEX
# ===============================

DATE_REGEX = re.compile(
    r"(?P<start>(\d{2}/\d{4}|\d{4}|[A-Za-z]+\s\d{4}))\s*-\s*(?P<end>(Present|present|\d{2}/\d{4}|\d{4}|[A-Za-z]+\s\d{4}))"
)

# ===============================
# HELPERS
# ===============================

def parse_date(date_str):
    if not date_str:
        return None

    date_str = date_str.strip()

    if "present" in date_str.lower():
        return datetime.now()

    for fmt in ("%m/%Y", "%Y", "%b %Y", "%B %Y"):
        try:
            return datetime.strptime(date_str, fmt)
        except:
            continue
    return None


def calculate_duration(start_str, end_str):
    start = parse_date(start_str)
    end = parse_date(end_str)

    if not start or not end:
        return 0

    months = (end.year - start.year) * 12 + (end.month - start.month)
    return round(months / 12, 2)


# ===============================
# STRICT SKILL FILTER
# ===============================
def extract_clean_skills(line):

    skills = []

    parts = re.split(r"[,\|/•\-]", line)

    BLOCK_WORDS = {
        "languages",
        "language",
        "hard skills",
        "soft skills",
        "skills",
        "interests",
        "hobbies",
        "awards",
        "achievements",
        "certifications",
        "projects",
        "education"
    }

    for p in parts:

        skill = p.strip()

        skill = re.sub(r"[^A-Za-z0-9+#. ]", "", skill)

        if not skill:
            continue

        lower = skill.lower()

        # Remove section labels
        if lower in BLOCK_WORDS:
            continue

        # Skip sentences
        if len(skill.split()) > 3:
            continue

        # Skip numbers
        if re.search(r"\d{4}", skill):
            continue

        # Skip location words
        if lower in ["city", "country"]:
            continue

        # Skip language combinations
        if lower in ["english", "spanish", "malayalam", "native", "advanced"]:
            continue

        # Skip verbs
        if lower.endswith("ing"):
            continue

        if len(skill) < 2:
            continue

        skills.append(skill)

    return skills


# ===============================
# MAIN CLASSIFIER
# ===============================

def classify_sections(resume_text: str):

    lines = resume_text.split("\n")

    skills = []
    experience = []
    education = []
    projects = []
    certifications = []

    current_section = None

    for line in lines:
        clean = line.strip()

        if not clean:
            continue

        lower = clean.lower()

        # -------------------------
        # SECTION DETECTION
        # -------------------------
        if lower in ["skills", "technical skills"]:
            current_section = "skills"
            continue

        if lower in ["experience", "work experience", "professional experience"]:
            current_section = "experience"
            continue

        if lower in ["education"]:
            current_section = "education"
            continue

        if lower in ["projects"]:
            current_section = "projects"
            continue

        if lower in ["certifications", "certificates"]:
            current_section = "certifications"
            continue

        if lower in ["languages", "language"]:
            current_section = "languages"
            continue
        # -------------------------
        # SKILLS
        # -------------------------
        if current_section == "skills":
            if clean.lower() in ["languages", "hard skills", "soft skills"]:
                continue

            skill_words = extract_clean_skills(clean)
            skills.extend(skill_words)
            continue

        # -------------------------
        # EXPERIENCE
        # -------------------------
        if current_section == "experience":

            match = DATE_REGEX.search(clean)

            if match:
                start_str = match.group("start")
                end_str = match.group("end")

                role_title = ""

                # Case 1: role and date on same line
                role_part = clean[:match.start()].strip(" -")
                if role_part:
                    role_title = role_part

                # Case 2: role is previous line
                else:
                    idx = lines.index(line)
                    if idx > 0:
                        prev_line = lines[idx - 1].strip()

                        # Avoid picking section headers
                        if prev_line.lower() not in [
                            "experience",
                            "work experience",
                            "professional experience"
                        ]:
                            role_title = prev_line

                duration = calculate_duration(start_str, end_str)

                experience.append({
                    "role": role_title,
                    "start_date": start_str,
                    "end_date": end_str,
                    "duration_years": duration
                })

            continue

        # -------------------------
        # EDUCATION
        # -------------------------
        if current_section == "education":

            match = DATE_REGEX.search(clean)

            if match:
                start_str = match.group("start")
                end_str = match.group("end")

                degree_part = clean[:match.start()].strip(" -")

                education.append({
                    "degree_or_institute": degree_part,
                    "start_date": start_str,
                    "end_date": end_str
                })

            continue

        # -------------------------
        # PROJECTS
        # -------------------------
        if current_section == "projects":

            match = DATE_REGEX.search(clean)

            if match:
                start_str = match.group("start")
                end_str = match.group("end")

                title = clean[:match.start()].strip(" -")

                projects.append({
                    "title": title,
                    "start_date": start_str,
                    "end_date": end_str
                })

            continue

        # -------------------------
        # CERTIFICATIONS
        # -------------------------
        if current_section == "certifications":

            lower = clean.lower()

            # Skip providers
            if any(word in lower for word in [
                "academy",
                "institute",
                "training",
                "coursera",
                "udemy",
                "officemaster"
            ]):
                continue

            # Skip long description sentences
            if len(clean.split()) > 7:
                continue

            # Skip sentence-like lines
            if clean.endswith("."):
                continue

            match = DATE_REGEX.search(clean)

            if match:
                start_str = match.group("start")
                end_str = match.group("end")

                title = clean[:match.start()].strip(" -")

                certifications.append({
                    "title": title,
                    "start_date": start_str,
                    "end_date": end_str
                })

            else:
                # capture certificate without dates
                certifications.append({
                    "title": clean,
                    "start_date": None,
                    "end_date": None
                })

            continue

    # Remove duplicate skills
    skills = sorted(list(set(skills)))

    return {
        "skills": skills,
        "experience": experience,
        "education": education,
        "projects": projects,
        "certifications": certifications
    }