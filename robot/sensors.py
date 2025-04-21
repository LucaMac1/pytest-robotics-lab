from robot.exceptions import SensorError


class DistanceSensor:
    """
    Simulated distance sensor for detecting obstacles.
    """

    def get_distance(self):
        """
        Get the distance reading from the sensor.

        :return: Simulated distance in meters.
        :raises SensorError: If distance is invalid.
        """
        simulated_distance = 10  # Replace with hardware interaction in real usage
        if simulated_distance < 0:
            raise SensorError("Distance reading is invalid", sensor_data=simulated_distance)
        return simulated_distance
