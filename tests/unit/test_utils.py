from robot.utils import calculate_speed

def test_speed_calculation():
    assert calculate_speed(10, 2) == 5.0

def test_zero_time():
    assert calculate_speed(10, 0) == 0