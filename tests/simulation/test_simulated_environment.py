import pytest

@pytest.mark.simulation
def test_simulated_robot_movement(sim_env):
    sim_env.load_map("test_room")
    sim_env.spawn_robot()
    sim_env.command_move(1.0, 0.0)
    assert sim_env.robot_position().x > 0
