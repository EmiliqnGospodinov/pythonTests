import pytest
from playwright.sync_api import expect


from pom_example.pages.login_page import LoginPage

def test_successful_login(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("student", "Password123")

    assert login_page.get_title() == "Logged In Successfully | Practice Test Automation"

def test_unsuccessful_login(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("invalid_user", "invalid_password")

    assert login_page.failure_message.is_visible()
    expect(login_page.failure_message).to_have_text("Your username is invalid!")
    assert login_page.get_title() == "Test Login | Practice Test Automation"