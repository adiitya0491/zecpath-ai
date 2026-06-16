from screening_ai.scoring_engine import (
    score_answer
)

answer = {

    "question_id":"Q3",

    "original_text":
    "I have 4 years experience in AWS Docker",

    "intent":"experience",

    "skills":[
        "aws",
        "docker"
    ],

    "experience_years":4,

    "availability":"Immediate",

    "off_topic":False,

    "is_vague":False
}

print(
    score_answer(
        answer,
        "experience"
    )
)