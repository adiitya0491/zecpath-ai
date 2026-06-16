import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from screening_ai.scoring_engine import (
    screening_scoring_pipeline
)

sample_answers = [

    {
        "question_id": "Q1",

        "original_text":
        "I am a Python developer with 2 years experience",

        "intent":
        "introduction",

        "skills":
        ["python"],

        "experience_years":
        2,

        "availability":
        "Immediate",

        "off_topic":
        False,

        "is_vague":
        False
    },

    {
        "question_id": "Q2",

        "original_text":
        "I have worked on Django and REST APIs",

        "intent":
        "experience",

        "skills":
        ["django"],

        "experience_years":
        2,

        "availability":
        "Immediate",

        "off_topic":
        False,

        "is_vague":
        False
    }
]

intent_map = {

    "Q1": "introduction",

    "Q2": "experience"
}


def simulate_test():

    result = screening_scoring_pipeline(
        sample_answers,
        intent_map
    )

    return result


if __name__ == "__main__":

    print(simulate_test())