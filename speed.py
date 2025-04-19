def calculate_speed(distance, time):
    if time == 0:
        raise ValueError("Time cannot be zero.")
    return distance / time