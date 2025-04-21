from robot.hardware import MotorStatus, Motor
from robot.sensors import DistanceSensor
from robot.exceptions import SensorError

class MotorController:
    """
    Controls a motor based on distance sensor input.

    :param sensor: Instance of DistanceSensor.
    :param motor: Instance of Motor.
    """
    def __init__(self, sensor: DistanceSensor, motor: Motor):
        self.sensor = sensor
        self.motor = motor

    def move_forward(self, speed: float):
        """
        Move the motor forward if there is enough stopping distance.

        :param speed: Speed in m/s.
        :return: Tuple of motor status and stopping distance.
        :raises ValueError: If speed is negative.
        :raises SensorError: If sensor reading is invalid.
        """
        if speed < 0:
            raise ValueError("Speed must be positive.")

        stopping_distance_factor = 1.5
        stopping_distance = speed * stopping_distance_factor

        distance = self.sensor.get_distance()
        if distance <= 0:
            raise SensorError("Invalid sensor reading", sensor_data=distance)

        if distance < stopping_distance:
            self.motor.stop()
            return MotorStatus.OBSTACLE_DETECTED, stopping_distance

        self.motor.start()
        return MotorStatus.RUNNING, stopping_distance