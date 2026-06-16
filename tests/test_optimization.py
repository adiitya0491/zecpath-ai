from parsers.skill_extractor import detect_skills

def test_skill_detection():

    text = """
    AWS Kubernetes Docker Terraform Python
    """

    skills = detect_skills(text)

    assert len(skills) > 0

    print("Optimization test passed")