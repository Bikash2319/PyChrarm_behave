Feature: Add New Make
  @login_required
  Scenario: Adding a new make into the master
    Given Navigate to Make module
    When User click on Add Make button
    And Enter new make details
    Then Click on Save button

  @login_required
  Scenario: Adding a new make by entering invalid values in make input field
    Given Navigate to Make module
    When User click on Add Make button
    And user entered special characters and numbers in input field
    Then Click on Save button and user should prompted to enter valid characters