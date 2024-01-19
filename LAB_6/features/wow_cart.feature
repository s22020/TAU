Feature: WoW Cart Checkout

  Scenario: Add product to cart and complete checkout
    Given the user is on the WoW Gear website
    When the user searches for a product with keyword 'horde beanie'
    Then the search is successful
    When the user clicks on the first returned product
    And adds the product to the cart
    And closes the promo popup
    And proceeds to checkout
    And adds shipping details
    And continues to payment
    Then the checkout is completed successfully