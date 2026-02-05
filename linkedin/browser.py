import os
import logging
from playwright.async_api import async_playwright, Browser, BrowserContext, Page

logger = logging.getLogger(__name__)


class BrowserManager:
    def __init__(self, storage_state_path: str, headless: bool = True):
        self.headless = headless
        self.storage_state_path = storage_state_path
        self.playwright = None
        self.browser: Browser | None = None
        self.context: BrowserContext | None = None

    async def _launch(self) -> None:
        """Launch Playwright and browser."""
        try:
            if self.playwright:
                return

            self.playwright = await async_playwright().start()
            self.browser = await self.playwright.chromium.launch(headless=self.headless)

            logger.info(f"Browser launched (headless={self.headless})")

        except Exception:
            logger.exception("Failed to launch browser")
            raise

    async def _create_context(self) -> None:
        """Create browser context with optional session restoration."""
        try:
            if not self.browser:
                await self._launch()

            context_args = {
                "user_agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/120.0.0.0 Safari/537.36"
                ),
                "viewport": {"width": 1280, "height": 800},
            }

            if os.path.exists(self.storage_state_path):
                self.context = await self.browser.new_context(
                    storage_state=self.storage_state_path, **context_args
                )
            else:
                self.context = await self.browser.new_context(**context_args)
            logger.info("Browser context created")
        except Exception:
            logger.exception("Failed to create browser context")
            raise

    async def new_page(self) -> Page:
        """Create a new page in the active context."""
        try:
            if not self.context:
                await self._create_context()

            page = await self.context.new_page()
            logger.info("New page created")
            return page
        except Exception:
            logger.exception("Failed to create new page")
            raise

    async def close(self) -> None:
        """Gracefully shutdown context, browser, and Playwright."""
        try:
            if self.context:
                await self.context.close()
                logger.info("Context closed")
            if self.browser:
                await self.browser.close()
                logger.info("Browser closed")
            if self.playwright:
                await self.playwright.stop()
                logger.info("Playwright stopped")
        except Exception:
            logger.exception("Error during browser shutdown")
            raise
