import re

def detect_category(text: str):
    text = text.lower()

    if "power bi" in text or "data" in text or "analytics" in text:
        return "Data Analytics"
    if "aws" in text or "cloud" in text:
        return "Cloud"
    if "python" in text or "ai" in text or "machine learning" in text:
        return "AI/ML"
    if "web" in text or "javascript" in text:
        return "Web Development"

    return "Other"


def parse_certifications(data: dict):
    cert_lines = data.get("certifications", [])
    results = []

    for line in cert_lines:

        # -------- HANDLE DICT INPUT ----------
        if isinstance(line, dict):
            text = line.get("title") or line.get("name") or ""
        else:
            text = line

        if not isinstance(text, str):
            continue

        text = text.strip()

        # -------- YEAR ----------
        year_match = re.search(r"(19|20)\d{2}", text)
        year = year_match.group(0) if year_match else None

        # -------- NAME ----------
        name = re.sub(r"(19|20)\d{2}", "", text).strip(" ,-")

        # -------- CATEGORY ----------
        category = detect_category(text)

        results.append({
            "name": name,
            "year": year,
            "category": category
        })

    return results


def build_academic_profile(data: dict):
    return {
        "certifications": parse_certifications(data)
    }