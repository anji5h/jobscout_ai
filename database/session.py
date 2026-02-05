import logging
from typing import List
from concurrent.futures import ThreadPoolExecutor, as_completed

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import NullPool
from sqlalchemy.exc import IntegrityError

from database.models import Base, Job

logger = logging.getLogger(__name__)


class DatabaseManager:
    def __init__(self, database_url: str, max_workers: int = 5):
        self.max_workers = max_workers
        self.engine = create_engine(
            database_url,
            pool_pre_ping=True,
            poolclass=NullPool,
        )
        self.SessionLocal = sessionmaker(
            bind=self.engine,
            expire_on_commit=False,
        )
        Base.metadata.create_all(bind=self.engine)

    def _insert_job(self, job: Job) -> bool:
        """Insert a single job (thread-safe)."""
        try:
            session = self.SessionLocal()
            session.add(job)
            session.commit()
            logger.info(f"Job saved: {job.title} at {job.company}")
            return True
        except IntegrityError as e:
            logger.info("Job already exists, skipping...")
            return True
        except Exception as e:
            logger.error(f"Failed to save job {job.title} at {job.company}: {e}")
            return False
        finally:
            session.close()

    def save_jobs(self, jobs: List[Job]) -> None:
        """Save jobs concurrently using threads."""
        if not jobs:
            logger.info("No jobs to save")
            return

        logger.info(f"Saving {len(jobs)} jobs using {self.max_workers} threads")

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [executor.submit(self._insert_job, job) for job in jobs]

            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    logger.error(f"Unhandled exception during job insert: {e}")
