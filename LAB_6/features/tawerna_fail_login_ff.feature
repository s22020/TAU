Feature: Tawerna RPG Forum Login Flow Firefox

  Scenario: Failed Login Flow on Firefox
    Given the user opens Tawerna RPG forum URL on Firefox
    When the user clicks on the login button on Firefox
    And types fake login and password on Firefox
    Then the user sees an error message about incorrect credentials on Firefox