import logging
from typing import List, Tuple

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, Query
from sqlalchemy.pool import NullPool
from sqlalchemy.exc import IntegrityError
from sqlalchemy.dialects.postgresql import insert

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

    def get_jobs(
        self,
        filter: list = None,
        order_by: list = None,
        limit: int = 25,
        skip: int = 0,
    ) -> Tuple[int, List[Job]]:
        session: Session = self.SessionLocal()
        try:
            query = session.query(Job)
            if filter:
                for condition in filter:
                    query = query.filter(condition)
            total_count = query.count()
            if order_by:
                for order in order_by:
                    query = query.order_by(order)
            query = query.offset(skip).limit(limit)
            jobs = query.all()
            return total_count, jobs
        except Exception as e:
            logger.error(f"Error retrieving jobs: {e}")
            return 0, []
        finally:
            session.close()

    def save_jobs(self, jobs: List[Job]) -> None:
        """Insert or update a list of Job in the database."""
        if not jobs:
            logger.info("No jobs to save.")
            return
        session = self.SessionLocal()
        try:
            values = [
                {
                    "id": job.id,
                    "title": job.title,
                    "company": job.company,
                    "company_website": job.company_website,
                    "location": job.location,
                    "location_type": job.location_type,
                    "job_url": job.job_url,
                    "description": job.description,
                    "posted_date": job.posted_date,
                    "match_score": job.match_score,
                }
                for job in jobs
            ]
            stmt = insert(Job).values(values)
            stmt = stmt.on_conflict_do_update(
                index_elements=["id"],
                set_={
                    "title": stmt.excluded.title,
                    "company": stmt.excluded.company,
                    "company_website": stmt.excluded.company_website,
                    "location": stmt.excluded.location,
                    "location_type": stmt.excluded.location_type,
                    "job_url": stmt.excluded.job_url,
                    "description": stmt.excluded.description,
                    "scraped_at": stmt.excluded.scraped_at,
                    "match_score": stmt.excluded.match_score,
                },
            )
            session.execute(stmt)
            session.commit()
            logger.info(f"Saved {len(jobs)} jobs to the database.")
        except Exception as e:
            logger.error(f"Failed to save jobs: {e}")
        finally:
            session.close()
