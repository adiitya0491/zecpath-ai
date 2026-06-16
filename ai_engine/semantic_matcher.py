from sentence_transformers import SentenceTransformer, util
import json

_model = None

def _get_model():
    """Lazy load — model loads once, not at import time."""
    global _model
    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model


def get_semantic_score(resume_text: str, jd_text: str) -> float:

    if not resume_text or not jd_text:
        return 0.0
  
    resume_text = resume_text[:3000]
    jd_text = jd_text[:3000]

    model = _get_model()

    e1 = model.encode(
        resume_text,
        convert_to_tensor=True
    )

    e2 = model.encode(
        jd_text,
        convert_to_tensor=True
    )

    score = float(util.cos_sim(e1, e2).item())

    # Convert from -1..1 → 0..1
    score = (score + 1) / 2

    return round(score, 4)


def semantic_match(sectioned_resume: dict, jd_text: str) -> dict:
    """Legacy function — kept for existing scripts that use it."""
    parts = []
    for s in sectioned_resume.get("skills", []):
        if isinstance(s, str): parts.append(s)
    for e in sectioned_resume.get("experience", []):
        if isinstance(e, dict): parts.append(e.get("role",""))
    text = " ".join(parts)
    score = get_semantic_score(text, jd_text)
    return {"similarity_score": score, "match": score > 0.6}