# ==========================================================
# SCORE NORMALIZATION
# ==========================================================

def normalize_score(score, min_val=0, max_val=100):

    if score < min_val:
        score = min_val

    if score > max_val:
        score = max_val

    normalized = (
        (score - min_val)
        / (max_val - min_val)
    ) * 100

    return round(normalized, 2)