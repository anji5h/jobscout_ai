import os
import re
import logging
from playwright.async_api import Browser, BrowserContext

logger = logging.getLogger(__name__)


class LinkedInAuthenticator:
    def __init__(
        self,
        email: str,
        password: str,
        login_url: str,
        feed_url: str,
        context_args: dict,
        session_file_path: str,
    ):
        self.email = email
        self.password = password
        self.login_url = login_url
        self.feed_url = feed_url
        self.context_args = context_args
        self.session_path = session_file_path

    async def get_context(self, browser: Browser) -> BrowserContext:
        if os.path.exists(self.session_path):
            logger.info("Using existing LinkedIn session")
            context = await browser.new_context(
                storage_state=self.session_path, **self.context_args
            )
            page = await context.new_page()
            await page.goto(self.feed_url, wait_until="load", timeout=120000)
            if page.url.startswith(self.feed_url):
                logger.info("Existing session is valid")
                return context
            else:
                logger.warning("Existing session is invalid, performing login")
                await context.close()

        logger.info("No session found, performing LinkedIn login")
        context = await browser.new_context(**self.context_args)

        login_success = await self._login(context)
        if not login_success:
            await context.close()
            raise RuntimeError("LinkedIn login failed")

        await context.storage_state(path=self.session_path)
        await context.close()
        logger.info("Login successful, session saved")

        return await browser.new_context(
            storage_state=self.session_path, **self.context_args
        )

    async def _login(self, context: BrowserContext) -> bool:
        """Login using email and password."""
        try:
            page = await context.new_page()
            await page.goto(self.login_url, wait_until="load", timeout=120000)
            await page.fill("#username", self.email)
            await page.fill("#password", self.password)
            await page.press("#password", "Enter")

            await page.wait_for_url(
                re.compile(rf"^{self.feed_url}"), wait_until="load", timeout=120000
            )
            await context.storage_state(path=self.session_path)
            return True
        except Exception as e:
            logger.error(f"Login attempt failed: {e}")
            return False
