import os
import re
import logging
from playwright.async_api import (
    Browser,
    BrowserContext,
    Page,
)

logger = logging.getLogger(__name__)


class LinkedInAuthenticator:
    def __init__(
        self,
        email: str,
        password: str,
        login_url: str,
        feed_url: str,
        context_args: dict,
        session_path: str,
    ):
        self.email = email
        self.password = password
        self.login_url = login_url
        self.feed_url = feed_url
        self.context_args = context_args
        self.session_path = session_path

    async def get_auth_context(self, browser: Browser) -> BrowserContext:
        if os.path.exists(self.session_path):
            logger.info(f"Found existing session file: {self.session_path}")
            context = await browser.new_context(
                storage_state=self.session_path, **self.context_args
            )

            if await self._is_session_valid(context):
                logger.info("Reusing valid LinkedIn session")
                return context

            logger.warning("Saved session is no longer valid → performing fresh login")
            await context.close()

        logger.info("Starting new LinkedIn authentication flow")
        context = await browser.new_context(**self.context_args)

        success = await self._perform_login(context)
        if not success:
            await context.close()
            raise RuntimeError(
                "LinkedIn login failed — check credentials, 2FA, or network issues"
            )

        await context.storage_state(path=self.session_path)
        logger.info(f"Login successful.New session saved to: {self.session_path}")

        await context.close()
        return await browser.new_context(
            storage_state=self.session_path, **self.context_args
        )

    async def _is_session_valid(self, context: BrowserContext) -> bool:
        """Quick check if the stored session is still authenticated."""
        page: Page = await context.new_page()
        try:
            await page.goto(self.feed_url, wait_until="commit", timeout=25000)

            if page.url.startswith(self.feed_url):
                logger.debug("Session appears valid (landed on feed)")
                return True
            return False
        except Exception as e:
            logger.warning(f"Session validation failed: {e}", exc_info=False)
            return False
        finally:
            await page.close()

    async def _perform_login(self, context: BrowserContext) -> bool:
        page: Page = await context.new_page()
        try:
            await page.goto(self.login_url, wait_until="commit", timeout=30000)
            await page.wait_for_selector(
                "#username, input[name='session_key']", timeout=15000
            )
            await page.fill("#username, input[name='session_key']", self.email)
            await page.fill("#password, input[name='session_password']", self.password)
            await page.click(
                "button[type=submit][data-litms-control-urn='login-submit']",
                timeout=10000,
            )
            await page.wait_for_url(
                re.compile(rf"^{re.escape(self.feed_url)}", re.IGNORECASE),
                timeout=45000,
                wait_until="domcontentloaded",
            )
            return True
        except Exception as e:
            logger.error(f"Login Failed with exception: {e}", exc_info=True)
            return False
        finally:
            await page.close()
