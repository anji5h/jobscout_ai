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
    task_time_limit=1800,
    task_soft_time_limit=1500,
)


@app.on_after_configure.connect
def trigger_startup_tasks(sender, **kwargs):
    sender.send_task("app.tasks.scrape_linkedin_jobs_task")
    sender.send_task(
        "app.tasks.process_jobs", countdown=300
    )  # Delay to allow scraping to finish


app.conf.beat_schedule = {
    "scrape-linkedin-jobs-hourly": {
        "task": "app.tasks.scrape_linkedin_jobs_task",
        "schedule": crontab(minute="0", hour="8,14,20"),  # Run at 8am, 2pm, and 8pm UTC
    },
    "process-jobs-hourly": {
        "task": "app.tasks.process_jobs",
        "schedule": crontab(minute="*/30"),  # Run every 30 minutes to process new jobs
    },
}
