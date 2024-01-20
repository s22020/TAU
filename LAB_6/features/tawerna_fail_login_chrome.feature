Feature: Tawerna RPG Forum Login Flow

  Scenario: Failed Login Flow
    Given the user opens Tawerna RPG forum URL
    When the user clicks on the login button
    And types fake login and password
    Then the user sees an error message about incorrect credentials