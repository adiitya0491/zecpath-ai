"""
Day 60
API Latency Optimization
"""

import time


def optimized_response(data):
    """
    Measure API response latency.
    """

    start = time.time()

    result = {
        "data": data
    }

    latency = (
        time.time() - start
    ) * 1000

    return {
        "result": result,
        "latency_ms": round(latency, 2)
    }


if __name__ == "__main__":

    print(
        optimized_response(
            {
                "candidate": "C100"
            }
        )
    )