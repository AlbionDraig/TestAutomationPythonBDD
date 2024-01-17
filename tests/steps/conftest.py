import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def browser():
    with sync_playwright() as p:
        # Headless
        #browser = p.chromium.launch()
        # No headless
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()
