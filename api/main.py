from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import upload, parse, scorer, shortlist

from api.utils.error_handler import (
    ATSBaseException, ats_exception_handler,
    generic_exception_handler, setup_logging,
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    print("✅  ATS API ready — http://localhost:8000/docs")
    yield
    print("🛑  Shutting down")

app = FastAPI(title="ATS Resume Screening API", version="1.0.0",
              docs_url="/docs", lifespan=lifespan)
app.add_middleware(CORSMiddleware, allow_origins=["*"],
                   allow_methods=["*"], allow_headers=["*"])
app.add_exception_handler(ATSBaseException, ats_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

app.include_router(upload.router,   prefix="/api", tags=["1. Upload"])
app.include_router(parse.router,    prefix="/api", tags=["2. Parse"])

app.include_router(scorer.router,   prefix="/api", tags=["3. Score"])

app.include_router(shortlist.router,prefix="/api", tags=["4. Shortlist"])

@app.get("/health", tags=["System"])
async def health(): return {"status":"healthy","version":"1.0.0"}