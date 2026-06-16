"""
Day 65

Final Production System

Zecpath AI
"""


# -------------------------------

# Score Normalization

# -------------------------------

def normalize_score(value):

    try:

        value = float(value)

    except Exception:

        return 0.0

    return max(

        0.0,

        min(

            value,

            100.0

        )

    )


# -------------------------------

# Consistency Smoothing

# -------------------------------

def smooth_scores(scores):

    values = [

        normalize_score(v)

        for v in scores.values()

    ]

    if not values:

        return scores

    average = (

        sum(values)

        / len(values)

    )

    smoothed = {}

    for key, value in scores.items():

        value = normalize_score(value)

        smoothed[key] = round(

            (value * 0.7)

            +

            (average * 0.3),

            2

        )

    return smoothed


# -------------------------------

# Final Decision

# -------------------------------

def final_decision(score):

    if score >= 80:

        return "Selected"

    elif score >= 60:

        return "Hold / Review"

    return "Rejected"


# -------------------------------

# Production Pipeline

# -------------------------------

def production_pipeline(

    candidate_id,

    scores

):

    scores = smooth_scores(

        scores

    )

    final_score = round(

        sum(scores.values())

        /

        len(scores),

        2

    )

    decision = final_decision(

        final_score

    )

    return {

        "candidate_id": candidate_id,

        "scores": scores,

        "final_score": final_score,

        "decision": decision,

        "status": "production_ready"

    }


if __name__ == "__main__":

    sample = production_pipeline(

        "C1001",

        {

            "ats": 90,

            "hr": 80,

            "technical": 88

        }

    )

    print(sample)