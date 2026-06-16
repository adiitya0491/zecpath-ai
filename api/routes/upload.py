# api/routes/upload.py
import uuid, aiofiles, logging
from pathlib import Path
from datetime import datetime
from fastapi import APIRouter, UploadFile, File, Query, BackgroundTasks
from api.schemas.response_models import UploadResponse
from api.utils.async_jobs import job_queue, JobStatus
from api.utils.error_handler import UploadError

logger     = logging.getLogger("ats_api.upload")
router     = APIRouter()
UPLOAD_DIR = Path("uploads"); UPLOAD_DIR.mkdir(exist_ok=True)
OUTPUT_DIR = Path("outputs"); OUTPUT_DIR.mkdir(exist_ok=True)
MAX_MB     = 10


async def _run_parse_job(job_id, resume_id, file_path, job_title):
    import json, time
    await job_queue.update(job_id, JobStatus.PROCESSING)
    start = time.perf_counter()
    try:
        from parsers.resume_reader      import extract_text_from_resume
        from parsers.text_cleaner       import clean_resume_text
        from parsers.section_classifier import classify_sections
        from parsers.skill_extractor    import detect_skills
        from parsers.experience_parser  import parse_experience
        from parsers.education_parser   import parse_education
        from parsers.certificate_parser import parse_certifications

        raw_text = extract_text_from_resume(file_path)
        if not raw_text or len(raw_text.strip()) < 50:
            raise ValueError(
                "Could not extract text. "
                "PDF may be scanned — ensure Tesseract is installed."
            )

        clean    = clean_resume_text(raw_text)
        sections = classify_sections(clean)

        skill_counts = detect_skills(" ".join(sections.get("skills", [])))
        skills_list  = [
            {
                "name":       k,
                "confidence": min(0.5 + v * 0.1, 0.99),
                "category":   None
            }
            for k, v in skill_counts.items()
        ]

        exp_data  = parse_experience(sections, job_title)
        edu_data  = parse_education(sections)
        cert_data = parse_certifications(sections)

        result = {
            "resume_id":               resume_id,
            "candidate_name":          sections.get("name"),
            "email":                   sections.get("email"),
            "phone":                   sections.get("phone"),
            "skills":                  skills_list,
            "experience":              exp_data.get("jobs", []),
            "total_experience_months": exp_data.get("total_months", 0),
            "education": [
                {
                    "degree":      e.get("degree"),
                    "institution": e.get("institution"),
                    "year":        e.get("year"),
                    "is_relevant": bool(e.get("degree"))
                }
                for e in edu_data
            ],
            "certifications": [
                {
                    "name":   c.get("name"),
                    "issuer": None,
                    "year":   c.get("year")
                }
                for c in cert_data
            ],
            "raw_text":        raw_text,
            "raw_text_length": len(raw_text),
            "parse_time_ms":   round((time.perf_counter() - start) * 1000),
        }

        out_path = OUTPUT_DIR / f"{resume_id}_parsed.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, default=str)

        logger.info("Parsed | resume=%s | %dms",
                    resume_id, result["parse_time_ms"])
        await job_queue.update(job_id, JobStatus.DONE, result=result)

    except Exception as e:
        logger.exception("Parse failed | resume=%s", resume_id)
        await job_queue.update(job_id, JobStatus.FAILED, error=str(e))


@router.post("/upload", response_model=UploadResponse,
             status_code=202, summary="Upload a resume PDF")
async def upload_resume(
    background_tasks: BackgroundTasks,
    file:      UploadFile = File(..., description="PDF only. Max 10MB."),
    job_title: str        = Query(..., description="e.g. 'Cloud Engineer'")
):
    ext = Path(file.filename or "x.pdf").suffix.lower()
    if ext != ".pdf":
        raise UploadError(
            f"Only PDF allowed. Got '{ext}'", 422,
            {"filename": file.filename}
        )

    content = await file.read()
    size_mb  = len(content) / (1024 * 1024)
    if size_mb > MAX_MB:
        raise UploadError(
            f"File {size_mb:.1f}MB exceeds {MAX_MB}MB limit", 413,
            {"size_mb": round(size_mb, 2)}
        )

    resume_id = str(uuid.uuid4())
    file_path = UPLOAD_DIR / f"{resume_id}.pdf"
    async with aiofiles.open(file_path, "wb") as f:
        await f.write(content)

    job = await job_queue.create("parse_resume", {
        "resume_id": resume_id,
        "file_path": str(file_path),
        "job_title": job_title,
        "filename":  file.filename,
    })

    background_tasks.add_task(
        _run_parse_job,
        job.job_id, resume_id, str(file_path), job_title
    )

    logger.info("Uploaded | resume=%s | %.2fMB | job=%s",
                resume_id, size_mb, job.job_id)

    return UploadResponse(
        job_id=job.job_id,
        resume_id=resume_id,
        filename=file.filename,
        upload_time=datetime.utcnow(),
        status="queued",
        message="Uploaded and parsing started. Poll /api/parse/status/{job_id}"
    )