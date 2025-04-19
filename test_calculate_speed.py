import pytest
from speed import calculate_speed

def test_calculate_speed():
    # Test valid case
    assert calculate_speed(10, 2) == 5

def test_calculate_speed_zero_time():
    # Test invalid case: Time cannot be zero
    with pytest.raises(ValueError):
        calculate_speed(10, 0)

# Fixture to simulate sensor data
@pytest.fixture
def sensor_data():
    return {"distance": 10, "time": 2}

def test_calculate_speed_with_sensor_data(sensor_data):
    speed = calculate_speed(sensor_data["distance"], sensor_data["time"])
    assert speed == 5
