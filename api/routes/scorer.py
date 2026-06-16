# api/routes/scorer.py — all imports fixed
import json, time, logging
from pathlib import Path
from fastapi import APIRouter
from api.schemas.request_models  import ScoringRequest
from api.schemas.response_models import ScoreResponse, ScoreBreakdown
from api.utils.error_handler     import ResumeNotFoundError, ScoringError

# ── CORRECT IMPORTS ───────────────────────────────────────────────

from scoring.ats_engine          import calculate_ats_score


from ai_engine.semantic_matcher  import get_semantic_score


from ai_engine.bias_checker      import detect_bias_flags


from scoring.score_normalizer    import normalize_score


logger     = logging.getLogger("ats_api.score")
router     = APIRouter()
OUTPUT_DIR = Path("outputs")
STRONG_THRESHOLD   = 75.0
MODERATE_THRESHOLD = 50.0
WEIGHTS = {"skill":0.30,"experience":0.25,"education":0.20,
           "certification":0.10,"semantic":0.15}

def _load_parsed(resume_id):
    p = OUTPUT_DIR / f"{resume_id}_parsed.json"
    if not p.exists(): raise ResumeNotFoundError(resume_id)
    with open(p, encoding="utf-8") as f: return json.load(f)

@router.post("/score", response_model=ScoreResponse)
async def score_resume(body: ScoringRequest):
    start = time.perf_counter()
    try:
        parsed  = _load_parsed(body.resume_id)
        scores  = calculate_ats_score(parsed, body.job_description, body.job_title, WEIGHTS)
        sem = get_semantic_score(parsed.get("raw_text",""), body.job_description)

        # prevent negative semantic scores
        sem = max(0, sem)

        sem_100 = normalize_score(sem)
        flags   = detect_bias_flags(parsed)

        # Blend semantic into final score
        final = round(
            scores["final_score"] * (1 - WEIGHTS["semantic"]) +
            sem_100 * WEIGHTS["semantic"], 2
        )
        decision = ("Strong" if final >= STRONG_THRESHOLD else
                    "Moderate" if final >= MODERATE_THRESHOLD else "Weak")

        logger.info("Scored | %s | %.1f | %s", body.resume_id, final, decision)
        return ScoreResponse(
            resume_id=body.resume_id, job_title=body.job_title,
            final_score=final, decision=decision,
            breakdown=ScoreBreakdown(
                skill_score=        scores["skill_score"],
                experience_score=   scores["experience_score"],
                education_score=    scores["education_score"],
                certification_score=scores["certification_score"],
                semantic_score=     sem_100,
            ),
            bias_flags=flags,
            scoring_time_ms=round((time.perf_counter()-start)*1000)
        )
    except (ResumeNotFoundError, ScoringError): raise
    except Exception as e:
        logger.exception("Scoring failed | %s", body.resume_id)
        raise ScoringError(f"Engine error: {e}", 500, {"resume_id": body.resume_id})