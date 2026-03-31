from sentence_transformers import SentenceTransformer, util
import json

with open("data/skill_synonyms.json") as f:
    SKILL_SYNONYMS = json.load(f)

def normalize_skill(skill):

    skill = skill.lower()

    if skill in SKILL_SYNONYMS:
        return SKILL_SYNONYMS[skill]

    return skill

model = SentenceTransformer("all-MiniLM-L6-v2")


def get_resume_text(sectioned_resume: dict):

    parts = []

    # -------- SKILLS --------
    for skill in sectioned_resume.get("skills", []):
        if isinstance(skill, str):
            parts.append(skill)

    # -------- EXPERIENCE --------
    for exp in sectioned_resume.get("experience", []):
        if isinstance(exp, dict):
            role = exp.get("role", "")
            parts.append(role)

    # -------- PROJECTS --------
    for proj in sectioned_resume.get("projects", []):
        if isinstance(proj, dict):
            title = proj.get("title", "")
            parts.append(title)

    # -------- EDUCATION --------
    for edu in sectioned_resume.get("education", []):
        if isinstance(edu, dict):
            degree = edu.get("degree_or_institute", "")
            parts.append(degree)

    # -------- CERTIFICATIONS --------
    for cert in sectioned_resume.get("certifications", []):
        if isinstance(cert, dict):
            title = cert.get("title", "")
            parts.append(title)

    return " ".join(parts)


def compute_similarity(resume_text, jd_text):

    emb1 = model.encode(resume_text, convert_to_tensor=True)
    emb2 = model.encode(jd_text, convert_to_tensor=True)

    score = util.cos_sim(emb1, emb2).item()

    return round(score, 3)


def semantic_match(sectioned_resume, jd_text):

    resume_text = get_resume_text(sectioned_resume)

    similarity = compute_similarity(resume_text, jd_text)

    return {
        "similarity_score": similarity,
        "match": similarity > 0.6
    }