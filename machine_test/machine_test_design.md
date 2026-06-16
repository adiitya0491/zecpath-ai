# Machine Test AI Design – Zecpath

## Objective

Evaluate real-world technical skills using practical tasks.

---

# Supported Machine Test Types

## Coding Problems

Examples:

- Arrays
- Strings
- Recursion
- Dynamic Programming

Purpose:

Evaluate coding and logical ability.

---

## Debugging Tasks

Examples:

- Fix syntax errors
- Fix runtime errors
- Fix logic bugs

Purpose:

Evaluate debugging skills.

---

## File-Based Tasks

Examples:

- React Component Fixes
- API Modifications
- SQL Query Optimization

Purpose:

Evaluate real project experience.

---

## Mini System Design

Examples:

- URL Shortener
- Notification Service
- Chat System

Purpose:

Evaluate architecture thinking.

---

# High-Level Architecture

Candidate Interface
        ↓
Code Editor
        ↓
Code Capture Engine
        ↓
Execution Sandbox
        ↓
Test Case Evaluator
        ↓
Code Quality Analyzer
        ↓
Scoring Engine
        ↓
Report Generator

---

# Evaluation Metrics

## Correctness

Measures:

- Test case success rate

Weight:

40%

---

## Efficiency

Measures:

- Runtime performance

Weight:

20%

---

## Code Quality

Measures:

- Readability
- Maintainability
- Structure

Weight:

20%

---

## Problem Solving

Measures:

- Number of attempts
- Solution approach

Weight:

20%

---

# Scoring Formula

Task Score =

(Correctness × 0.40)

+

(Efficiency × 0.20)

+

(Code Quality × 0.20)

+

(Problem Solving × 0.20)

---

# Time Scoring Formula

Final Score =

(Task Score × 0.80)

+

(Time Score × 0.20)

---

# Input Capture Example

{
  "candidate_id": "C5001",

  "task_id": "T101",

  "code_snapshot":
      "def add(a,b): return a+b",

  "execution_results": {

      "passed": 8,

      "total": 10,

      "runtime": 1.2
  },

  "attempts": 2,

  "time_taken": 25
}

---

# Output Example

{
  "candidate_id": "C5001",

  "final_score": 76.8,

  "decision": "Good Performance"
}

---

# Advantages

- Practical evaluation
- Objective scoring
- Scalable assessment
- Recruiter-friendly reporting

---

# Limitations

- No deep code review
- No plagiarism detection
- No live coding analysis

---

# Future Improvements

- AI Code Review
- Plagiarism Detection
- Live Coding Sessions
- AST-Based Analysis
- LLM Code Understanding