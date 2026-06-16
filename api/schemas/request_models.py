from pydantic import BaseModel, Field
from typing import Optional


# Used by: POST /api/score
class ScoringRequest(BaseModel):
    resume_id:       str = Field(..., min_length=1,
                         description="resume_id returned after parsing")
    job_title:       str = Field(..., min_length=2)
    job_description: str = Field(..., min_length=50,
                         description="Full JD text — min 50 chars for meaningful match")


# Used by: POST /api/shortlist
class ShortlistRequest(BaseModel):
    job_title:       str       = Field(..., min_length=2)
    job_description: str       = Field(..., min_length=50)
    resume_ids:      list[str] = Field(..., min_length=1, max_length=500)
    top_n:           int       = Field(default=10, ge=1, le=500)


# Used by: POST /api/parse
class ParseRequest(BaseModel):
    resume_id: str = Field(..., min_length=1)
    job_title: str = Field(..., min_length=2)