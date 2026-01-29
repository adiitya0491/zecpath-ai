# Zecpath AI Code Standards

## 1. General Rules
- Follow Python PEP8 coding style
- Use meaningful variable and function names
- Keep functions small and modular
- Avoid hardcoding values

## 2. Folder-Based Modularity
Each AI service must remain inside its own module:

- parsers/ → Resume parsing
- ats_engine/ → ATS scoring logic
- screening_ai/ → Screening automation
- interview_ai/ → Interview intelligence
- scoring/ → Final decision aggregation

## 3. Documentation Rules
Every function must include a docstring:

Example:

```python
def parse_resume(file_path: str) -> dict:
    """
    Extract candidate information from resume.

    Args:
        file_path (str): Location of resume file

    Returns:
        dict: Parsed resume data
    """
