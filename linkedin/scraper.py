import logging
from typing import List, Optional

from playwright.async_api import Page, Locator, TimeoutError as PlaywrightTimeoutError
from bs4 import BeautifulSoup

from database.models import Job

logger = logging.getLogger(__name__)


class LinkedInJobScraper:
    def __init__(self, jobs_search_url: str):
        self.jobs_url = jobs_search_url

    async def scrape_jobs(self, page: Page) -> List[Job]:
        """
        Scrape LinkedIn job listings from the provided search URL.

        Args:
            page: Playwright Page instance
            max_jobs: Maximum number of jobs to scrape (helps with rate limiting / timeouts)

        Returns:
            List of Job model instances
        """
        jobs = []
        try:
            await page.goto(self.jobs_url, wait_until="domcontentloaded", timeout=90000)
            await page.wait_for_selector(
                "li.scaffold-layout__list-item", state="attached", timeout=90000
            )
            job_elements = await page.locator("li.scaffold-layout__list-item").all()
            logger.info(f"Found {len(job_elements)} job cards on the page")

            for job_li in job_elements:
                try:
                    job_card = await self._extract_job_card_data(page, job_li)
                    if job_card:
                        jobs.append(job_card)

                except Exception as e:
                    logger.warning(f"Failed to process a job: {e}", exc_info=False)
                    continue
            logger.info(f"Successfully scraped {len(jobs)} jobs")
            return jobs
        except Exception as e:
            logger.error(f"Critical error during LinkedIn scraping: {e}", exc_info=True)
            return jobs

    async def _extract_job_card_data(
        self, page: Page, job_li: Locator
    ) -> Optional[Job]:
        """Extract data from one job card and detail pane"""
        try:
            job_id = await job_li.get_attribute("data-occludable-job-id")
            if not job_id:
                return None

            await job_li.click(timeout=90000)

            await page.wait_for_selector(
                "div.jobs-search__job-details article.jobs-description__container",
                timeout=90000,
                state="attached",
            )

            details_html = await page.locator(
                "div.jobs-search__job-details"
            ).inner_html()
            soup = BeautifulSoup(details_html, "html.parser")

            # Title & URL
            title_a = soup.select_one(
                "div.job-details-jobs-unified-top-card__job-title a"
            )
            if not title_a:
                return None

            title = title_a.get_text(strip=True)
            job_url = title_a.get("href", "")

            # Company
            company_a = soup.select_one(
                "div.job-details-jobs-unified-top-card__company-name a"
            )
            if not company_a:
                return None

            company = company_a.get_text(strip=True)
            company_url = company_a.get("href", "")

            # Description
            desc_container = soup.select_one("article.jobs-description__container")
            description = (
                desc_container.get_text(separator="\n", strip=True)
                if desc_container
                else ""
            )

            # Location type (on-site / hybrid / remote / internship)
            location_type = "unknown"
            for btn in soup.select("div.job-details-fit-level-preferences button"):
                text = btn.get_text(strip=True).lower()
                if any(
                    word in text
                    for word in ["on-site", "remote", "hybrid", "internship"]
                ):
                    location_type = text
                    break

            # Location & posted date
            meta_spans = soup.select(
                ".job-details-jobs-unified-top-card__tertiary-description-container "
                "span.tvm__text"
            )

            location = meta_spans[0].get_text(strip=True) if len(meta_spans) > 0 else ""
            posted_date = (
                meta_spans[2].get_text(strip=True) if len(meta_spans) > 2 else None
            )

            return Job(
                id=job_id,
                title=title.lower(),
                company=company.lower(),
                company_website=company_url,
                location=location.lower(),
                location_type=location_type,
                job_url=job_url,
                description=description,
                posted_date=posted_date,
                match_score=None,
            )

        except PlaywrightTimeoutError as te:
            logger.debug(f"Timeout while processing job: {te}")
            return None
        except Exception as e:
            logger.warning(f"Unexpected error in job: {e}")
            return None
