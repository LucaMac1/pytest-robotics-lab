from enum import Enum
from robot.exceptions import MotorError


class MotorStatus(Enum):
    """Enumeration of motor states."""
    STOPPED = "Motor stopped"
    RUNNING = "Motor running"
    OBSTACLE_DETECTED = "Obstacle too close, motor stopped"


class Motor:
    """
    Simulated motor with basic start and stop behaviour.

    :param id: Optional motor identifier.
    """
    def __init__(self, id=None):
        self.id = id
        self.status = MotorStatus.STOPPED

    def start(self):
        """
        Start the motor. Raises MotorError if already running.
        """
        if self.status == MotorStatus.RUNNING:
            raise MotorError("Motor already running", motor_id=self.id)
        self.status = MotorStatus.RUNNING

    def stop(self):
        """
        Stop the motor. Raises MotorError if already stopped.
        """
        if self.status == MotorStatus.STOPPED:
            raise MotorError("Motor already stopped", motor_id=self.id)
        self.status = MotorStatus.STOPPED