"""
Day 61
Alerting System
"""


def check_alerts(metrics):
    """
    Generate alerts based on thresholds.
    """

    alerts = []

    if metrics.get(
        "avg_latency",
        0
    ) > 2:
        alerts.append(
            "High latency detected"
        )

    if metrics.get(
        "success_rate",
        1
    ) < 0.90:
        alerts.append(
            "Low success rate"
        )

    if metrics.get(
        "error_rate",
        0
    ) > 0.10:
        alerts.append(
            "High error rate"
        )

    return alerts


if __name__ == "__main__":

    sample_metrics = {
        "success_rate": 0.85,
        "avg_latency": 2.5,
        "error_rate": 0.15
    }

    print(
        check_alerts(
            sample_metrics
        )
    )