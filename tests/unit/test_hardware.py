import pytest
from robot.hardware import Motor, MotorStatus
from robot.exceptions import MotorError

def test_motor_start_stop():
    motor = Motor(id="L")
    motor.start()
    assert motor.status == MotorStatus.RUNNING
    motor.stop()
    assert motor.status == MotorStatus.STOPPED

def test_start_while_running():
    motor = Motor()
    motor.start()
    with pytest.raises(MotorError):
        motor.start()

def test_stop_while_stopped():
    motor = Motor()
    with pytest.raises(MotorError):
        motor.stop()