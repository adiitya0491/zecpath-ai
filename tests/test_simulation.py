"""
Day 56
Simulation Test
"""

from tests.full_simulation import (
    run_full_simulation
)


def test_simulation():

    results = run_full_simulation(10)

    assert len(results) == 10


def test_candidate_structure():

    results = run_full_simulation(1)

    candidate = results[0]

    assert "scores" in candidate

    assert "decision" in candidate

    assert "final_score" in candidate


if __name__ == "__main__":

    test_simulation()

    test_candidate_structure()

    print(
        "All tests passed"
    )