import uuid, asyncio
from datetime import datetime
from typing import Any, Optional
from enum import Enum


class JobStatus(str, Enum):
    QUEUED     = "queued"
    PROCESSING = "processing"
    DONE       = "done"
    FAILED     = "failed"


class Job:
    def __init__(self, job_type: str, payload: dict):
        self.job_id:     str            = str(uuid.uuid4())
        self.job_type:   str            = job_type
        self.payload:    dict           = payload
        self.status:     JobStatus      = JobStatus.QUEUED
        self.result:     Any            = None
        self.error:      Optional[str]  = None
        self.created_at: datetime       = datetime.utcnow()
        self.updated_at: datetime       = datetime.utcnow()


class JobQueue:
    def __init__(self):
        self._store: dict[str, Job] = {}
        self._lock = asyncio.Lock()

    async def create(self, job_type: str, payload: dict) -> Job:
        job = Job(job_type, payload)
        async with self._lock:
            self._store[job.job_id] = job
        return job

    async def get(self, job_id: str) -> Optional[Job]:
        return self._store.get(job_id)

    async def update(self, job_id: str, status: JobStatus,
                      result: Any = None, error: str = None):
        async with self._lock:
            job = self._store.get(job_id)
            if job:
                job.status = status; job.result = result
                job.error  = error;  job.updated_at = datetime.utcnow()


# Single shared instance — import everywhere:
# from api.utils.async_jobs import job_queue, JobStatus
job_queue = JobQueue()