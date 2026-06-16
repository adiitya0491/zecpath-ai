"""
Day 58
AI Coaching System
Zecpath AI
"""


def generate_feedback(scores):
    """
    Generate candidate improvement suggestions.
    """

    feedback = []

    if scores.get("communication", 0) < 70:
        feedback.append(
            "Improve communication clarity and structure."
        )

    if scores.get("technical", 0) < 70:
        feedback.append(
            "Strengthen technical fundamentals and problem-solving."
        )

    if scores.get("confidence", 0) < 65:
        feedback.append(
            "Work on confidence and interview delivery."
        )

    if not feedback:
        feedback.append(
            "Excellent performance. Continue maintaining your strengths."
        )

    return feedback


if __name__ == "__main__":

    result = generate_feedback(
        {
            "communication": 60,
            "technical": 80,
            "confidence": 50
        }
    )

    print(result)