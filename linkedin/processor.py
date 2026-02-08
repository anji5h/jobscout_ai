import os
import re
import logging
from pathlib import Path
from typing import List, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed

from pypdf import PdfReader
from huggingface_hub import InferenceClient

from database.models import Job

logger = logging.getLogger(__name__)


class JobProcessor:
    def __init__(self, hf_token: str, hf_model: str, cv_path: str, prompt_path: str):
        self.hf_cli = InferenceClient(api_key=hf_token)
        self.hf_model = hf_model
        self.cv_path = Path(cv_path)
        self.prompt_path = Path(prompt_path)

        self.workers = min(8, os.cpu_count() or 4)

        self._cv_text: Optional[str] = None
        self._prompt: Optional[str] = None

    def process_job(self, jobs: List[Job]) -> List[Job]:
        if not jobs:
            logger.info("No jobs to process")
            return []

        cv_text = self._load_cv()
        prompt = self._load_prompt()

        if not cv_text or not prompt:
            logger.warning("Missing CV text or prompt; skipping processing")
            return []

        processed_jobs: List[Job] = []

        with ThreadPoolExecutor(max_workers=self.workers) as executor:
            futures = {
                executor.submit(self._process_single_job, job, cv_text, prompt): job
                for job in jobs
            }

            for future in as_completed(futures):
                job = futures[future]
                try:
                    result = future.result()
                    if result:
                        processed_jobs.append(result)
                except Exception:
                    logger.exception(f"Unhandled error processing job {job.id}")

        return processed_jobs

    def _process_single_job(self, job: Job, cv_text: str, prompt: str) -> Optional[Job]:
        try:
            input_text = prompt.replace("{{cv_text}}", cv_text).replace(
                "{{job_description}}", job.description
            )

            response = self.hf_cli.chat.completions.create(
                model=self.hf_model,
                messages=[{"role": "user", "content": input_text}],
                temperature=0,
            )

            job.match_score = int(response.choices[0].message.content)
            return job

        except Exception:
            logger.exception(f"Error processing job {job.id}")
            return None

    def _load_cv(self) -> Optional[str]:
        if self._cv_text is not None:
            return self._cv_text

        if not self.cv_path.exists():
            logger.warning(f"CV file not found: {self.cv_path}")
            return None

        try:
            text_parts = []
            reader = PdfReader(str(self.cv_path))
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text_parts.append(page_text)

            self._cv_text = "\n".join(text_parts).strip()
            return self._cv_text

        except Exception:
            logger.exception("Error extracting text from CV PDF")
            return None

    def _load_prompt(self) -> Optional[str]:
        if self._prompt is not None:
            return self._prompt

        if not self.prompt_path.exists():
            logger.warning(f"Prompt file not found: {self.prompt_path}")
            return None

        try:
            self._prompt = self.prompt_path.read_text(encoding="utf-8")
            return self._prompt
        except Exception:
            logger.exception("Error loading prompt file")
            return None
