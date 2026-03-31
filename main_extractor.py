
import os
import traceback
from parsers.resume_reader import extract_text_from_resume
from parsers.text_cleaner import clean_resume_text
from utils.logger import get_logger

logger = get_logger()

logger.info("Main Resume Extraction Engine Started")

# ==========================================================
# CONFIGURATION
# ==========================================================

INPUT_FOLDER = "data/resumes/DevOps Engineer resumes"
OUTPUT_FOLDER = "outputs/extracted_text/DevOps Engineer resumes"

# Ensure output directory exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


# ==========================================================
# SAFE FILE NAME NORMALIZER
# ==========================================================

def safe_filename(filename: str) -> str:
    name, _ = os.path.splitext(filename)
    return name.replace(" ", "_").replace("(", "").replace(")", "") + ".txt"


# ==========================================================
# MAIN PROCESS
# ==========================================================

def process_resumes():

    print("==== Resume Extraction Started ====\n")

    processed = 0
    failed = 0
    skipped = 0

    if not os.path.exists(INPUT_FOLDER):
        print(f"[ERROR] Input folder not found: {INPUT_FOLDER}")
        return

    files = os.listdir(INPUT_FOLDER)

    if not files:
        print("[INFO] No files found in input folder.")
        return

    for file in files:

        file_path = os.path.join(INPUT_FOLDER, file)

        if not file.lower().endswith((".pdf", ".docx")):
            skipped += 1
            continue

        print(f"[PROCESSING] {file}")

        try:
            # Extract raw text
            raw_text = extract_text_from_resume(file_path)

            if not raw_text or len(raw_text.strip()) < 30:
                print(f"[FAILED EXTRACTION] Empty or weak text: {file}")
                failed += 1
                continue

            # Clean text
            cleaned_text = clean_resume_text(raw_text)

            if not cleaned_text or len(cleaned_text.strip()) < 30:
                print(f"[FAILED CLEANING] Cleaned text too small: {file}")
                failed += 1
                continue

            # Prepare output file path safely
            output_file = os.path.join(
                OUTPUT_FOLDER,
                safe_filename(file)
            )

            # Write as UTF-8 (important to avoid binary issues)
            # Force safe UTF-8 encoding
            # Prepare output file path safely
            output_file = os.path.join(
                OUTPUT_FOLDER,
                safe_filename(file)
            )

            # -------- HARD CLEAN BEFORE SAVE --------

            # Ensure string
            if not isinstance(cleaned_text, str):
                cleaned_text = str(cleaned_text)

            # Remove NULL bytes
            cleaned_text = cleaned_text.replace("\x00", "")

            # Remove zero-width & hidden unicode chars
            cleaned_text = cleaned_text.replace("\u200b", "")
            cleaned_text = cleaned_text.replace("\ufeff", "")

            # Remove all non-printable characters
            cleaned_text = "".join(
                ch for ch in cleaned_text
                if ch.isprintable() or ch in "\n\t"
            )

            # Save clean text
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(cleaned_text)

            print(f"[SAVED] {output_file}\n")
            processed += 1

        except Exception as e:
            print(f"[ERROR] {file}")
            print(str(e))
            print(traceback.format_exc())
            failed += 1

    print("\n==== Extraction Finished ====")
    print(f"Processed : {processed}")
    print(f"Failed    : {failed}")
    print(f"Skipped   : {skipped}")
    print(f"Output Dir: {OUTPUT_FOLDER}")


# ==========================================================
# RUN
# ==========================================================

if __name__ == "__main__":
    process_resumes()