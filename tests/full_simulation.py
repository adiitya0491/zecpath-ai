"""
Day 56
Full System Simulation
Zecpath AI
"""

import random


def simulate_candidate():
    """
    Generate a simulated candidate.
    """

    ats = random.randint(60, 90)

    screening = random.randint(60, 85)

    hr = random.randint(65, 90)

    technical = random.randint(60, 95)

    machine_test = random.randint(60, 95)

    behavior_risk = random.choice(
        [
            "Low Risk",
            "Moderate Risk",
            "High Risk"
        ]
    )

    integrity_risk = random.choice(
        [
            "Low Risk",
            "Moderate Risk",
            "High Risk"
        ]
    )

    final_score = round(
        (
            ats +
            screening +
            hr +
            technical +
            machine_test
        ) / 5,
        2
    )

    decision = (
        "Selected"
        if final_score >= 75
        else "Rejected"
    )

    return {

        "scores": {

            "ats":
                ats,

            "screening":
                screening,

            "hr":
                hr,

            "technical":
                technical,

            "machine_test":
                machine_test
        },

        "behavior": {
            "risk_level":
                behavior_risk
        },

        "integrity": {
            "risk_level":
                integrity_risk
        },

        "final_score":
            final_score,

        "decision":
            decision
    }


def run_full_simulation(
    total_candidates=50
):
    """
    Run full pipeline simulation.
    """

    results = []

    for idx in range(
        total_candidates
    ):

        candidate = simulate_candidate()

        candidate[
            "candidate_id"
        ] = f"C{20000 + idx}"

        results.append(
            candidate
        )

    return results


if __name__ == "__main__":

    simulation = run_full_simulation()

    for item in simulation[:5]:

        print(item)