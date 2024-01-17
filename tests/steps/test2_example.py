import pytest
from playwright.sync_api import sync_playwright

from pytest_bdd import scenario, given, when, then, scenarios

# Escenario 1
@scenario("../features/example2.feature", 'Visit a website and assert the title')
def test_visit_website_and_assert_title():
    pass

@given("The browser is open")
def open_browser(browser):
    assert browser

@when('I navigate to "https://www.google.com/search?q=maps"')
def navigate_to_url(page):
    page.goto("https://www.google.com/search?q=maps")

@then('The title should be "maps - Buscar con Google"')
def assert_title(page):
    assert page.title() == "maps - Buscar con Google"

@then("The browser should close")
def close_browser(browser):
    browser.close()
    

    

# Escenario 2
@scenario("../features/example2.feature", 'Visit a second website')
def test_visit_website_2():
    pass

@given("The browser 2 is open")
def open_browser_2(browser):
    assert browser

@when('I navigate to "https://www.saucedemo.com"')
def navigate_to_url(page):
    page.goto("https://www.saucedemo.com")
    
@then('The title should be "Swag Labs"')
def assert_title_navigate_2(page):
    assert page.title() == "Swag Labs"

@then("The browser should close the page")
def close_browser(browser):
    browser.close()
