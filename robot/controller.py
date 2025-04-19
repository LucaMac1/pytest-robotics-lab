# Simulated controller for a robot
class MotorController:
    def __init__(self, sensor):
        self.sensor = sensor

    def move_forward(self, speed):
        # Define a factor that determines how stopping distance increases with speed
        stopping_distance_factor = 1.5  # This factor can be adjusted based on real-world physics
        
        # Calculate the stopping distance based on speed
        stopping_distance = speed * stopping_distance_factor
        
        if self.sensor.get_distance() < stopping_distance:  # If obstacle is too close
            return f"Obstacle too close. Stopping distance: {stopping_distance} meters."
        
        return f"Moving forward at {speed} m/s"
