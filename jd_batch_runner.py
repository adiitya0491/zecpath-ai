import json
from parsers.jd_parser import parse_job_description
from utils.logger import get_logger
logger = get_logger()

logger.info("jd phaser")

# -------- INPUT FILE --------
INPUT_FILE = "data/job_descriptions/cloud_engineer_jds/Cloud Infrastructure Engineer.txt"

# -------- OUTPUT FILE --------
OUTPUT_FILE = "outputs/jd_parsed/cloud_engineer_jds_parsed/Cloud Infrastructure Engineer.json"

# Read text file
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    jd_text = f.read()

# Parse job description
parsed_output = parse_job_description(jd_text)

# Save JSON output
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(parsed_output, f, indent=4)

print("✅ Parsing complete")
print(f"📥 Input file: {INPUT_FILE}")
print(f"📤 Output file: {OUTPUT_FILE}")