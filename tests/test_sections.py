import json
import os
from parsers.section_classifier import classify_sections 
from utils.logger import get_logger
logger = get_logger()

logger.info("test sections")

INPUT_FOLDER = "outputs/extracted_text/Cloud Engineer resumes"
OUTPUT_FOLDER = "outputs/sectioned_resumes/Cloud Engineer resumes"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for filename in os.listdir(INPUT_FOLDER):
    if filename.endswith(".txt"):
        input_path = os.path.join(INPUT_FOLDER, filename)

        with open(input_path, "r", encoding="utf-8") as f:
            text = f.read()

        sections = classify_sections(text)

        output_filename = filename.replace(".txt", ".json")
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(sections, f, indent=2)

        print(f"Saved structured resume → {output_path}")