import re
from datetime import datetime
from difflib import SequenceMatcher

DATE_REGEX = re.compile(
    r"(?P<start>(\d{1,2}/\d{4}|\d{4}|[A-Za-z]+\s\d{4}))\s*[-–—]\s*"
    r"(?P<end>(Present|present|Now|now|\d{1,2}/\d{4}|\d{4}|[A-Za-z]+\s\d{4}))"
)

# All known heading aliases — add more as you encounter them
SECTION_ALIASES = {
    "skills": [
        "skills","technical skills","core competencies","technologies",
        "tools","tech stack","expertise","key skills","competencies",
        "hard skills","proficiencies","technical expertise","strengths",
    ],
    "experience": [
        "experience","work experience","professional experience",
        "employment","career","work history","professional background",
        "professional journey","positions held","employment history",
    ],
    "education": [
        "education","academic background","qualifications",
        "academic history","degrees","studies","academic qualifications",
    ],
    "projects": [
        "projects","personal projects","side projects",
        "portfolio","key projects","notable projects",
    ],
    "certifications": [
        "certifications","certificates","accreditations",
        "credentials","licenses","achievements","awards",
    ],
    "summary": [
        "summary","profile","objective","about","about me",
        "overview","professional summary","career objective",
        "professional profile",
    ],
}


def _sim(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def _match_heading(line: str) -> str | None:

    """Match ANY heading variation with fuzzy logic. Returns section name or None."""
    clean = line.strip().lower()
    # Remove trailing colons e.g. "SKILLS:"
    clean = clean.rstrip(":")

    for section, aliases in SECTION_ALIASES.items():
        for alias in aliases:
            if clean == alias:
                return section
            if _sim(clean, alias) >= 0.82:
                return section
    return None


def _is_heading(line: str) -> bool:
    s = line.strip()
    if not s: return False
    words = s.split()
    return (
        len(words) <= 5 and
        (s.isupper() or s.istitle() or _match_heading(s) is not None)
    )


def parse_date(s):
    if not s: return None
    s = s.strip()
    if s.lower() in ("present", "now", "current"):
        return datetime.now()
    for fmt in ("%m/%Y","%Y","%b %Y","%B %Y"):
        try: return datetime.strptime(s, fmt)
        except: pass
    return None


def calc_duration(s1, s2):
    a, b = parse_date(s1), parse_date(s2)
    if not a or not b: return 0
    return max(0, (b.year - a.year)*12 + (b.month - a.month))


def extract_clean_skills(line):
    JUNK = {
        "languages","language","hard skills","soft skills","skills",
        "interests","hobbies","awards","certifications","english",
        "spanish","native","advanced","city","country","fluent",
    }
    out = []
    for p in re.split(r"[,|/•\-]", line):
        s = re.sub(r"[^A-Za-z0-9+#. ]", "", p).strip()
        if not s or s.lower() in JUNK: continue
        if len(s.split()) > 4: continue
        if re.search(r"\d{4}", s): continue
        if s.lower().endswith("ing") and len(s) > 8: continue
        if len(s) >= 2: out.append(s)
    return out


def classify_sections(resume_text: str) -> dict:

    """
    Split resume into labelled sections.
    Returns dict with keys: skills, experience, education,
    projects, certifications, summary, name, email, phone
    """
    lines = resume_text.split("\n")
    buckets = {k: [] for k in SECTION_ALIASES}
    buckets["other"] = []
    current = "other"

    # Extract contact info from first 10 lines
    email = phone = name = None
    for line in lines[:10]:
        em = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", line)
        ph = re.search(r"\+?[\d\s\-\(\)]{9,15}", line)
        if em and not email: email = em.group(0)
        if ph and not phone: phone = ph.group(0).strip()
        if not em and not ph and not name and 2 <= len(line.split()) <= 4:
            if line.strip() and line.strip()[0].isupper():
                name = line.strip()

    for line in lines:
        stripped = line.strip()
        if not stripped: continue

        matched = _match_heading(stripped)
        if matched and _is_heading(stripped):
            current = matched
            continue

        if current == "skills":
            buckets["skills"].extend(extract_clean_skills(stripped))
        elif current == "experience":
            m = DATE_REGEX.search(stripped)
            if m:
                role = stripped[:m.start()].strip(" -–") or ""
                buckets["experience"].append({
                    "role": role,
                    "start_date": m.group("start"),
                    "end_date":   m.group("end"),
                    "duration_years": calc_duration(m.group("start"), m.group("end")) / 12,
                })
        elif current == "education":
            m = DATE_REGEX.search(stripped)
            if m:
                buckets["education"].append({
                    "degree_or_institute": stripped[:m.start()].strip(" -"),
                    "start_date": m.group("start"),
                    "end_date":   m.group("end"),
                })
            else:
                buckets["education"].append({"degree_or_institute": stripped})
        elif current == "certifications":
            if len(stripped.split()) <= 10 and not stripped.endswith("."):
                m = DATE_REGEX.search(stripped)
                buckets["certifications"].append({
                    "title": stripped[:m.start()].strip() if m else stripped,
                    "start_date": m.group("start") if m else None,
                    "end_date":   m.group("end")   if m else None,
                })
        elif current in ("projects", "summary"):
            buckets[current].append(stripped)
        else:
            buckets["other"].append(stripped)

    return {
        "skills":         sorted(set(buckets["skills"])),
        "experience":     buckets["experience"],
        "education":      buckets["education"],
        "projects":       buckets["projects"],
        "certifications": buckets["certifications"],
        "summary":        " ".join(buckets["summary"]),
        "name":  name,
        "email": email,
        "phone": phone,
    }