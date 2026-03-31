def check_bias(skill_score, experience_score):

    if skill_score > 0.9 and experience_score < 0.3:
        return "Possible keyword bias"

    return "No bias detected"