Feature: Playwright Example

  Scenario: Verify the title after navigating to a website
    Given The browser is open
    When I navigate to "https://www.google.com"
    Then The title should be "Google"
    And I search for "Hello World"
    And The browser should close
