import pytest
from robot.controller import MotorController
from robot.sensors import DistanceSensor

@pytest.mark.integration
def test_controller_stops_on_near_obstacle():
    # Create a sensor with a patched distance method
    sensor = DistanceSensor()
    sensor.get_distance = lambda: 3  # Mocking the distance to be 3 meters (obstacle too close)
    
    # Instantiate the MotorController with the mocked sensor
    controller = MotorController(sensor)
    
    # Set the speed of the motor
    speed = 10
    
    # Calculate the stopping distance (for speed 10, stopping distance is speed * 1.5)
    stopping_distance = speed * 1.5
    
    # Call the move_forward method
    result = controller.move_forward(speed)
    
    # Assert that the result includes the stopping distance
    assert result == f"Obstacle too close. Stopping distance: {stopping_distance} meters."