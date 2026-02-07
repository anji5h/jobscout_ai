import asyncio
import logging
from datetime import datetime, timezone
from playwright.async_api import async_playwright

from app.celery import app
from app.service import auth_provider, scraper, db_manager

logger = logging.getLogger(__name__)


@app.task(bind=True, max_retries=3)
def scrape_linkedin_jobs_task(self):
    """
    Main task to scrape LinkedIn jobs, parse them, and persist to database.
    Runs on schedule via Celery Beat.
    """
    try:
        logger.info(f"Starting job scraping task (attempt {self.request.retries + 1})")

        jobs = asyncio.run(_scrape_and_persist())

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
            context = await auth_provider.get_auth_context(browser)
            page = await context.new_page()
            jobs = await scraper.scrape_jobs(page)
            db_manager.save_jobs(jobs)
            await context.close()
            await browser.close()
            return jobs
    except Exception as e:
        logger.error(f"Error during scraping and persistence: {e}")
        raise
