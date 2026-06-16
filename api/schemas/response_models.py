from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


# ── Upload ────────────────────────────────────────────────────────
class UploadResponse(BaseModel):
    job_id:      str       # use to poll parse status
    resume_id:   str       # use to score later
    filename:    str
    upload_time: datetime
    status:      str       # "queued"
    message:     str


# ── Parse — sub-pieces ────────────────────────────────────────────
class SkillItem(BaseModel):
    name:       str
    confidence: float = Field(..., ge=0.0, le=1.0)
    category:   Optional[str] = None

class ExperienceItem(BaseModel):
    role:            str
    company:         str
    duration_months: int
    is_relevant:     bool

# REPLACE WITH — make degree and institution Optional:
# FIND THIS:
class EducationItem(BaseModel):
    degree:      str
    institution: str
    year:        Optional[str] = None
    is_relevant: bool

# REPLACE WITH:
class EducationItem(BaseModel):
    degree:      Optional[str] = None
    institution: Optional[str] = None
    year:        Optional[str] = None
    is_relevant: bool = False

class CertificationItem(BaseModel):
    name:   str
    issuer: Optional[str] = None
    year:   Optional[str] = None

class ParsedResumeData(BaseModel):
    resume_id:               str
    candidate_name:          Optional[str] = None
    email:                   Optional[str] = None
    phone:                   Optional[str] = None
    skills:                  list[SkillItem]
    experience:              list[ExperienceItem]
    total_experience_months: int
    education:               list[EducationItem]
    certifications:          list[CertificationItem]
    raw_text_length:         int
    parse_time_ms:           int


# ── Parse status ──────────────────────────────────────────────────
class ParseStatusResponse(BaseModel):
    job_id:        str
    status:        str                         # queued|processing|done|failed
    parsed_resume: Optional[ParsedResumeData] = None
    error:         Optional[str]              = None


# ── Score ─────────────────────────────────────────────────────────
class ScoreBreakdown(BaseModel):
    skill_score:         float = Field(..., ge=0, le=100)
    experience_score:    float = Field(..., ge=0, le=100)
    education_score:     float = Field(..., ge=0, le=100)
    certification_score: float = Field(..., ge=0, le=100)
    semantic_score:      float = Field(..., ge=0, le=100)

class ScoreResponse(BaseModel):
    resume_id:       str
    job_title:       str
    final_score:     float = Field(..., ge=0, le=100)
    decision:        str   # Strong | Moderate | Weak
    breakdown:       ScoreBreakdown
    bias_flags:      list[str] = []
    scoring_time_ms: int


# ── Shortlist ─────────────────────────────────────────────────────
class RankedCandidate(BaseModel):
    rank:           int
    resume_id:      str
    candidate_name: Optional[str] = None
    final_score:    float
    decision:       str
    breakdown:      dict
    bias_flags:     list[str] = []

class ShortlistResponse(BaseModel):
    job_title:          str
    total_processed:    int
    shortlisted_count:  int
    processing_time_ms: int
    candidates:         list[RankedCandidate]


# ── Error (standard shape for all errors) ─────────────────────────
class ErrorResponse(BaseModel):
    error:   str
    message: str
    detail:  dict = {}