from pathlib import Path
from playwright.async_api import Page
import logging
import asyncio

logger = logging.getLogger(__name__)


class LinkedInAuthenticator:
    def __init__(
        self,
        email: str,
        password: str,
        session_file_path: str,
        login_url: str,
        feed_url: str,
    ):
        self.email = email
        self.password = password
        self.session_path = Path(session_file_path)
        self.login_url = login_url
        self.feed_url = feed_url

    async def authenticate(self, page: Page) -> bool:
        """Authenticate using saved session or fallback to login."""
        try:
            if await self._verify_session(page):
                logger.info("Authenticated using existing session")
                return True
            success = await self._login(page)
            if success:
                await self._save_session(page)
            return success
        except Exception as e:
            logger.error(f"Authentication failed: {e}")
            return False

    async def _login(self, page: Page) -> bool:
        """Login using email and password."""
        try:
            await page.goto(self.login_url, wait_until="load", timeout=10000)
            await asyncio.sleep(1)

            await page.fill("#username", self.email)
            await page.fill("#password", self.password)
            await page.press("#password", "Enter")

            await page.wait_for_load_state("networkidle", timeout=10000)
            await asyncio.sleep(2)

            if "feed" in page.url.lower():
                logger.info("Login successful")
                return True
            logger.error("Login failed")
            return False
        except Exception as e:
            logger.error(f"Login attempt failed: {e}")
            return False

    async def _verify_session(self, page: Page) -> bool:
        """Verify if saved session is still valid."""
        try:
            if not self.session_path.exists():
                return False

            await page.goto(self.feed_url, wait_until="load", timeout=10000)
            await asyncio.sleep(1)

            if "login" in page.url.lower():
                return False

            return True
        except Exception as e:
            logger.error(f"Session verification failed: {e}")
            return False

    async def _save_session(self, page: Page):
        """Save session state to file."""
        try:
            self.session_path.parent.mkdir(parents=True, exist_ok=True)
            await page.context.storage_state(path=str(self.session_path))
        except Exception as e:
            logger.error(f"Failed to save session: {e}")
