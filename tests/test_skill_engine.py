import os
import json
from parsers.skill_extractor import detect_skills, assign_confidence


# ==========================================================
# CONFIG
# ==========================================================

INPUT_FOLDER = "outputs/extracted_text/Cloud Engineer resumes"
OUTPUT_FOLDER = "outputs/skills_output/Cloud Engineer resumes"


# ==========================================================
# CHECK FOLDERS
# ==========================================================

if not os.path.exists(INPUT_FOLDER):
    print("❌ Input folder not found.")
    exit()

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

files = [f for f in os.listdir(INPUT_FOLDER) if f.endswith(".txt")]

if not files:
    print("❌ No .txt files found.")
    exit()

print(f"\nFound {len(files)} resumes\n")


# ==========================================================
# PROCESS FILES
# ==========================================================

for file in files:

    print(f"Processing: {file}")

    input_path = os.path.join(INPUT_FOLDER, file)

    with open(input_path, "r", encoding="utf-8") as f:
        resume_text = f.read()

    # Skill detection
    skill_counts = detect_skills(resume_text)
    scored_skills = assign_confidence(skill_counts)

    output_data = {
        "total_skills_found": len(scored_skills),
        "skills": scored_skills
    }

    output_filename = file.replace(".txt", "_skills.json")
    output_path = os.path.join(OUTPUT_FOLDER, output_filename)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=4)

    print(f"Saved → {output_path}\n")

print("✅ Skill extraction complete.")