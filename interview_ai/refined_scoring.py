"""
Refined Scoring Engine
Zecpath AI - Day 42

Reduces scoring anomalies
and confidence bias.
"""


def normalize_scores(scores):
    """
    Normalize scores to 0-100 scale.
    """

    if not scores:
        return []

    min_score = min(scores)
    max_score = max(scores)

    if min_score == max_score:
        return scores

    normalized = []

    for score in scores:

        value = (
            (score - min_score)
            /
            (max_score - min_score)
        ) * 100

        normalized.append(
            round(value, 2)
        )

    return normalized


def reduce_bias(score, confidence):
    """
    Small confidence adjustment.
    """

    adjusted = (
        score * 0.90
        +
        confidence * 0.10
    )

    return round(adjusted, 2)


def refined_score_pipeline(
    scores,
    confidence_scores
):
    """
    Full optimization pipeline.
    """

    normalized = normalize_scores(scores)

    results = []

    for score, confidence in zip(
        normalized,
        confidence_scores
    ):

        results.append(
            reduce_bias(
                score,
                confidence
            )
        )

    return results


if __name__ == "__main__":

    scores = [45, 60, 75, 90]
    confidence = [70, 80, 85, 90]

    print(
        refined_score_pipeline(
            scores,
            confidence
        )
    )