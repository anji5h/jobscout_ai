import asyncio
import logging
from playwright.async_api import async_playwright

from app.celery_app import app
from app.config import settings
from database.session import DatabaseManager
from datetime import datetime, timezone
from linkedin.scraper import LinkedInJobScraper
from linkedin.auth import LinkedInAuthenticator

logger = logging.getLogger(__name__)

CONTEXT_ARGS = {
    "user_agent": settings.user_agent,
    "viewport": {"width": 1280, "height": 800},
}

authenticator = LinkedInAuthenticator(
    email=settings.linkedin_username,
    password=settings.linkedin_password,
    login_url=settings.lki_login_url,
    feed_url=settings.lki_feed_url,
    context_args=CONTEXT_ARGS,
    session_file_path=settings.session_file_path,
)

scraper = LinkedInJobScraper(
    jobs_search_url=settings.lki_job_search_url,
)

db_manager = DatabaseManager(database_url=settings.database_url)


@app.task(bind=True, max_retries=3)
def scrape_linkedin_jobs_task(self):
    """
    Main task to scrape LinkedIn jobs, parse them, and persist to database.
    Runs on schedule via Celery Beat.
    """
    try:
        logger.info(f"Starting job scraping task (attempt {self.request.retries + 1})")

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        jobs = loop.run_until_complete(_scrape_and_persist())

        logger.info(f"Task completed successfully.")
        return {
            "status": "success",
            "jobs_processed": len(jobs),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
    except Exception as exc:
        logger.error(f"Task failed with error: {exc}")
        raise self.retry(exc=exc, countdown=60 * (2**self.request.retries))


async def _scrape_and_persist():
    """Async helper function for scraping and persisting jobs."""
    try:
        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch(headless=True)
            context = await authenticator.get_context(browser)
            page = await context.new_page()
            jobs = await scraper.scrape_jobs(page)
            db_manager.save_jobs(jobs)
            await context.close()
            await browser.close()
            return jobs
    except Exception as e:
        logger.error(f"Error during scraping and persistence: {e}")
        raise
