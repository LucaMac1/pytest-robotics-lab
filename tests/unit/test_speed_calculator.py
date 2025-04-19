from robot.utils import calculate_speed

def test_speed_calculator_simple():
    assert calculate_speed(10, 2) == 5

def test_speed_divide_by_zero():
    assert calculate_speed(10, 0) == 0