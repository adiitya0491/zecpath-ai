from parsers.resume_reader import extract_resume_text
from utils.logger import get_logger
logger = get_logger()
logger.info("test reader")
# Test resume file path
file_path = "data/resumes/sample.pdf"

# Extract resume text
text = extract_resume_text(file_path)

# Print output
print("✅ Resume Text Extracted Successfully!")
print(text[:500])  # Print first 500 characters only
