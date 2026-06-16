import json
import os
from parsers.certificate_parser import build_academic_profile
from utils.logger import get_logger

logger = get_logger()
logger.info("test_certificate")

INPUT_FOLDER = "outputs/sectioned_resumes/Cloud Engineer resumes"
OUTPUT_FOLDER = "outputs/certification_output/Cloud Engineer resumes"


def run():

    print("\n=== CERTIFICATE ENGINE ===\n")

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
                data = json.load(f)

            result = build_academic_profile(data)

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=4)

            print(f"[SAVED] {output_path}\n")

        except Exception as e:
            print(f"❌ Error processing {filename}: {e}\n")

    print("✅ Certificate engine complete.")


if __name__ == "__main__":
    run()