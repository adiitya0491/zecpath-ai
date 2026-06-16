"""
Day 68

Release Ready System

Zecpath AI
"""


# -------------------------------

# Safe Value Handler

# -------------------------------

def safe_value(v, default=0):

    try:

        v = float(v)

    except Exception:

        return default

    return max(

        0,

        min(v, 100)

    )


# -------------------------------

# Unified Score Validator

# -------------------------------

def validate_scores(scores):

    return {

        key: safe_value(value)

        for key, value in scores.items()

    }


# -------------------------------

# Stable Aggregation

# -------------------------------

def final_aggregate(scores):

    scores = validate_scores(scores)

    if not scores:

        return 0

    return round(

        sum(scores.values())

        /

        len(scores),

        2

    )


# -------------------------------

# Final Decision Logic

# -------------------------------

def final_decision(score):

    if score >= 80:

        return "Selected"

    elif score >= 60:

        return "Hold / Review"

    return "Rejected"


# -------------------------------

# Release Pipeline

# -------------------------------

def release_pipeline(

    candidate_id,

    scores

):

    scores = validate_scores(

        scores

    )

    final_score = final_aggregate(

        scores

    )

    decision = final_decision(

        final_score

    )

    return {

        "candidate_id": candidate_id,

        "scores": scores,

        "final_score": final_score,

        "decision": decision,

        "status": "release_ready"

    }


if __name__ == "__main__":

    sample = release_pipeline(

        "C30001",

        {

            "ats": 85,

            "hr": 80,

            "technical": 90

        }

    )

    print(sample)