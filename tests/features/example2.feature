Feature: Playwright example 2

  Scenario: Visit a website and assert the title
    Given The browser is open
    When I navigate to "https://www.google.com/search?q=maps"
    Then The title should be "maps - Buscar con Google"
    And The browser should close

  Scenario: Visit a second website
    Given The browser 2 is open
    When I navigate to "https://www.saucedemo.com"
    Then The title should be "Swag Labs"
    And The browser should close the page
