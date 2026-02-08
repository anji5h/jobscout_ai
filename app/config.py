from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    linkedin_username: str = Field(..., env="LINKEDIN_USERNAME")
    linkedin_password: str = Field(..., env="LINKEDIN_PASSWORD")
    postgres_user: str = Field("postgres", env="POSTGRES_USER")
    hf_token: str = Field(..., env="HF_TOKEN")
    hf_model: str = Field(..., env="HF_MODEL")
    postgres_password: str = Field("postgres", env="POSTGRES_PASSWORD")
    postgres_host: str = Field("postgres", env="POSTGRES_HOST")
    postgres_port: int = Field(5432, env="POSTGRES_PORT")
    postgres_db: str = Field("jobscout_ai", env="POSTGRES_DB")
    redis_url: str = Field("redis://redis:6379/0", env="REDIS_URL")
    base_url: str = Field("https://www.linkedin.com", env="BASE_URL")
    login_url: str = Field("/uas/login", env="LOGIN_URL")
    feed_url: str = Field("/feed", env="FEED_URL")
    job_search_url: str = Field("/jobs/search/?", env="JOB_SEARCH_URL")
    job_search_params: str = Field(
        "geoId=102974008&keywords=junior software engineer&refresh=true",
        env="JOB_SEARCH_PARAMS",
    )
    user_agent: str = Field(
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        env="USER_AGENT",
    )
    session_file_path: str = Field("/data/session.json", env="SESSION_FILE_PATH")
    cv_file_path: str = Field("/data/resume.pdf", env="CV_FILE_PATH")
    prompt_file_path: str = Field("/data/prompt.txt", env="PROMPT_FILE_PATH")

    class Config:
        case_sensitive = False

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg2://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )

    @property
    def celery_broker_url(self) -> str:
        return self.redis_url

    @property
    def celery_result_backend(self) -> str:
        return self.redis_url

    @property
    def lki_login_url(self) -> str:
        return f"{self.base_url}{self.login_url}"

    @property
    def lki_feed_url(self) -> str:
        return f"{self.base_url}{self.feed_url}"

    @property
    def lki_job_search_url(self) -> str:
        return f"{self.base_url}{self.job_search_url}{self.job_search_params}"


settings = Settings()
