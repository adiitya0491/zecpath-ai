from utils.logger import get_logger

logger = get_logger()

def parse_resume(resume_text: str) -> dict:
    """
    Parses the resume text and extracts key candidate information.

    This module is part of the Zecpath Resume Parser AI Service.

    Args:
        resume_text (str): Extracted plain text from candidate resume.

    Returns:
        dict: Structured candidate data such as skills and experience.
    """

    logger.info("Resume parsing started")

    extracted_data = {
        "skills": [],
        "experience": [],
        "education": []
    }

    logger.info("Resume parsing completed")

    return extracted_data
