# Dynamic Follow-Up Logic Framework

## Objective

Enable adaptive AI questioning based on candidate responses.

---

## Answer Quality Levels

| Quality | Meaning |
|----------|----------|
| empty | No answer |
| too_short | Very short answer |
| uncertain | Candidate unsure |
| basic | Some detail but limited |
| good | Complete answer |

---

## Follow-Up Types

### Clarification
Used for uncertain answers.

### Elaboration
Used for short answers.

### Example-Based
Used for basic answers.

### Advanced Probe
Used for strong answers.

---

## Difficulty Modes

| Mode | Usage |
|--------|--------|
| simplify | Weak answers |
| example | Medium answers |
| advanced | Strong answers |
| normal | Default |

---

## State Tracking

Tracks:

- Asked questions
- Candidate answers
- Prevents repetition

---

## Benefits

- Human-like conversations
- Better evaluation
- Adaptive interviews

---

## Limitations

- Rule-based logic
- No deep reasoning

---

## Future Improvements

- LLM follow-ups
- Context memory
- Emotion detection