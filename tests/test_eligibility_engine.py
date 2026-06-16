from screening_ai.eligibility_engine import evaluate_candidate


def test_eligible_candidate():

    candidate = {
        "candidate_id": "C001",
        "final_score": 85,
        "skills": ["aws", "docker", "terraform"],
        "total_experience": 4,
        "location": "Remote",
        "available": True
    }

    rules = {
        "min_ats_score": 70,
        "mandatory_skills": ["aws", "docker"],
        "min_experience": 2,
        "max_experience": 8,
        "allowed_locations": ["Remote"],
        "availability_required": True
    }

    result = evaluate_candidate(candidate, rules)

    assert result["eligibility_status"] == "Eligible"


def test_review_candidate():

    candidate = {
        "candidate_id": "C002",
        "final_score": 60,
        "skills": ["aws"],
        "total_experience": 3,
        "location": "Remote",
        "available": True
    }

    rules = {
        "min_ats_score": 70,
        "mandatory_skills": ["aws"],
        "min_experience": 2,
        "max_experience": 8,
        "allowed_locations": ["Remote"],
        "availability_required": True
    }

    result = evaluate_candidate(candidate, rules)

    assert result["eligibility_status"] == "Review"


def test_rejected_candidate():

    candidate = {
        "candidate_id": "C003",
        "final_score": 40,
        "skills": ["html"],
        "total_experience": 1,
        "location": "Delhi",
        "available": False
    }

    rules = {
        "min_ats_score": 70,
        "mandatory_skills": ["aws"],
        "min_experience": 2,
        "max_experience": 8,
        "allowed_locations": ["Remote"],
        "availability_required": True
    }

    result = evaluate_candidate(candidate, rules)

    assert result["eligibility_status"] == "Rejected"