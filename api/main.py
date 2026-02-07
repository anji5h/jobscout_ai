import shutil
import logging
from pathlib import Path
from datetime import datetime, timezone
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File, HTTPException, Query

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
)


@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler for unhandled errors."""
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"status": "error", "detail": "Internal server error"},
    )


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "service": "jobscout-ai-api",
    }


@app.post("/upload-cv")
async def upload_cv(file: UploadFile = File(...)):
    """
    Upload a CV file and save it with a fixed name.
    Existing file will be replaced.
    """
    file_ext = Path(file.filename).suffix.lower()

    if file_ext != ".pdf":
        raise HTTPException(
            status_code=400,
            detail="File type not allowed. Only PDF files are allowed.",
        )

    file_path = Path(settings.cv_file_path)

    try:
        if file_path.exists():
            file_path.unlink()

        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        logger.info(f"CV uploaded to {file_path}")

        return {
            "status": "success",
            "message": f"CV uploaded successfully",
        }
    except Exception as e:
        logger.error(f"Error saving CV: {e}")
        raise HTTPException(status_code=500, detail="Failed to upload CV")
    finally:
        await file.close()


@app.get("/jobs")
async def get_jobs(
    limit: int = Query(25, description="Number of jobs to return"),
    skip: int = Query(0, description="Number of jobs to skip for pagination"),
    match_score: bool = Query(
        True, description="Filter jobs with non-null match_score"
    ),
    title: str = Query(None, description="Filter jobs by title"),
    location: str = Query(None, description="Filter jobs by location"),
):
    """
    Retrieve jobs with match scores (non-null match_score values).

    Args:
        limit: Number of jobs to return (default 25)
        skip: Number of jobs to skip for pagination (default 0)

    Returns:
        List of jobs sorted by match_score descending and then by scraped date descending
    """
    try:
        filters = []
        if match_score:
            filters.append(Job.match_score != None)
        if title:
            filters.append(Job.title.like(f"%{title}%"))
        if location:
            filters.append(Job.location.like(f"%{location}%"))

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
    except Exception as e:
        logger.error(f"Error retrieving matched jobs: {e}")
        raise HTTPException(status_code=500, detail="Failed to retrieve jobs")
