"""
Day 50
Machine Test Evaluation Logic
"""

# ----------------------------------
# Correctness Evaluation
# ----------------------------------

def correctness_score(passed, total):

    if total == 0:
        return 0

    return passed / total


# ----------------------------------
# Efficiency Score
# ----------------------------------

def efficiency_score(runtime):

    if runtime < 1:
        return 1.0

    elif runtime < 2:
        return 0.7

    return 0.4


# ----------------------------------
# Code Quality Score
# ----------------------------------

def code_quality_score(code):

    length = len(code.splitlines())

    if length < 20:
        return 1.0

    elif length < 50:
        return 0.7

    return 0.4


# ----------------------------------
# Problem Solving Score
# ----------------------------------

def problem_solving_score(attempts):

    if attempts == 1:
        return 1.0

    elif attempts <= 3:
        return 0.7

    return 0.4


# ----------------------------------
# Final Task Score
# ----------------------------------

def calculate_task_score(
    passed,
    total,
    runtime,
    code,
    attempts
):

    correctness = correctness_score(
        passed,
        total
    )

    efficiency = efficiency_score(
        runtime
    )

    quality = code_quality_score(
        code
    )

    problem = problem_solving_score(
        attempts
    )

    final = (
        correctness * 0.40 +
        efficiency * 0.20 +
        quality * 0.20 +
        problem * 0.20
    )

    return {

        "task_score":
            round(final * 100, 2),

        "breakdown": {

            "correctness":
                round(correctness, 2),

            "efficiency":
                round(efficiency, 2),

            "code_quality":
                round(quality, 2),

            "problem_solving":
                round(problem, 2)
        }
    }


if __name__ == "__main__":

    result = calculate_task_score(
        8,
        10,
        1.2,
        "print('hello')",
        2
    )

    print(result)