from pytest_bdd import given, when, then, scenarios
import pytest
from robot_bindings import RobotController  # pybind11-generated

scenarios('../features/autonomous_navigation.feature')

@pytest.fixture
def robot():
    return RobotController()

@given("the robot is initialised")
def init_robot(robot):
    # Assume constructor does the initialisation
    pass

@when("the robot moves forward")
def move(robot):
    robot.move_forward(3)

@then("the robot should report moving forward")
def check(robot):
    assert robot.get_status() == "Moving forward"