import random


# ==========================================================
# CANDIDATE SIMULATION
# ==========================================================

def simulate_candidate(candidate_type):
    """
    Simulate AI score and Human score
    for different candidate types.
    """

    score_ranges = {
        "Confident": (80, 95),
        "Hesitant": (55, 70),
        "Inexperienced": (50, 65),
        "Overqualified": (75, 90)
    }

    low, high = score_ranges[candidate_type]

    ai_score = random.randint(low, high)

    # Human evaluator score
    human_score = ai_score + random.randint(-5, 5)

    # Keep score inside 0-100
    human_score = max(0, min(100, human_score))

    return {
        "candidate_type": candidate_type,
        "ai_score": ai_score,
        "human_score": human_score,
        "decision_ai": get_decision(ai_score),
        "decision_human": get_decision(human_score)
    }


# ==========================================================
# DECISION LOGIC
# ==========================================================

def get_decision(score):
    """
    Convert score into hiring decision.
    """

    if score >= 75:
        return "Strong Hire"

    if score >= 55:
        return "Consider"

    return "Reject"


# ==========================================================
# ACCURACY CALCULATION
# ==========================================================

def calculate_accuracy(results):
    """
    Compare AI decisions vs Human decisions.
    """

    if not results:
        return 0

    matches = sum(
        1
        for item in results
        if item["decision_ai"] == item["decision_human"]
    )

    return round((matches / len(results)) * 100, 2)


# ==========================================================
# CANDIDATE TYPE ANALYSIS
# ==========================================================

def analyze_by_type(results):

    summary = {}

    candidate_types = [
        "Confident",
        "Hesitant",
        "Inexperienced",
        "Overqualified"
    ]

    for candidate_type in candidate_types:

        filtered = [
            item
            for item in results
            if item["candidate_type"] == candidate_type
        ]

        if not filtered:
            continue

        accuracy = calculate_accuracy(filtered)

        avg_ai = round(
            sum(x["ai_score"] for x in filtered) / len(filtered),
            2
        )

        avg_human = round(
            sum(x["human_score"] for x in filtered) / len(filtered),
            2
        )

        summary[candidate_type] = {
            "accuracy": accuracy,
            "avg_ai_score": avg_ai,
            "avg_human_score": avg_human
        }

    return summary


# ==========================================================
# MAIN SIMULATION
# ==========================================================

def run_simulation(total_candidates=40):

    candidate_types = [
        "Confident",
        "Hesitant",
        "Inexperienced",
        "Overqualified"
    ]

    results = []

    for _ in range(total_candidates):

        candidate_type = random.choice(candidate_types)

        result = simulate_candidate(candidate_type)

        results.append(result)

    overall_accuracy = calculate_accuracy(results)

    type_analysis = analyze_by_type(results)

    return {
        "total_candidates": total_candidates,
        "overall_accuracy": overall_accuracy,
        "results": results,
        "type_analysis": type_analysis
    }


# ==========================================================
# EXECUTION
# ==========================================================

if __name__ == "__main__":

    simulation = run_simulation()

    print("\n=== HR INTERVIEW SIMULATION REPORT ===\n")

    print("Total Candidates:",
          simulation["total_candidates"])

    print("Overall Accuracy:",
          simulation["overall_accuracy"], "%")

    print("\n=== TYPE ANALYSIS ===")

    for candidate_type, metrics in simulation["type_analysis"].items():

        print(f"\n{candidate_type}")

        print("Accuracy:",
              metrics["accuracy"])

        print("Average AI Score:",
              metrics["avg_ai_score"])

        print("Average Human Score:",
              metrics["avg_human_score"])