import re


def parse_education(data: dict):

    education_lines = data.get("education", [])
    results = []

    for line in education_lines:

        # -------- HANDLE DICT OR STRING --------
        if isinstance(line, dict):
            text = line.get("degree_or_institute", "")
            start_date = line.get("start_date")
            end_date = line.get("end_date")
        else:
            text = str(line)
            start_date = None
            end_date = None

        text = text.lower().strip()

        # skip headings
        if text in ["education", "academic background"]:
            continue

        # -------- DEGREE ----------
        degree = None
        if "b tech" in text or "b.tech" in text or "b.e" in text:
            degree = "B.TECH"
        elif "m tech" in text:
            degree = "M.TECH"
        elif "bachelor" in text:
            degree = "BACHELOR"
        elif "master" in text:
            degree = "MASTER"
        elif "phd" in text:
            degree = "PHD"

        # -------- YEARS ----------
        year = None

        if start_date and end_date:
            year = f"{start_date} - {end_date}"
        else:
            years = re.findall(r"(?:19|20)\d{2}", text)
            if len(years) >= 2:
                year = f"{years[0]} - {years[1]}"
            elif len(years) == 1:
                year = years[0]

        # -------- FIELD ----------
        field = None
        field_match = re.search(
            r"(artificial intelligence.*?science|computer science|data science|information technology|electronics)",
            text,
            re.I,
        )
        if field_match:
            field = field_match.group(0).strip()

        # -------- INSTITUTION ----------
        institution = None
        inst_match = re.search(
            r"(college|university|institute).*",
            text,
            re.I
        )
        if inst_match:
            institution = inst_match.group(0).strip()

        results.append({
            "degree": degree,
            "field": field,
            "institution": institution,
            "year": year
        })

    return results


def build_academic_profile(data: dict):

    return {
        "education": parse_education(data)
    }