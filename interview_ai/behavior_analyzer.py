from interview_ai.confidence_analyzer import (
    calculate_confidence
)

from interview_ai.sentiment_engine import (
    sentiment_score
)

from interview_ai.contradiction_detector import (
    detect_contradiction
)

from interview_ai.stress_detector import (
    stress_score
)


# ==========================================================
# BEHAVIOR ANALYSIS PIPELINE
# ==========================================================

def analyze_behavior(text, duration):
    confidence = calculate_confidence(
        text,
        duration
    )

    sentiment = sentiment_score(text)

    contradiction = detect_contradiction(text)

    stress = stress_score(text)

    final_score = (
        confidence["confidence_score"] * 0.50 +
        sentiment["sentiment_score"] * 100 * 0.20 +
        stress * 100 * 0.30
    )

    return {
        "confidence": confidence,
        "sentiment": sentiment,
        "stress_score": round(stress, 2),
        "contradiction": contradiction,
        "behavioral_score": round(final_score, 2)
    }


# ==========================================================
# DEMO
# ==========================================================

if __name__ == "__main__":

    sample_text = (
        "I think I am confident but maybe "
        "I need improvement."
    )

    result = analyze_behavior(
        sample_text,
        duration=6
    )

    print(result)