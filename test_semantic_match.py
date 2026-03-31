import json
import os
from ai_engine.semantic_matcher import semantic_match
from utils.logger import get_logger

logger = get_logger()
logger.info("test_semantic_match")

# 📂 FOLDERS
INPUT_FOLDER = "outputs/sectioned_resumes/Cloud Operations Engineer resumes"
OUTPUT_FOLDER = "outputs/semantic_output/Cloud Operations Engineer resumes"

# 📄 JOB DESCRIPTION
JD_FILE = "data/job_descriptions/cloud_engineer_jds/Cloud Operations Engineer.txt"


def run():

    print("\n=== SEMANTIC MATCH ENGINE ===\n")

    if not os.path.exists(INPUT_FOLDER):
        print("❌ Input folder not found.")
        return

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    # load job description
    with open(JD_FILE, encoding="utf-8") as f:
        jd_text = f.read()

    files = [f for f in os.listdir(INPUT_FOLDER) if f.endswith(".json")]

    if not files:
        print("❌ No JSON resumes found.")
        return

    print(f"Found {len(files)} resumes\n")

    for filename in files:

        input_path = os.path.join(INPUT_FOLDER, filename)
        output_path = os.path.join(OUTPUT_FOLDER, filename)

        print(f"[PROCESSING] {filename}")

        try:
            with open(input_path, "r", encoding="utf-8") as f:
                resume_data = json.load(f)

            # semantic matching
            result = semantic_match(resume_data, jd_text)

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=4)

            print(f"[SAVED] {output_path}\n")
            logger.info(f"Semantic match saved: {output_path}")

        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")

    print("✅ Semantic matching complete.")


if __name__ == "__main__":
    run()