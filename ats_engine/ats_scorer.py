from scoring.score_normalizer import normalize_score

def calculate_ats_score(candidate_skills: list, required_skills: list) -> float:
    """
    Calculates the ATS match score between candidate skills and job requirements.

    Args:
        candidate_skills (list): Skills extracted from candidate resume.
        required_skills (list): Skills required for the job role.

    Returns:
        float: ATS score percentage (0 to 100).
    """

    matched = set(candidate_skills).intersection(set(required_skills))
    score = (len(matched) / len(required_skills)) * 100

    return score
