from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timezone

Base = declarative_base()


class Job(Base):
    __tablename__ = "jobs"

    id = Column(String(15), primary_key=True)
    title = Column(String(100), nullable=False)
    company = Column(String(100), nullable=False)
    company_website = Column(String(255), nullable=True)
    location = Column(String(255), nullable=False)
    location_type = Column(String(255), nullable=True)
    job_url = Column(Text, nullable=True)
    description = Column(Text, nullable=False)
    posted_date = Column(String(255), nullable=True)
    match_score = Column(Integer, nullable=True)
    scraped_at = Column(DateTime, nullable=False, default=datetime.now(tz=timezone.utc))

    def __repr__(self):
        return f"<Job(id={self.id}, title={self.title}, company={self.company})>"
