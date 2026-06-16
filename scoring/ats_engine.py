from scoring.score_normalizer import normalize_score
from ai_engine.bias_checker   import check_bias
from parsers.skill_extractor   import detect_skills
from parsers.experience_parser import parse_experience
from parsers.education_parser  import parse_education
from parsers.certificate_parser import parse_certifications


def _skill_score(parsed: dict, jd_text: str) -> float:
    """Compare resume skills vs JD skills. Returns 0.0–1.0"""
    resume_skills = set(
        s["name"].lower()
        for s in parsed.get("skills", [])
        if isinstance(s, dict) and s.get("name")
    )
    jd_skills     = set(detect_skills(jd_text).keys())
    if not jd_skills: return 0.5
    overlap = resume_skills & jd_skills
    return round(len(overlap) / len(jd_skills), 3)


def _experience_score(parsed: dict, job_title: str) -> float:
    """Score based on total months and relevance. Returns 0.0–1.0"""
    exp = parse_experience(parsed, job_title)
    months   = exp.get("total_months", 0)
    relevant = sum(1 for j in exp.get("jobs", []) if j.get("is_relevant"))
    total    = len(exp.get("jobs", [])) or 1

    months_score    = min(months / 60, 1.0)   # 60 months = perfect
    relevance_score = relevant / total
    return round((months_score * 0.6) + (relevance_score * 0.4), 3)


def _education_score(parsed: dict) -> float:
    """Score based on highest degree. Returns 0.0–1.0"""
    edu = parse_education(parsed)
    degree_scores = {"PHD":1.0,"MASTER":0.85,"M.TECH":0.85,
                     "BACHELOR":0.7,"B.TECH":0.7}
    best = 0.5
    for e in edu:
        d = (e.get("degree") or "").upper()
        if d in degree_scores:
            best = max(best, degree_scores[d])
    return best


def _cert_score(parsed: dict) -> float:
    """Score based on number of certifications. Returns 0.0–1.0"""
    certs = parse_certifications(parsed)
    return min(len(certs) * 0.25, 1.0)


def calculate_ats_score(parsed: dict, jd_text: str, job_title: str, weights: dict) -> dict:

    """
    Main entry point called by API routes.
    Input:
      parsed    — dict from classify_sections() saved as JSON
      jd_text   — full job description string
      job_title — e.g. "Cloud Engineer"
      weights   — {"skill":0.30, "experience":0.25, ...}
    Output:
      {"skill_score", "experience_score", "education_score",
       "certification_score", "final_score"}  all 0–100
    """
    sk = _skill_score(parsed, jd_text)
    ex = _experience_score(parsed, job_title)
    ed = _education_score(parsed)
    ce = _cert_score(parsed)

    raw = (
        sk * weights.get("skill", 0.30) +
        ex * weights.get("experience", 0.25) +
        ed * weights.get("education", 0.20) +
        ce * weights.get("certification", 0.10)
        # semantic added by route after calling semantic_matcher
    )
    return {
        "skill_score":         normalize_score(sk),
        "experience_score":    normalize_score(ex),
        "education_score":     normalize_score(ed),
        "certification_score": normalize_score(ce),
        "final_score":         normalize_score(raw / 0.90),  # normalise to 90% (semantic adds 10%)
        "bias_check":          check_bias(sk, ex),
    }

# ==========================================================
# BACKWARD COMPATIBILITY
# ==========================================================

def generate_candidate_score(parsed, jd_text="", job_title="General"):
    """
    Compatibility wrapper for old ATS tests.
    """

    weights = {
        "skill": 0.30,
        "experience": 0.25,
        "education": 0.20,
        "certification": 0.10
    }

    return calculate_ats_score(
        parsed=parsed,
        jd_text=jd_text,
        job_title=job_title,
        weights=weights
    )