"""
Day 60
Load Test Simulation
"""

import random


def simulate_load(
    n=1000
):

    response_times = []

    for _ in range(n):

        response_time = random.uniform(
            0.5,
            1.5
        )

        response_times.append(
            response_time
        )

    avg_response = (
        sum(response_times)
        / len(response_times)
    )

    return {
        "avg_response": round(
            avg_response,
            2
        ),
        "max_response": round(
            max(response_times),
            2
        )
    }


if __name__ == "__main__":

    print(
        simulate_load()
    )