DEFAULT_RULES = {
    "min_ats_score": 70,
    "mandatory_skills": [],
    "min_experience": 0,
    "max_experience": 20,
    "allowed_locations": [],
    "availability_required": False
}


def check_mandatory_skills(candidate_skills, required_skills):

    if not required_skills:
        return True

    candidate_skills = [s.lower() for s in candidate_skills]
    required_skills = [s.lower() for s in required_skills]

    return all(
        skill in candidate_skills
        for skill in required_skills
    )


def check_experience(exp, min_exp, max_exp):
    return min_exp <= exp <= max_exp


def check_location(location, allowed_locations):

    if not allowed_locations:
        return True

    return location.lower() in [
        l.lower()
        for l in allowed_locations
    ]


def check_availability(is_available, required):

    if not required:
        return True

    return is_available


def evaluate_candidate(candidate, rules=DEFAULT_RULES):

    ats_score = candidate.get("final_score", 0)
    skills = candidate.get("skills", [])
    experience = candidate.get("total_experience", 0)
    location = candidate.get("location", "")
    available = candidate.get("available", True)

    skill_ok = check_mandatory_skills(
        skills,
        rules["mandatory_skills"]
    )

    exp_ok = check_experience(
        experience,
        rules["min_experience"],
        rules["max_experience"]
    )

    loc_ok = check_location(
        location,
        rules["allowed_locations"]
    )

    avail_ok = check_availability(
        available,
        rules["availability_required"]
    )

    if (
        ats_score >= rules["min_ats_score"]
        and skill_ok
        and exp_ok
        and loc_ok
        and avail_ok
    ):
        status = "Eligible"

    elif ats_score >= (rules["min_ats_score"] - 15):
        status = "Review"

    else:
        status = "Rejected"

    return {
        "candidate_id": candidate.get("candidate_id"),
        "eligibility_status": status,
        "checks": {
            "ats_score": ats_score,
            "skill_match": skill_ok,
            "experience_match": exp_ok,
            "location_match": loc_ok,
            "availability_match": avail_ok
        }
    }


cloud_engineer_rules = {
    "min_ats_score": 70,
    "mandatory_skills": [
        "aws",
        "docker",
        "terraform"
    ],
    "min_experience": 2,
    "max_experience": 8,
    "allowed_locations": [
        "Remote",
        "Bangalore",
        "Chennai"
    ],
    "availability_required": True
}


candidate = {
    "candidate_id": "C001",
    "final_score": 82,
    "skills": [
        "aws",
        "docker",
        "terraform"
    ],
    "total_experience": 4,
    "location": "Remote",
    "available": True
}


result = evaluate_candidate(
    candidate,
    cloud_engineer_rules
)

print(result)