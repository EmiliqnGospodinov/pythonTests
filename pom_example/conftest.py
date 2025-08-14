import pytest
from playwright.sync_api import sync_playwright
from config.config import BASE_URL, HEADLESS, BROWSER_TYPE

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = getattr(playwright_instance, BROWSER_TYPE).launch(headless=HEADLESS)
    yield browser
    browser.close()

@pytest.fixture(scope="session")
def context(browser):
    context = browser.new_context(base_url=BASE_URL)
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()
