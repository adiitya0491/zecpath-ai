import pdfplumber
from docx import Document
import pytesseract
from pdf2image import convert_from_path
from PIL import Image

Image.MAX_IMAGE_PIXELS = None

# ⚠️ Update this path to your system
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text_from_resume(file_path: str) -> str:

    if file_path.lower().endswith(".pdf"):
        text = extract_pdf_text(file_path)

        # If normal extraction fails → try OCR
        if not text or len(text.strip()) < 20:
            text = extract_pdf_ocr(file_path)

        return text

    elif file_path.lower().endswith(".docx"):
        return extract_docx(file_path)

    return ""


def extract_pdf_text(file_path: str) -> str:

    text = ""

    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:

                words = page.extract_words()

                if not words:
                    continue

                # Get page width
                page_width = page.width

                # Split words into left and right column
                left_words = []
                right_words = []

                for word in words:
                    if word["x0"] < page_width / 2:
                        left_words.append(word)
                    else:
                        right_words.append(word)

                # Sort each column by vertical position
                left_words = sorted(left_words, key=lambda w: (w["top"], w["x0"]))
                right_words = sorted(right_words, key=lambda w: (w["top"], w["x0"]))

                # Reconstruct lines
                def build_text(word_list):
                    lines = {}
                    for w in word_list:
                        top = round(w["top"])
                        lines.setdefault(top, []).append(w["text"])
                    ordered = sorted(lines.items())
                    return "\n".join([" ".join(words) for _, words in ordered])

                left_text = build_text(left_words)
                right_text = build_text(right_words)

                # Combine properly: left first, then right
                text += left_text + "\n\n" + right_text + "\n"

    except Exception as e:
        print("PDF Extraction Error:", e)

    return text


def extract_pdf_ocr(file_path: str) -> str:

    text = ""

    try:
        pages = convert_from_path(file_path, dpi=200)

        for page in pages:
            ocr_text = pytesseract.image_to_string(page)
            ocr_text = ocr_text.encode("utf-8", errors="ignore").decode("utf-8")
            text += ocr_text + "\n"

    except Exception as e:
        print("PDF Extraction Error:", e)

    return text


def extract_docx(file_path: str) -> str:

    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])