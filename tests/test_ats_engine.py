import json
import os
from scoring.ats_engine import generate_candidate_score
from ai_engine.resume_normalizer import normalize_resume
from utils.logger import get_logger

logger = get_logger()
logger.info("test_ats_engine")

INPUT_FOLDER = "outputs/semantic_output/Cloud Engineer resumes"
OUTPUT_FOLDER = "outputs/ats_scores/Cloud Engineer resumes"


def run():

    print("\n=== ATS SCORING ENGINE ===\n")

    if not os.path.exists(INPUT_FOLDER):
        print("❌ Input folder not found.")
        return

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    files = [f for f in os.listdir(INPUT_FOLDER) if f.endswith(".json")]

    if not files:
        print("❌ No JSON files found.")
        return

    print(f"Found {len(files)} resumes\n")

    for filename in files:

        input_path = os.path.join(INPUT_FOLDER, filename)
        output_path = os.path.join(OUTPUT_FOLDER, filename)

        print(f"[PROCESSING] {filename}")

        try:

            with open(input_path, "r", encoding="utf-8") as f:
                semantic_data = json.load(f)

            # Get semantic similarity from Day-12 engine
            semantic_score = semantic_data.get("similarity_score", 0)

            # Generate dynamic scores based on semantic similarity
            skill_score = round(min(semantic_score + 0.25, 1), 3)
            experience_score = round(min(semantic_score + 0.15, 1), 3)
            education_score = round(min(semantic_score + 0.35, 1), 3)
            certification_score = round(min(semantic_score + 0.10, 1), 3)

            result = generate_candidate_score(
                skill_score,
                experience_score,
                education_score,
                certification_score,
                semantic_score
            )

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=4)

            print(f"[SAVED] {output_path}\n")

        except Exception as e:
            print(f"❌ Error processing {filename}: {e}\n")

    print("✅ ATS scoring complete.")


if __name__ == "__main__":
    run()