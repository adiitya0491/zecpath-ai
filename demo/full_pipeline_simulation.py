"""
Day 63

Full Pipeline Simulation

Zecpath AI
"""


def run_demo_pipeline(candidate):

    scores = {

        "C001": {

            "final": 85,

            "decision": "Selected"
        },

        "C002": {

            "final": 68,

            "decision": "Hold / Review"
        },

        "C003": {

            "final": 45,

            "decision": "Rejected"
        }

    }

    return {

        "candidate_id": candidate,

        "result": scores.get(candidate)

    }


if __name__ == "__main__":

    candidates = [

        "C001",

        "C002",

        "C003"

    ]

    for candidate in candidates:

        print(

            run_demo_pipeline(candidate)

        )