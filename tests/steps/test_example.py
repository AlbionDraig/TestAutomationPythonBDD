import pytest
from playwright.sync_api import sync_playwright

from pytest_bdd import given, when, then, scenarios

# Use pytest-bdd scenarios decorator to specify the feature file
scenarios("../features/example.feature")

# Implement the Given step
@given("The browser is open")
def open_browser(browser):
    assert browser

# Implement the When step
@when('I navigate to "https://www.google.com"')
def navigate_to_url(page):
    page.goto("https://www.google.com")

# Implement the Then steps
@then('The title should be "Google"')
def assert_title(page):
    assert page.title() == "Google"
    
@then('I search for "Hello World"')
def assert_title_navigate(page):
    page.locator('//textarea[@id="APjFqb" and @type="search"]').fill('Hello World')
    page.locator('//div[@jsname="VlcLAe"]/center/input[1]').click()
    assert page.title() == "Hello World - Buscar con Google"

@then("The browser should close")
def close_browser(browser):
    browser.close()
