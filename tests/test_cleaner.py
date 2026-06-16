from parsers.text_cleaner import clean_text
from utils.logger import get_logger
logger = get_logger()

logger.info("test cleaner")

# This is messy extracted resume text (dirty text)
dirty_text = """
• SKILLS
Python   SQL   Power BI!!!

● EDUCATION
B.Tech Computer Science@@@@
"""

# Clean it using our engine
cleaned = clean_text(dirty_text)

# Print the cleaned result
print("✅ Cleaned Output:")
print(cleaned)
