import json
import random
from pathlib import Path


QUESTION_BANK_PATH = Path(__file__).parent / "question_bank.json"


def load_question_bank():
    with open(QUESTION_BANK_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def generate_questions(role_type, experience_level):
    """
    role_type:
        technical
        non_technical

    experience_level:
        fresher
        experienced
    """

    qb = load_question_bank()

    questions = []

    # Introduction
    questions += qb["categories"]["introduction"][experience_level]

    # Career Journey
    questions += qb["categories"]["career_journey"][experience_level]

    # Common Categories
    common_categories = [
        "strengths_weaknesses",
        "teamwork",
        "career_goals",
        "availability"
    ]

    for category in common_categories:
        questions += qb["categories"][category]["common"]

    # Role-Based Questions
    questions += qb["role_based"][role_type]

    random.shuffle(questions)

    return questions[:10]


if __name__ == "__main__":

    result = generate_questions(
        role_type="technical",
        experience_level="fresher"
    )

    for q in result:
        print("-", q)