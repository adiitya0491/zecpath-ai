import random


QUESTION_BANK = {

    "JavaScript": {

        "basic": [
            "What is a variable?",
            "Explain let vs var."
        ],

        "intermediate": [
            "Explain closures.",
            "How does the event loop work?"
        ],

        "advanced": [
            "Design a scalable frontend architecture."
        ]
    },

    "Python": {

        "basic": [
            "What is a list?",
            "Explain loops."
        ],

        "intermediate": [
            "Explain decorators.",
            "How does Python memory management work?"
        ],

        "advanced": [
            "Design a scalable backend system."
        ]
    },

    "Docker": {

        "basic": [
            "What is Docker?"
        ],

        "intermediate": [
            "Explain Docker Compose."
        ],

        "advanced": [
            "Design a containerized deployment architecture."
        ]
    }
}


def generate_question(skill, difficulty):

    questions = QUESTION_BANK.get(
        skill,
        {}
    ).get(
        difficulty,
        []
    )

    if not questions:
        return "No question available"

    return random.choice(questions)


if __name__ == "__main__":

    print(
        generate_question(
            "JavaScript",
            "basic"
        )
    )