# Behavioral Analysis Framework – Zecpath AI

## Objective

The Behavioral AI module evaluates candidate focus,
engagement, attention, and distraction patterns during interviews.

The system uses only non-invasive behavioral signals.

---

# Core Behavioral Signals

## Eye Movement

Measures:

- Gaze stability
- Focus level
- Attention consistency

Signal:

eye_focus

Range:

0 → Poor focus

1 → Excellent focus

---

## Head Movement

Measures:

- Head stability
- Frequent movement
- Distraction indicators

Signal:

head_stability

Range:

0 → Unstable

1 → Stable

---

## Facial Engagement

Measures:

- Candidate attentiveness
- Active participation
- Interview engagement

Signal:

engagement

Range:

0 → Low

1 → High

---

## Attention Pattern

Measures:

- Looking away frequency
- Attention loss

Signal:

distraction

Range:

0 → No distraction

1 → High distraction

---

# Processing Pipeline

Video / Webcam Feed
        ↓
Face Detection
        ↓
Eye Tracking
        ↓
Head Movement Analysis
        ↓
Engagement Detection
        ↓
Signal Normalization
        ↓
Behavior Scoring Engine
        ↓
Behavioral Report Generation

---

# Score Formula

Behavior Score =

(Eye Focus × 0.30)

+

(Head Stability × 0.20)

+

(Engagement × 0.30)

+

(1 − Distraction) × 0.20

---

# Behavioral Levels

85–100
Highly Focused

70–84
Good Engagement

50–69
Moderate

Below 50
Distracted / Low Focus

---

# Behavioral Insights

Generated Insights:

- Focus Level
- Engagement Level
- Risk Level
- Distraction Pattern

---

# Ethical Design Principles

No facial recognition

No identity tracking

No biometric storage

Only metadata stored

Candidate consent required

Privacy-first architecture

---

# Future Improvements

- Gesture Recognition
- Emotion Detection
- Real-Time Behavioral Tracking
- Webcam-Based Interview Analytics
- ML-Based Behavioral Scoring