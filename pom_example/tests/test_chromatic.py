from playwright.sync_api import sync_playwright, expect

def test_homepage():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://practicetestautomation.com/practice-test-login/")
        
        # Assert title
        expect(page).to_have_title("Test Login | Practice Test Automation")

        browser.close()
