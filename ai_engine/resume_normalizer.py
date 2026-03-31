def normalize_resume(resume_data):

    normalized = {}

    normalized["skills"] = resume_data.get("skills", [])
    normalized["experience"] = resume_data.get("experience", [])
    normalized["education"] = resume_data.get("education", [])
    normalized["projects"] = resume_data.get("projects", [])
    normalized["certifications"] = resume_data.get("certifications", [])

    return normalized