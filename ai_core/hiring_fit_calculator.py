"""
Day 51
Hiring Fit Calculator
"""


def calculate_hiring_fit(score):

    if score >= 85:
        category = "Excellent Fit"

    elif score >= 70:
        category = "Strong Fit"

    elif score >= 55:
        category = "Moderate Fit"

    else:
        category = "Low Fit"

    return {

        "hiring_fit_percentage":
            round(score, 2),

        "fit_category":
            category
    }


def get_hiring_decision(score):

    if score >= 75:
        return "Hire"

    elif score >= 55:
        return "Consider"

    return "Reject"


if __name__ == "__main__":

    result = calculate_hiring_fit(82)

    print(result)

    print(
        get_hiring_decision(82)
    )