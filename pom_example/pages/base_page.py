from playwright.sync_api import Page
from pom_example.config.config import BASE_URL

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, path: str = ""):
        full_url = f"{BASE_URL.rstrip('/')}/{path.lstrip('/')}"
        self.page.goto(full_url)

    def get_title(self):
        return self.page.title()

    def click(self, selector: str):
        self.page.click(selector)

    def fill(self, selector: str, value: str):
        self.page.fill(selector, value)

    def is_visible(self, selector: str):
        return self.page.is_visible(selector)
