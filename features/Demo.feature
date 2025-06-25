Feature: Testing feature
  Scenario Outline:
    Given Open the browser and enter the url
    When user enter the "<username>" and "<password>"
    And user click on login button
    Then user should successfully logged in and dashboard page should be displayed
    Examples:
      | username                    |  password    |
      | bikash.sahoo@sharajman.com  |  "Admin@1234 |