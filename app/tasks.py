import asyncio
import logging
from app.celery_app import app
from app.config import settings
from database.session import DatabaseManager
from datetime import datetime, timezone
from linkedin.browser import BrowserManager
from linkedin.scraper import LinkedInJobScraper
from linkedin.auth import LinkedInAuthenticator

logger = logging.getLogger(__name__)

browser_manager = BrowserManager(
    headless=settings.headless, storage_state_path=settings.session_file_path
)
authenticator = LinkedInAuthenticator(
    email=settings.linkedin_username,
    password=settings.linkedin_password,
    session_file_path=settings.session_file_path,
    login_url=settings.lki_login_url,
    feed_url=settings.lki_feed_url,
)
scraper = LinkedInJobScraper(
    jobs_search_url=settings.lki_job_search_url,
)

db_manager = DatabaseManager(database_url=settings.database_url)
db_manager.init_db()


@app.task(bind=True, max_retries=3)
def scrape_linkedin_jobs_task(self):
    """
    Main task to scrape LinkedIn jobs, parse them, and persist to database.
    Runs on schedule via Celery Beat.
    """
    try:
        logger.info(f"Starting job scraping task (attempt {self.request.retries + 1})")

        jobs = asyncio.run(_async_scrape_and_persist())

        logger.info(f"Task completed successfully. Scraped and saved {len(jobs)} jobs.")
        return {
            "status": "success",
            "jobs_processed": len(jobs),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
    except Exception as exc:
        logger.error(f"Task failed with error: {exc}")
        raise self.retry(exc=exc, countdown=60 * (2**self.request.retries))


async def _async_scrape_and_persist():
    """Async helper function for scraping and persisting jobs."""

    try:
        page = await browser_manager.new_page()
        auth_success = await authenticator.authenticate(page)

        if not auth_success:
            logger.error("Authentication failed, aborting task")
            return []

        jobs = await scraper.scrape_jobs(page)
        db_manager.save_jobs(jobs)
        return jobs
    except Exception as e:
        logger.error(f"Error during scraping and persistence: {e}")
        raise
    finally:
        await browser_manager.close()
