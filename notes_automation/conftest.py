import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from utils.config import EMAIL, PASSWORD, BASE_URL

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="session")
def logged_in_page(browser):
    context = browser.new_context(viewport=None)
    page = context.new_page()

    # Manual maximize by setting viewport size
    page.set_viewport_size({"width": 1920, "height": 1080})

    login_page = LoginPage(page)
    login_page.navigate(BASE_URL)
    login_page.login()
    yield page
    context.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(viewport=None)
    page = context.new_page()

    # Manual maximize by setting viewport size
    page.set_viewport_size({"width": 1920, "height": 1080})

    yield page
    context.close()
