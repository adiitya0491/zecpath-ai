import json, time, asyncio, logging
from pathlib import Path
from fastapi import APIRouter
from api.schemas.request_models  import ShortlistRequest
from api.schemas.response_models import ShortlistResponse, RankedCandidate
from scoring.ats_engine import calculate_ats_score
from ai_engine.semantic_matcher import get_semantic_score
from ai_engine.bias_checker import detect_bias_flags
from scoring.score_normalizer import normalize_score

logger     = logging.getLogger("ats_api.shortlist")
router     = APIRouter()
OUTPUT_DIR = Path("outputs")
STRONG_THRESHOLD   = 75.0
MODERATE_THRESHOLD = 50.0
WEIGHTS = {"skill":0.30,"experience":0.25,"education":0.20,
           "certification":0.10,"semantic":0.15}


async def _score_one(resume_id: str, job_description: str, job_title: str) -> dict | None:
    """Score one resume. Returns None on failure — batch keeps going."""
    try:
        path = OUTPUT_DIR / f"{resume_id}_parsed.json"

        print("Resume ID:", resume_id)
        print("Path:", path)
        print("Exists:", path.exists())

        if not path.exists():
            logger.warning("Skipping %s — not parsed", resume_id)
            return None
        with open(path) as f: parsed = json.load(f)


        scores = calculate_ats_score(parsed, job_description, job_title, WEIGHTS)
        sem = get_semantic_score(
            parsed.get("raw_text", ""),
            job_description
        )

        if sem < 0:
            sem = 0

        sem_100 = normalize_score(sem)
        flags  = detect_bias_flags(parsed)
        final = round(
            scores["final_score"] * (1 - WEIGHTS["semantic"]) +
            sem_100 * WEIGHTS["semantic"],
            2
        )
        decision = ("Strong" if final >= STRONG_THRESHOLD else
                    "Moderate" if final >= MODERATE_THRESHOLD else "Weak")
        return {
            "resume_id":resume_id, "candidate_name":parsed.get("candidate_name"),
            "final_score":final, "decision":decision, "bias_flags":flags,
            "breakdown":{"skill_score":scores["skill_score"],
                          "experience_score":scores["experience_score"],
                          "education_score":scores["education_score"],
                          "certification_score":scores["certification_score"],
                          "semantic_score": round(sem_100,2)},
        }
    except Exception as e:
        print("ERROR:", e)
        raise


@router.post("/shortlist", response_model=ShortlistResponse,
             summary="Rank multiple resumes for a job")
async def shortlist_candidates(body: ShortlistRequest):
    start   = time.perf_counter()
    results = await asyncio.gather(*[
        _score_one(rid, body.job_description, body.job_title)
        for rid in body.resume_ids
    ])
    scored  = [r for r in results if r]
    scored.sort(key=lambda x: x["final_score"], reverse=True)
    top = scored[:body.top_n]
    logger.info("Shortlist | %d processed | %d returned", len(scored), len(top))
    return ShortlistResponse(
        job_title=body.job_title, total_processed=len(scored),
        shortlisted_count=len(top),
        processing_time_ms=round((time.perf_counter()-start)*1000),
        candidates=[
            RankedCandidate(rank=i+1, resume_id=c["resume_id"],
                            candidate_name=c.get("candidate_name"),
                            final_score=c["final_score"], decision=c["decision"],
                            breakdown=c["breakdown"], bias_flags=c.get("bias_flags",[]))
            for i, c in enumerate(top)
        ]
    )