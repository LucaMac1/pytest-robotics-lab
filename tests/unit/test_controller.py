import pytest
from unittest.mock import MagicMock
from robot.controller import MotorController
from robot.hardware import Motor, MotorStatus
from robot.sensors import DistanceSensor
from robot.exceptions import SensorError

def test_move_forward_success():
    mock_sensor = MagicMock(spec=DistanceSensor)
    mock_motor = MagicMock(spec=Motor)
    mock_sensor.get_distance.return_value = 15

    controller = MotorController(mock_sensor, mock_motor)
    status, stopping_distance = controller.move_forward(5)

    assert status == MotorStatus.RUNNING
    assert stopping_distance == pytest.approx(7.5)
    mock_motor.start.assert_called_once()

def test_obstacle_detected():
    mock_sensor = MagicMock(spec=DistanceSensor)
    mock_motor = MagicMock(spec=Motor)
    mock_sensor.get_distance.return_value = 5

    controller = MotorController(mock_sensor, mock_motor)
    status, stopping_distance = controller.move_forward(5)

    assert status == MotorStatus.OBSTACLE_DETECTED
    assert stopping_distance == pytest.approx(7.5)
    mock_motor.stop.assert_called_once()

def test_invalid_speed():
    controller = MotorController(DistanceSensor(), Motor())
    with pytest.raises(ValueError):
        controller.move_forward(-1)

def test_sensor_error_propagates():
    mock_sensor = MagicMock(spec=DistanceSensor)
    mock_sensor.get_distance.return_value = -1  # Invalid distance
    controller = MotorController(mock_sensor, Motor())

    with pytest.raises(SensorError):
        controller.move_forward(2)