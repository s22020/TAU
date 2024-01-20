Feature: WoW Cart Checkout Firefox

  Scenario: Add product to cart and complete checkout on Firefox
    Given the user is on the WoW Gear website on Firefox
    When the user closes the promo popup on Firefox
    And the user searches for a product with keyword 'horde beanie' on Firefox
    Then the search is successful on Firefox
    When the user clicks on the first returned product on Firefox
    And adds the product to the cart on Firefox
    And proceeds to checkout on Firefox
    And adds shipping details on Firefox
    And continues to payment on Firefox
    Then the checkout is completed successfully on Firefox