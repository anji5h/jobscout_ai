import shutil
import logging
from pathlib import Path
from datetime import datetime, timezone
from typing import List, Optional

from fastapi import (
    FastAPI,
    UploadFile,
    File,
    HTTPException,
    Query,
    Request,
)
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.service import db_manager
from database.models import Job

logger = logging.getLogger(__name__)

app = FastAPI(
    title="JobScout AI API",
    description="LinkedIn Job Scraper with CV Matching",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.exception("Unhandled exception", extra={"path": request.url.path})
    return JSONResponse(
        status_code=500,
        content={"status": "error", "detail": "Internal server error"},
    )


@app.get("/health", tags=["system"])
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "service": "jobscout-ai-api",
    }


async def save_uploaded_file(
    file: UploadFile,
    allowed_ext: str,
    destination: Path,
    label: str,
):
    file_ext = Path(file.filename).suffix.lower()

    if file_ext != allowed_ext:
        raise HTTPException(
            status_code=400,
            detail=f"Only {allowed_ext.upper()} files are allowed.",
        )

    try:
        if destination.exists():
            destination.unlink()

        with destination.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        logger.info("%s uploaded successfully", label)

        return {"status": "success", "message": f"{label} uploaded successfully"}

    except Exception:
        logger.exception("Failed to upload %s", label)
        raise HTTPException(status_code=500, detail=f"Failed to upload {label}")

    finally:
        await file.close()


@app.post("/upload-cv", tags=["files"])
async def upload_cv(file: UploadFile = File(...)):
    return await save_uploaded_file(
        file=file,
        allowed_ext=".pdf",
        destination=Path(settings.cv_file_path),
        label="CV",
    )


@app.post("/upload-prompt", tags=["files"])
async def upload_prompt(file: UploadFile = File(...)):
    return await save_uploaded_file(
        file=file,
        allowed_ext=".txt",
        destination=Path(settings.prompt_file_path),
        label="Prompt",
    )


@app.get("/jobs", tags=["jobs"])
async def get_jobs(
    limit: int = Query(25, ge=1, le=100),
    skip: int = Query(0, ge=0),
    match_score: bool = Query(True),
    title: Optional[str] = Query(None),
    location: Optional[str] = Query(None),
):
    try:
        filters: List = []

        if match_score:
            filters.append(Job.match_score.isnot(None))

        if title:
            filters.append(Job.title.ilike(f"%{title}%"))

        if location:
            filters.append(Job.location.ilike(f"%{location}%"))

        total_count, jobs = db_manager.get_jobs(
            filter=filters,
            order_by=[Job.match_score.desc(), Job.scraped_at.desc()],
            limit=limit,
            skip=skip,
        )

        return {
            "status": "success",
            "meta": {
                "page": (skip // limit) + 1,
                "page_size": limit,
                "total_results": total_count,
                "total_pages": (total_count + limit - 1) // limit,
            },
            "data": jobs,
        }

    except Exception:
        logger.exception("Error retrieving jobs")
        raise HTTPException(status_code=500, detail="Failed to retrieve jobs")
