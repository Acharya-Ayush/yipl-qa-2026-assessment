import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport=None)  # tells Playwright to use full window
        page = context.new_page()
        
        # Get the screen size (use typical large values if unsure)
        page.set_viewport_size({"width": 1920, "height": 1080})  # manually maximize
        yield page
        browser.close()
