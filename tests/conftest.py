import pytest
from robot.controller import MotorController
from robot.sensors import DistanceSensor

@pytest.fixture
def sensor():
    return DistanceSensor()

@pytest.fixture
def controller(sensor):
    return MotorController(sensor)

@pytest.fixture
def sim_env():
    # This fixture would return a mock environment for simulation tests
    class SimulatedEnvironment:
        def load_map(self, map_name):
            pass

        def spawn_robot(self):
            pass

        def command_move(self, x, y):
            pass

        def robot_position(self):
            class Position:
                x = 1
            return Position()
    
    return SimulatedEnvironment()