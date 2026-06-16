"""
Day 61
Metrics Collection System
"""


def calculate_metrics(
    success,
    total,
    response_times
):
    """
    Calculate basic monitoring metrics.
    """

    success_rate = (
        success / total
        if total
        else 0
    )

    avg_latency = (
        sum(response_times)
        / len(response_times)
        if response_times
        else 0
    )

    error_rate = (
        (total - success) / total
        if total
        else 0
    )

    return {
        "success_rate": round(
            success_rate,
            2
        ),
        "avg_latency": round(
            avg_latency,
            2
        ),
        "error_rate": round(
            error_rate,
            2
        )
    }


if __name__ == "__main__":

    metrics = calculate_metrics(
        95,
        100,
        [1.1, 1.2, 0.8, 1.5]
    )

    print(metrics)