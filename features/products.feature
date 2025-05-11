Feature: Product API BDD Scenarios

  Background:
    Given the following products exist:
      | name   | category    | price | available |
      | Widget | Electronics | 19.99 | true      |
      | Book   | Books       | 9.99  | false     |

  Scenario: Read a product
    When I send a "GET" request to "/products/1"
    Then the response status code should be 200
    And the response should contain "Widget"

  Scenario: Update a product
    When I send a "PUT" request to "/products/1" with json:
      """
      {
        "name": "WidgetX",
        "category": "Electronics",
        "price": 24.99,
        "available": true
      }
      """
    Then the response status code should be 200
    And the response should contain "WidgetX"

  Scenario: Delete a product
    When I send a "DELETE" request to "/products/2"
    Then the response status code should be 200
    And the response should contain "product deleted"

  Scenario: List all products
    When I send a "GET" request to "/products"
    Then the response status code should be 200
    And the response should contain "Widget"

  Scenario: Search by category
    When I send a "GET" request to "/products?category=Books"
    Then the response status code should be 200
    And the response should contain "Book"

  Scenario: Search by availability
    When I send a "GET" request to "/products?available=true"
    Then the response status code should be 200
    And the response should contain "Widget"

  Scenario: Search by name
    When I send a "GET" request to "/products?name=Widget"
    Then the response status code should be 200
    And the response should contain "Widget"
