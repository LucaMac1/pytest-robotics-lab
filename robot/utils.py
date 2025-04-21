def calculate_speed(distance, time):
    """
    Calculate speed given the distance and time.

    :param distance: The distance covered (in meters).
    :param time: The time taken (in seconds).
    :return: The calculated speed (m/s).
    """
    if time == 0:
        return 0
    return distance / time