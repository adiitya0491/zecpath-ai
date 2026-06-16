import re


# ==========================================================
# CONFIG
# ==========================================================

LEFT_SECTION_HEADERS = [
    "summary",
    "experience",
    "work experience",
    "professional experience",
    "education",
    "projects",
]

RIGHT_SECTION_HEADERS = [
    "strengths",
    "key achievements",
    "skills",
    "technical skills",
    "hard skills",
    "languages",
    "certifications"
]


ALL_HEADERS = LEFT_SECTION_HEADERS + RIGHT_SECTION_HEADERS


# ==========================================================
# NORMALIZATION HELPERS
# ==========================================================

def normalize_unicode(text: str) -> str:
    text = text.replace("\u00a0", " ")  # non-breaking space
    text = text.replace("\u200b", "")   # zero width
    text = text.replace("\ufeff", "")   # BOM
    text = text.replace("\x00", "")     # NULL bytes
    return text


def normalize_dashes(text: str) -> str:
    text = text.replace("–", "-")
    text = text.replace("—", "-")
    return text


def normalize_bullets(text: str) -> str:
    bullets = ["•", "▪", "●", "·", "▪", "►", "▸"]
    for b in bullets:
        text = text.replace(b, "\n")
    return text


# ==========================================================
# HEADER FIXING
# ==========================================================

def separate_section_headers(text: str) -> str:
    """
    Fix cases like:
    EXPERIENCE Ability to work well
    → EXPERIENCE
      Ability to work well
    """

    lines = text.split("\n")
    fixed = []

    for line in lines:
        stripped = line.strip()

        for header in ALL_HEADERS:
            if stripped.lower().startswith(header):
                header_len = len(header)
                header_text = stripped[:header_len]
                remainder = stripped[header_len:].strip()

                fixed.append(header_text.upper())
                if remainder:
                    fixed.append(remainder)
                break
        else:
            fixed.append(line)

    return "\n".join(fixed)


# ==========================================================
# COLUMN RECONSTRUCTION
# ==========================================================

def reconstruct_columns(text: str) -> str:
    """
    Moves right-column sections (Strengths, Skills, etc.)
    to bottom of document so Experience block stays clean.
    """

    lines = text.split("\n")

    left_content = []
    right_content = []

    current_block = "left"

    for line in lines:
        lower = line.strip().lower()

        if any(lower == h for h in RIGHT_SECTION_HEADERS):
            current_block = "right"

        elif any(lower == h for h in LEFT_SECTION_HEADERS):
            current_block = "left"

        if current_block == "right":
            right_content.append(line)
        else:
            left_content.append(line)

    return "\n".join(left_content + [""] + right_content)


# ==========================================================
# EXPERIENCE SANITY FILTER
# ==========================================================

def clean_experience_noise(text: str) -> str:
    """
    Removes soft skills mistakenly injected under EXPERIENCE.
    Keeps only lines likely related to job entries.
    """

    lines = text.split("\n")
    cleaned = []
    inside_experience = False

    date_pattern = re.compile(r"\d{1,2}/\d{4}|\d{4}")

    for line in lines:
        lower = line.strip().lower()

        if lower == "experience":
            inside_experience = True
            cleaned.append(line)
            continue

        if inside_experience:
            # Stop if new section starts
            if any(lower == h for h in ALL_HEADERS if h != "experience"):
                inside_experience = False
                cleaned.append(line)
                continue

            # Keep only lines with date or role keywords
            if date_pattern.search(line) or any(
                word in lower for word in
                ["engineer", "developer", "manager", "analyst", "consultant", "architect"]
            ):
                cleaned.append(line)

            continue

        cleaned.append(line)

    return "\n".join(cleaned)


# ==========================================================
# MAIN CLEAN FUNCTION
# ==========================================================

def clean_resume_text(text: str) -> str:

    if not isinstance(text, str):
        text = str(text)

    # Basic normalization
    text = normalize_unicode(text)
    text = normalize_dashes(text)
    text = normalize_bullets(text)

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # Remove junk footer lines
    text = re.sub(r"powered by.*", "", text, flags=re.IGNORECASE)

    # Fix section collisions
    text = separate_section_headers(text)

    # Fix spacing around dates
    text = re.sub(r"\s*-\s*", " - ", text)

    # Remove extra spaces
    text = re.sub(r"[ \t]+", " ", text)

    # Remove excessive newlines
    text = re.sub(r"\n+", "\n", text)

    # Reconstruct columns
    text = reconstruct_columns(text)

    # Clean noise inside EXPERIENCE
    text = clean_experience_noise(text)

    # Final newline cleanup
    text = re.sub(r"\n+", "\n", text)

    # Remove junk symbols
    text = re.sub(r"[@#%^&*+=<>|~]", "", text)

    return text.strip()

# ==========================================================
# BACKWARD COMPATIBILITY
# ==========================================================


def clean_text(text):
    """
    Legacy wrapper used by tests.
    """

    cleaned = clean_resume_text(text)

    # Remove special symbols
    cleaned = re.sub(r"[@#$%^&*+=<>|~`]", "", cleaned)

    return cleaned

# ==========================================
# Compatibility Alias For Tests
# ==========================================

def clean_text(text):
    return clean_resume_text(text)