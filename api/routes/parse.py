# api/routes/parse.py — all imports fixed to your actual files
import json, time, logging
from pathlib import Path
from fastapi import APIRouter, BackgroundTasks
from api.schemas.request_models  import ParseRequest
from api.schemas.response_models import ParseStatusResponse
from api.utils.async_jobs        import job_queue, JobStatus
from api.utils.error_handler     import JobNotFoundError, ResumeParseError

logger     = logging.getLogger("ats_api.parse")
router     = APIRouter()
OUTPUT_DIR = Path("outputs"); OUTPUT_DIR.mkdir(exist_ok=True)

async def _run_parse_job(job_id, resume_id, file_path, job_title):
    await job_queue.update(job_id, JobStatus.PROCESSING)
    start = time.perf_counter()
    try:
        # ── CORRECT IMPORTS — your actual files ──────────────────

        from parsers.resume_reader      import extract_text_from_resume


        from parsers.text_cleaner       import clean_resume_text


        from parsers.section_classifier import classify_sections


        from parsers.skill_extractor    import detect_skills


        from parsers.experience_parser  import parse_experience


        from parsers.education_parser   import parse_education


        from parsers.certificate_parser import parse_certifications

        # ────────────────────────────────────────────────────────

        raw_text = extract_text_from_resume(file_path)
        if not raw_text or len(raw_text.strip()) < 50:
            raise ResumeParseError("Could not extract text. PDF may be scanned — ensure Tesseract is installed.")

        clean    = clean_resume_text(raw_text)
        sections = classify_sections(clean)

        # detect_skills returns {skill: count} dict
        skill_counts = detect_skills(" ".join(sections.get("skills", [])))
        skills_list  = [
            {"name": k, "confidence": min(0.5 + v*0.1, 0.99), "category": None}
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
            "experience":             exp_data.get("jobs", []),
            "total_experience_months": exp_data.get("total_months", 0),
            "education": [
                {"degree": e.get("degree"), "institution": e.get("institution"),
                 "year": e.get("year"), "is_relevant": bool(e.get("degree"))}
                for e in edu_data
            ],
            "certifications": [
                {"name": c.get("name"), "issuer": None, "year": c.get("year")}
                for c in cert_data
            ],
            "raw_text":        raw_text,
            "raw_text_length": len(raw_text),
            "parse_time_ms":   round((time.perf_counter()-start)*1000),
        }

        out_path = OUTPUT_DIR / f"{resume_id}_parsed.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, default=str)

        logger.info("Parsed | resume=%s | %dms", resume_id, result["parse_time_ms"])
        await job_queue.update(job_id, JobStatus.DONE, result=result)

    except Exception as e:
        logger.exception("Parse failed | resume=%s", resume_id)
        await job_queue.update(job_id, JobStatus.FAILED, error=str(e))


@router.post("/parse", status_code=202)
async def trigger_parse(body: ParseRequest, background_tasks: BackgroundTasks):
    job = await job_queue.create("parse_resume", {"resume_id": body.resume_id})
    file_path = str(Path("uploads") / f"{body.resume_id}.pdf")
    background_tasks.add_task(_run_parse_job, job.job_id, body.resume_id, file_path, body.job_title)
    return {"job_id": job.job_id, "resume_id": body.resume_id,
            "status": "queued", "message": "Poll /api/parse/status/{job_id}"}

@router.get("/parse/status/{job_id}", response_model=ParseStatusResponse)
async def get_parse_status(job_id: str):
    job = await job_queue.get(job_id)
    if not job: raise JobNotFoundError(job_id)
    return ParseStatusResponse(
        job_id=job_id, status=job.status.value,
        parsed_resume=job.result if job.status == JobStatus.DONE else None,
        error=job.error
    )