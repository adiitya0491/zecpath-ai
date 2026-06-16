from screening_ai.scoring_engine import (
    score_answer
)

def test_scoring():

    answer = {

        "question_id":"Q3",

        "original_text":
        "I have 2 years experience",

        "intent":"experience",

        "skills":[],

        "experience_years":2,

        "availability":"Unknown",

        "off_topic":False,

        "is_vague":False
    }

    result = score_answer(
        answer,
        "experience"
    )

    assert (
        result["final_score"]
        > 50
    )