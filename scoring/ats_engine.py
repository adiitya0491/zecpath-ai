from ai_engine.bias_checker import check_bias
from scoring.score_normalizer import normalize_score

def generate_candidate_score(
    skill_score,
    experience_score,
    education_score,
    certification_score,
    semantic_score
):

    # -------------------------
    # WEIGHTS
    # -------------------------
    weights = {
        "skills": 0.40,
        "experience": 0.25,
        "education": 0.10,
        "certifications": 0.05,
        "semantic": 0.20
    }

    # -------------------------
    # ATS SCORE
    # -------------------------
    ats_score = (
        skill_score * weights["skills"] +
        experience_score * weights["experience"] +
        education_score * weights["education"] +
        certification_score * weights["certifications"] +
        semantic_score * weights["semantic"]
    )

    ats_score = normalize_score(ats_score)

    bias_status = check_bias(skill_score, experience_score)

    # -------------------------
    # DECISION
    # -------------------------
    if ats_score >= 0.75:
        decision = "Strong Match"
    elif ats_score >= 0.6:
        decision = "Moderate Match"
    else:
        decision = "Weak Match"

    return {
        "skill_score": skill_score,
        "experience_score": experience_score,
        "education_score": education_score,
        "certification_score": certification_score,
        "semantic_score": semantic_score,
        "ats_score": ats_score,
        "decision": decision,
        "bias_check": bias_status
    }