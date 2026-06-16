"""
Day 50
Machine Test Tests
"""

from machine_test.evaluation_logic import (
    calculate_task_score
)

from machine_test.time_scoring import (
    time_score
)

from machine_test.machine_test_pipeline import (
    machine_test_pipeline
)


def test_task_score():

    result = calculate_task_score(

        5,

        10,

        1.5,

        "print('hello')",

        2
    )

    assert result["task_score"] > 0


def test_time_score():

    result = time_score(
        15,
        30
    )

    assert result > 0


def test_machine_pipeline():

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

    assert "final_score" in result

    assert "decision" in result


if __name__ == "__main__":

    test_task_score()

    test_time_score()

    test_machine_pipeline()

    print("All tests passed")