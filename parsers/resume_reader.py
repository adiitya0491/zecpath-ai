
from docx import Document
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
from pathlib import Path
import os
import pdfplumber
MAX_TEXT_LENGTH = 5000

try:
    from docx import Document
    DOCX_OK = True
except ImportError:
    DOCX_OK = False

try:
    import pytesseract
    from pdf2image import convert_from_path
    from PIL import Image
    Image.MAX_IMAGE_PIXELS = None
    _tess = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    if os.path.exists(_tess):
        pytesseract.pytesseract.tesseract_cmd = _tess
    OCR_OK = True
except ImportError:
    OCR_OK = False

try:
    import pytesseract
    from pdf2image import convert_from_path
    from PIL import Image
    Image.MAX_IMAGE_PIXELS = None
    # Windows path — ignored on Linux/Mac
    _tess = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    if os.path.exists(_tess):
        pytesseract.pytesseract.tesseract_cmd = _tess
    OCR_OK = True
except ImportError:
    OCR_OK = False


# ── PUBLIC ENTRY POINT ────────────────────────────────────────────
def extract_text_from_resume(file_path: str) -> str:

    """
    Main function called by ALL other modules.
    Tries text extraction first, falls back to OCR for scanned PDFs.
    Supports: .pdf (text), .pdf (scanned/image), .docx
    """
    path = str(file_path).lower()

    if path.endswith(".pdf"):
        text = _extract_pdf_text(file_path)
        if not text or len(text.strip()) < 50:
            if OCR_OK:
                text = _extract_pdf_ocr(file_path)
            else:
                raise ValueError(
                    f"Could not extract text from '{file_path}'. "
                    "PDF appears scanned but pytesseract/pdf2image not installed."
                )
        return text[:MAX_TEXT_LENGTH]

        if path.endswith(".docx"):
            if not DOCX_OK:
                raise ImportError("Install python-docx: pip install python-docx")

            text = _extract_docx(file_path)

            return text[:MAX_TEXT_LENGTH]

    raise ValueError(f"Unsupported file type: {file_path}")


# ── PDF TEXT EXTRACTION (two-column aware) ────────────────────────
def _extract_pdf_text(file_path: str) -> str:
    text = ""
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                words = page.extract_words(x_tolerance=3, y_tolerance=3)
                if not words:
                    continue
                pw = page.width
                left  = [w for w in words if w["x0"] < pw * 0.55]
                right = [w for w in words if w["x0"] >= pw * 0.55]

                def _build(wlist):
                    lines = {}
                    for w in sorted(wlist, key=lambda x: (x["top"], x["x0"])):
                        k = round(w["top"] / 5) * 5
                        lines.setdefault(k, []).append(w["text"])
                    return "\n".join(" ".join(v) for _, v in sorted(lines.items()))

                if right:
                    text += _build(left) + "\n\n" + _build(right) + "\n"
                else:
                    text += _build(left) + "\n"
    except Exception as e:
        print(f"[resume_reader] PDF text error: {e}")
    return text


# ── OCR FALLBACK (scanned PDFs) ───────────────────────────────────
def _extract_pdf_ocr(file_path: str) -> str:
    text = ""
    try:
        pages = convert_from_path(file_path, dpi=300)
        for page in pages:
            t = pytesseract.image_to_string(page, lang="eng")
            text += t.encode("utf-8", errors="ignore").decode("utf-8") + "\n"
    except Exception as e:
        print(f"[resume_reader] OCR error: {e}")
    return text


# ── DOCX ─────────────────────────────────────────────────────────
def _extract_docx(file_path: str) -> str:
    doc = Document(file_path)
    return "\n".join(p.text for p in doc.paragraphs if p.text.strip())

# ==========================================================
# BACKWARD COMPATIBILITY
# ==========================================================

def extract_resume_text(file_path):
    """
    Legacy wrapper expected by tests.
    """
    return extract_text_from_resume(file_path)

# ==========================================
# Compatibility Alias For Tests
# ==========================================

def extract_resume_text(file_path):
    return extract_text_from_resume(file_path)