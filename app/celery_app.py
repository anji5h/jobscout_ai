from celery import Celery
from celery.schedules import crontab
from app.config import settings
import logging

logger = logging.getLogger(__name__)

app = Celery("jobscout_ai", include=["app.tasks"])

app.conf.update(
    broker_url=settings.celery_broker_url,
    result_backend=settings.celery_result_backend,
    timezone="UTC",
    enable_utc=True,
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    task_track_started=True,
    task_time_limit=600,
    task_soft_time_limit=540,
)

app.conf.beat_schedule = {
    "scrape-linkedin-jobs-hourly": {
        "task": "app.tasks.scrape_linkedin_jobs_task",
        "schedule": crontab(minute=0, hour="*/1"),  # Every 1 hour
    },
}
