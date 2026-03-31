from parsers.jd_parser import parse_job_description


def test_jd_parser():
    sample_jd = """
    We are hiring a Data Analyst.
    Required skills: SQL, Python, Power BI.
    Experience: 2+ years.
    Education: Bachelor's degree preferred.
    """

    parsed = parse_job_description(sample_jd)

    assert parsed["job_title"] == "Data Analyst"
    assert "python" in parsed["required_skills"]
    assert "sql" in parsed["required_skills"]
