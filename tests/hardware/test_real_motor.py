# tests/hardware/test_real_motor.py
from robot.hardware import Motor

def test_motor_can_spin():
    motor = Motor()  # No need for the 'id' argument
    motor.start()
    assert motor.status == "running"