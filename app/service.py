from app.config import settings

from database.session import DatabaseManager
from linkedin.processor import JobProcessor
from linkedin.scraper import LinkedInJobScraper
from linkedin.auth import LinkedInAuthenticator

auth_provider = LinkedInAuthenticator(
    email=settings.linkedin_username,
    password=settings.linkedin_password,
    login_url=settings.lki_login_url,
    feed_url=settings.lki_feed_url,
    user_agent=settings.user_agent,
    session_path=settings.session_file_path,
)

scraper = LinkedInJobScraper(
    jobs_search_url=settings.lki_job_search_url,
)

db_manager = DatabaseManager(database_url=settings.database_url)

job_processor = JobProcessor(
    hf_token=settings.hf_token,
    hf_model=settings.hf_model,
    cv_path=settings.cv_file_path,
    prompt_path=settings.prompt_file_path,
)
