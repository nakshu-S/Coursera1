Feature: Products Management

  Background:
    Given the following products exist:
      | name    | category | available |
      | Hat     | Clothing | True      |
      | Shoes   | Clothing | True      |
      | Big Mac | Food     | True      |
      | Sheets  | Home     | False     |

  Scenario: Reading a Product
    Given I am on the Products page
    When I search for "Hat"
    Then I should see a success message
    And I should see the product details

  Scenario: Updating a Product
    Given I am on the Products page
    When I search for "Hat"
    Then I should see a success message
    When I update the product details
    Then I should see a success message
    When I retrieve the updated product
    Then I should see the updated values

  Scenario: Deleting a Product
    Given I am on the Products page
    When I search for "Hat"
    Then I should see a success message
    When I delete the product
    Then I should see "Product has been Deleted!"
    When I search for "Hat"
    Then the product should not be in the results

  Scenario: Listing All Products
    Given I am on the Products page
    When I clear the form
    And I press the Search button
    Then I should see a success message
    And I should see all products:
      | name    |
      | Hat     |
      | Shoes   |
      | Big Mac |
      | Sheets  |

  Scenario: Searching Product by Category
    Given I am on the Products page
    When I select the "Food" category
    And I press the Search button
    Then I should see a success message
    And I should see "Big Mac" in the results
    And other categories should not appear

  Scenario: Searching Product by Availability
    Given I am on the Products page
    When I select Available as "True"
    And I press the Search button
    Then I should see a success message
    And only available products should appear in the results

  Scenario: Searching Product by Name
    Given I am on the Products page
    When I enter the product name "Hat"
    And I press the Search button
    Then I should see a success message
    And I should see "Hat" in the results