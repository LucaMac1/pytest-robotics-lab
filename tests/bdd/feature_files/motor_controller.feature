Feature: Motor controller basic movement logic

  Scenario: Motor moves forward without obstacles
    Given I have a valid sensor and motor
    When I command the motor to move forward with speed 5
    Then the motor should be running
    And the stopping distance should be 2.5

  Scenario: Motor stops when obstacle is detected
    Given I have a sensor that detects an obstacle at distance 10
    When I command the motor to move forward with speed 3
    Then the motor should stop
    And the stopping distance should be 1.5

  Scenario: Invalid speed input
    Given I have a valid sensor and motor
    When I command the motor to move forward with speed -1
    Then I should receive an error indicating invalid speed

  Scenario: Faulty sensor triggers error
    Given I have a sensor that reports invalid distance
    When I command the motor to move forward with speed 4
    Then I should receive a sensor error
