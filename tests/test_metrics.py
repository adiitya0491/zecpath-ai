from observability.logging import (
    log_event
)


def test_metrics():

    log = log_event(
        "ATS",
        "test",
        {}
    )

    assert "service" in log

    assert "event_type" in log


if __name__ == "__main__":

    test_metrics()

    print("All tests passed")