import pytest
from robot.sensors import DistanceSensor
from robot.exceptions import SensorError

def test_valid_distance():
    sensor = DistanceSensor()
    assert sensor.get_distance() == 10

def test_invalid_distance():
    class FaultySensor(DistanceSensor):
        def get_distance(self):
            return -5  # simulate fault

    sensor = FaultySensor()
    with pytest.raises(SensorError):
        sensor.get_distance()