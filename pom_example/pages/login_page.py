from .base_page import BasePage
from playwright.sync_api import Locator

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Locators
        self.username_input: Locator = page.locator("#username")
        self.password_input: Locator = page.locator("#password")
        self.login_button: Locator = page.locator("#submit")
        self.banner: Locator = page.locator("#site-header")
        self.failure_message = page.locator("#error")

    def visit(self, url: str):
        """Navigate to the login page."""
        self.page.goto(url)

    def login(self, username: str, password: str):
        """Fill in credentials and submit the form."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

