class SensorError(Exception):
    """
    Custom exception to indicate sensor issues.

    :param message: Description of the error.
    :param sensor_data: Optional data from the sensor that caused the error.
    """
    def __init__(self, message, sensor_data=None):
        super().__init__(message)
        self.message = message
        self.sensor_data = sensor_data

    def __str__(self):
        if self.sensor_data is not None:
            return f"{self.message} - Sensor Data: {self.sensor_data}"
        return self.message


class MotorError(Exception):
    """
    Custom exception to indicate motor-related errors.

    :param message: Description of the error.
    :param motor_id: Optional ID of the motor involved in the error.
    """
    def __init__(self, message, motor_id=None):
        super().__init__(message)
        self.message = message
        self.motor_id = motor_id

    def __str__(self):
        if self.motor_id is not None:
            return f"{self.message} - Motor ID: {self.motor_id}"
        return self.message
