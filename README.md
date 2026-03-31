# Zecpath AI - Intelligent Hiring Platform

## Overview

Zecpath AI is an autonomous AI-powered hiring platform that automates resume parsing, candidate screening, and job-description matching using NLP and semantic similarity techniques.

## Architecture

```
zecpath-ai/
├── parsers/              # Resume & JD parsing modules
│   ├── resume_reader.py   # PDF/DOCX text extraction + OCR
│   ├── text_cleaner.py   # Text normalization
│   ├── section_classifier.py  # Section detection (skills/exp/edu)
│   ├── skill_extractor.py      # Skill detection with confidence
│   ├── experience_parser.py    # Experience timeline extraction
│   ├── education_parser.py     # Education details extraction
│   ├── jd_parser.py            # Job description parsing
│   └── resume_parser.py        # Combined resume parser
├── ai_engine/            # AI matching engine
│   └── semantic_matcher.py     # Sentence transformer similarity
├── ats_engine/          # ATS scoring
│   └── ats_scorer.py           # Skill match percentage
├── scoring/             # Final weighted scoring
│   └── ats_engine.py           # Role-based weighted scoring
├── screening_ai/       # Screening assistant modules
├── interview_ai/       # Interview intelligence
├── utils/              # Utilities
│   └── logger.py       # Logging system
├── data/               # Sample resumes & job descriptions
├── tests/              # Unit tests
└── logs/               # Log storage
```

## Algorithm & Processing Pipeline

### Step-by-Step Procedure

#### 1. Resume Text Extraction (`resume_reader.py`)
- **Input**: PDF or DOCX file
- **Process**:
  - For PDF: Uses `pdfplumber` for text extraction
  - Falls back to OCR (Tesseract) if extraction yields <20 chars
  - For DOCX: Uses `python-docx` to extract paragraphs
- **Output**: Raw text string

#### 2. Text Cleaning (`text_cleaner.py`)
- Removes special characters, extra whitespace
- Normalizes unicode characters
- Handles encoding issues
- **Output**: Cleaned normalized text

#### 3. Section Classification (`section_classifier.py`)
- Detects sections using keyword matching:
  - `skills`, `experience`, `education`, `projects`, `certifications`
- Special handling for skills (split by delimiters)
- **Output**: Dictionary with categorized sections

#### 4. Skill Extraction (`skill_extractor.py`)
- Master skill dictionary with variants
- Regex-based skill detection
- Confidence scoring:
  - 3+ occurrences → 0.95
  - 2 occurrences → 0.85
  - 1 occurrence → 0.70
- **Output**: List of skills with confidence scores

#### 5. Experience Parsing (`experience_parser.py`)
- Regex to extract date ranges (multiple formats)
- Parses role titles from date patterns
- Calculates duration in months/years
- Relevance scoring based on target role keywords
- **Output**: Total experience years, role list, relevance score

#### 6. Education Parsing (`education_parser.py`)
- Detects degree types (B.Tech, M.Tech, Bachelor, Master, PhD)
- Extracts field of study (CS, AI, IT, etc.)
- Extracts institution names
- Parses graduation years
- **Output**: Education details list

#### 7. Job Description Parsing (`jd_parser.py`)
- Extracts job title (first meaningful line)
- Extracts required skills from "Required Skills" section
- Extracts experience requirements (ranges or minimums)
- Extracts responsibilities and qualifications
- **Output**: Structured JD data

#### 8. Semantic Matching (`semantic_matcher.py`)
- Uses `sentence-transformers` (all-MiniLM-L6-v2)
- Encodes resume and JD text to embeddings
- Computes cosine similarity
- Threshold: 0.6 (match if score > 0.6)
- **Output**: Similarity score (0-1)

#### 9. ATS Scoring (`ats_engine/ats_scorer.py`)
- Calculates skill match percentage:
  - `score = (matched_skills / required_skills) * 100`
- **Output**: ATS score (0-100)

#### 10. Final Weighted Scoring (`scoring/ats_engine.py`)
- Role-based weighted scoring (example: AI Engineer):
  - Skills: 35%
  - Experience: 25%
  - Education: 15%
  - Semantic Match: 25%
- **Output**: Final score with breakdown

## Usage

### Environment Setup
```bash
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### Extract Resume Text
```bash
python main_extractor.py
```

### Run Tests
```bash
pytest tests/
```

## Key Dependencies

- **pdfplumber** - PDF text extraction
- **pytesseract** + **pdf2image** - OCR for scanned PDFs
- **python-docx** - DOCX parsing
- **sentence-transformers** - Semantic embeddings
- **spacy** - NLP processing
- **scikit-learn** - ML utilities

## Scoring Weights (Customizable)

| Role       | Skills | Experience | Education | Semantic |
|------------|--------|------------|-----------|----------|
| AI Engineer| 35%    | 25%        | 15%       | 25%      |

## Output Example

```json
{
  "final_score": 78.5,
  "breakdown": {
    "skills": 85.0,
    "experience": 72.0,
    "education": 80.0,
    "semantic": 0.72
  },
  "weights": {
    "skills": 0.35,
    "experience": 0.25,
    "education": 0.15,
    "semantic": 0.25
  }
}
```

## License

Proprietary - Zecpath AI
