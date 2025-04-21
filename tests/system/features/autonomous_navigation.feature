Feature: Robot movement

  Scenario: Move forward when path is clear
    Given the robot is started
    And the sensor reports a distance of 100 meters
    When the robot tries to move at speed 3
    Then the robot should move forward

  Scenario: Stop when an obstacle is close
    Given the robot is started
    And the sensor reports a distance of 1 meter
    When the robot tries to move at speed 5
    Then the robot should stop with a warning