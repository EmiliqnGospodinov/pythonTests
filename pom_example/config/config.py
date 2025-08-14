import os

# Base URL for all tests (default to staging)
BASE_URL = os.getenv("BASE_URL", "https://practicetestautomation.com/")

# Browser settings
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
BROWSER_TYPE = os.getenv("BROWSER", "chromium")  # chromium, firefox, webkit
