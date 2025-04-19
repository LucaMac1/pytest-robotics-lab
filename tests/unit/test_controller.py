import pytest
from unittest.mock import MagicMock
from robot.controller import MotorController

def test_move_forward_with_no_obstacle():
    # Create a mock sensor
    mock_sensor = MagicMock()
    # Mock get_distance to return a value greater than the stopping distance for speed 5
    mock_sensor.get_distance.return_value = 10  # Distance is far enough (greater than stopping distance)
    
    # Instantiate MotorController with the mock sensor
    controller = MotorController(mock_sensor)
    
    # Test if the motor moves forward when no obstacle is close
    result = controller.move_forward(5)
    
    # The expected result should be moving forward at speed 5
    assert result == "Moving forward at 5 m/s"

def test_move_forward_with_obstacle():
    # Create a mock sensor
    mock_sensor = MagicMock()
    # Mock get_distance to return a value less than the stopping distance for speed 5
    mock_sensor.get_distance.return_value = 6  # Distance is less than stopping distance for speed 5 (5 * 1.5 = 7.5)
    
    # Instantiate MotorController with the mock sensor
    controller = MotorController(mock_sensor)
    
    # Test if the motor detects the obstacle and stops
    stopping_distance = 5 * 1.5  # Expected stopping distance for speed 5
    result = controller.move_forward(5)
    
    # The expected result should include the stopping distance
    assert result == f"Obstacle too close. Stopping distance: {stopping_distance} meters."