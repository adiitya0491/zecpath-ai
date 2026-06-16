from fastapi import Request
from fastapi.responses import JSONResponse
import logging

logger = logging.getLogger("ats_api")


# ── Custom Exception Classes ──────────────────────────────────────
class ATSBaseException(Exception):
    def __init__(self, message: str, status_code: int = 400, detail: dict = None):
        self.message     = message
        self.status_code = status_code
        self.detail      = detail or {}
        super().__init__(message)

class UploadError(ATSBaseException):
    """Wrong file type, too large, etc."""

class ResumeParseError(ATSBaseException):
    """AI parsing engine failed"""

class ScoringError(ATSBaseException):
    """ATS scoring engine failed"""

class JobNotFoundError(ATSBaseException):
    def __init__(self, job_id: str):
        super().__init__(
            message=f"Job '{job_id}' not found. Check the job_id.",
            status_code=404, detail={"job_id": job_id}
        )

class ResumeNotFoundError(ATSBaseException):
    def __init__(self, resume_id: str):
        super().__init__(
            message=f"Resume '{resume_id}' not parsed yet. Run /api/parse first.",
            status_code=404, detail={"resume_id": resume_id}
        )


# ── Global Exception Handlers ─────────────────────────────────────
# Register both in main.py with app.add_exception_handler()
async def ats_exception_handler(request: Request, exc: ATSBaseException):
    logger.error("ATS Error: %s | %s", exc.message, exc.detail)
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.__class__.__name__,
                 "message": exc.message, "detail": exc.detail}
    )

async def generic_exception_handler(request: Request, exc: Exception):
    logger.exception("Unhandled exception at %s", request.url.path)
    return JSONResponse(
        status_code=500,
        content={"error": "InternalServerError",
                 "message": "Unexpected error. Check server logs.",
                 "detail": {}}
    )

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )