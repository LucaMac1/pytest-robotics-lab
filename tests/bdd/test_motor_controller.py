import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from unittest.mock import MagicMock
from robot.controller import MotorController
from robot.hardware import Motor, MotorStatus
from robot.sensors import DistanceSensor
from robot.exceptions import SensorError

# Load feature scenarios
scenarios('motor_controller.feature')

# --- Given Steps ---

@given("I have a valid sensor and motor")
def valid_sensor_motor():
    mock_sensor = MagicMock(spec=DistanceSensor)
    mock_motor = MagicMock(spec=Motor)
    mock_sensor.get_distance.return_value = 15  # Safe distance
    return mock_sensor, mock_motor


@given(parsers.parse("I have a sensor that detects an obstacle at distance {obstacle_distance:d}"))
def obstacle_sensor(obstacle_distance):
    mock_sensor = MagicMock(spec=DistanceSensor)
    mock_motor = MagicMock(spec=Motor)
    mock_sensor.get_distance.return_value = obstacle_distance
    controller = MotorController(mock_sensor, mock_motor)
    return controller.move_forward(3)  # Use the same speed as in the feature


@given("I have a sensor that reports invalid distance")
def faulty_sensor():
    mock_sensor = MagicMock(spec=DistanceSensor)
    mock_motor = MagicMock(spec=Motor)
    mock_sensor.get_distance.return_value = -1
    return mock_sensor, mock_motor


# --- When Steps ---

@when(parsers.parse("I command the motor to move forward with speed {speed:d}"))
def move_motor_forward(valid_sensor_motor, speed):
    mock_sensor, mock_motor = valid_sensor_motor
    controller = MotorController(mock_sensor, mock_motor)
    if speed < 0:
        # Let the 'then' step handle the error
        return controller, speed
    return controller.move_forward(speed)


# --- Then Steps ---

@then("the motor should be running")
def motor_running(move_motor_forward):
    status, _ = move_motor_forward
    assert status == MotorStatus.RUNNING


@then("the motor should stop")
def motor_stop(obstacle_sensor):
    status, _ = obstacle_sensor
    assert status == MotorStatus.OBSTACLE_DETECTED


@then(parsers.parse("the stopping distance should be {stopping_distance:f}"))
def check_stopping_distance(move_motor_forward, stopping_distance):
    _, actual_stopping_distance = move_motor_forward
    assert actual_stopping_distance == pytest.approx(stopping_distance)


@then("I should receive an error indicating invalid speed")
def invalid_speed_error(move_motor_forward):
    controller, speed = move_motor_forward
    with pytest.raises(ValueError):
        controller.move_forward(speed)


@then("I should receive a sensor error")
def sensor_error(faulty_sensor):
    mock_sensor, mock_motor = faulty_sensor
    controller = MotorController(mock_sensor, mock_motor)
    with pytest.raises(SensorError):
        controller.move_forward(4)  # arbitrary speed