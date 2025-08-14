from playwright.sync_api import expect
from pom_example.pages.login_page import LoginPage

def test_banner_aria_snapshot(page):
    login_page = LoginPage(page)
    login_page.open()
    expect(login_page.banner).to_match_aria_snapshot("""
        - navigation
        - link "Practice Test Automation"
        - navigation
    """)