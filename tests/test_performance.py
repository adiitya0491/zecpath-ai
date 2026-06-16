from ai_core.performance_optimized import (
    fast_decision
)


def test_performance():

    result = fast_decision(80)

    assert result == "Selected"


if __name__ == "__main__":

    test_performance()

    print("All tests passed")