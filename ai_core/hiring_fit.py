"""
Hiring Fit Calculator
Zecpath AI - Day 41
"""


def calculate_hiring_fit(score):
    """
    Converts score into fit category.
    """

    if score >= 80:
        fit = "Excellent Fit"

    elif score >= 65:
        fit = "Good Fit"

    elif score >= 50:
        fit = "Moderate Fit"

    else:
        fit = "Low Fit"

    return {
        "hiring_fit_percentage": round(score, 2),
        "fit_category": fit
    }