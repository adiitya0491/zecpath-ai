"""
Day 50
Machine Test Pipeline
"""

from machine_test.evaluation_logic import (
    calculate_task_score
)

from machine_test.time_scoring import (
    time_score,
    classify_speed
)


def machine_test_pipeline(data):

    task_result = calculate_task_score(

        data["execution_results"]["passed"],

        data["execution_results"]["total"],

        data["execution_results"]["runtime"],

        data["code_snapshot"],

        data["attempts"]
    )

    time_factor = time_score(
        data["time_taken"],
        data["time_limit"]
    )

    final_score = (

        task_result["task_score"] * 0.80 +

        time_factor * 100 * 0.20
    )

    if final_score >= 85:
        decision = "Excellent"

    elif final_score >= 70:
        decision = "Good Performance"

    elif final_score >= 50:
        decision = "Average Performance"

    else:
        decision = "Needs Improvement"

    return {

        "candidate_id":
            data["candidate_id"],

        "task_id":
            data["task_id"],

        "task_score":
            task_result["task_score"],

        "time_score":
            round(time_factor * 100, 2),

        "speed":
            classify_speed(
                data["time_taken"],
                data["time_limit"]
            ),

        "final_score":
            round(final_score, 2),

        "decision":
            decision,

        "details":
            task_result["breakdown"]
    }


if __name__ == "__main__":

    sample_data = {

        "candidate_id": "C5001",

        "task_id": "T101",

        "code_snapshot":
            "def add(a,b): return a+b",

        "execution_results": {

            "passed": 8,

            "total": 10,

            "runtime": 1.2
        },

        "attempts": 2,

        "time_taken": 25,

        "time_limit": 30
    }

    result = machine_test_pipeline(
        sample_data
    )

    print(result)