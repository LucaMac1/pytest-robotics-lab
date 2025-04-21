from robot.exceptions import SensorError, MotorError

def test_sensor_error_with_data():
    error = SensorError("Failure", sensor_data=0)
    assert str(error) == "Failure - Sensor Data: 0"

def test_sensor_error_without_data():
    error = SensorError("Failure")
    assert str(error) == "Failure"

def test_motor_error_with_id():
    error = MotorError("Stuck", motor_id="M1")
    assert str(error) == "Stuck - Motor ID: M1"

def test_motor_error_without_id():
    error = MotorError("Stuck")
    assert str(error) == "Stuck"