import logging
from typing import List

from playwright.async_api import Page
from bs4 import BeautifulSoup

from database.models import Job

logger = logging.getLogger(__name__)


class LinkedInJobScraper:
    def __init__(self, jobs_search_url: str):
        self.jobs_url = jobs_search_url

    async def scrape_jobs(self, page: Page) -> List[Job]:
        jobs: List[Job] = []

        try:
            await page.goto(self.jobs_url, wait_until="load", timeout=120000)
            await page.wait_for_timeout(2000)

            job_list = await page.locator("li.scaffold-layout__list-item").all()

            logger.info(f"Found {len(job_list)} jobs on the page")

            for job in job_list:
                try:
                    job_id = await job.get_attribute(
                        "data-occludable-job-id", timeout=120000
                    )
                    if not job_id:
                        continue

                    await job.click()
                    await page.wait_for_timeout(2000)

                    job_details_html = await page.locator(
                        "div.jobs-search__job-details"
                    ).inner_html(timeout=120000)
                    soup = BeautifulSoup(job_details_html, "html.parser")

                    job_el = soup.select_one(
                        "div.job-details-jobs-unified-top-card__job-title a"
                    )
                    if not job_el:
                        logger.warning(
                            f"Job title element not found for job ID {job_id}"
                        )
                        continue
                    job_title = job_el.get_text(strip=True)
                    job_url = job_el.get("href")

                    company_el = soup.select_one(
                        "div.job-details-jobs-unified-top-card__company-name a"
                    )
                    if not company_el:
                        logger.warning(f"Company element not found for job ID {job_id}")
                        continue
                    company = company_el.get_text(strip=True)
                    company_website = company_el.get("href")

                    description_el = soup.select_one(
                        "article.jobs-description__container"
                    )
                    if not description_el:
                        logger.warning(
                            f"Description element not found for job ID {job_id}"
                        )
                        continue

                    job_description = description_el.get_text(
                        separator="\n", strip=True
                    )

                    insights_el = soup.select(
                        "div.job-details-fit-level-preferences button"
                    )
                    location_type = "unknown"
                    for el in insights_el:
                        text = el.get_text(strip=True).lower()
                        if "on-site" in text or "remote" in text or "hybrid" in text:
                            location_type = text
                            break

                    meta_el = soup.select(
                        ".job-details-jobs-unified-top-card__tertiary-description-container span.tvm__text"
                    )

                    if len(meta_el) == 0:
                        logger.warning(f"Meta elements not found for job ID {job_id}")
                        continue
                    job_location = meta_el[0].get_text(strip=True)
                    posted_date = (
                        meta_el[2].get_text(strip=True) if len(meta_el) > 2 else None
                    )

                    jobs.append(
                        Job(
                            id=job_id,
                            title=job_title,
                            company=company,
                            company_website=company_website,
                            location=job_location,
                            location_type=location_type,
                            job_url=job_url,
                            description=job_description,
                            posted_date=posted_date,
                        )
                    )

                except Exception as job_err:
                    logger.warning(f"Failed to scrape job with ID {job_id}: {job_err}")
                    continue

            logger.info(f"Successfully scraped {len(jobs)} jobs")
            return jobs

        except Exception as e:
            logger.error(f"Error during job scraping: {e}")
            return jobs
