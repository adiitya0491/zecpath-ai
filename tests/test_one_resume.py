import json
from parsers.section_classifier import classify_sections
from utils.logger import get_logger
logger = get_logger()

logger.info("test one resume")

# 👇 CHANGE THIS to whichever resume you want to test
FILE_PATH = "outputs/extracted_text/Cloud Engineer resumes/Cloud_Engineer_1.txt"


def test_single_resume():
    print("\n==== TESTING ONE RESUME ====\n")

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    sections = classify_sections(text)

    print("---- DETECTED SECTIONS ----\n")

    for section, content in sections.items():
        print(f"\n### {section.upper()} ###")
        for line in content[:5]:  # show first 5 lines only
            print("-", line)

    # save JSON output
    output_path = FILE_PATH.replace(
        "extracted_text", "sectioned_resumes"
    ).replace(".txt", ".json")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(sections, f, indent=4)

    print("\nSaved JSON to:", output_path)


if __name__ == "__main__":
    test_single_resume()
