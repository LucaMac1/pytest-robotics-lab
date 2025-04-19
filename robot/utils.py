# robot/utils.py
def calculate_speed(distance, time):
    if time == 0:
        return 0
    return distance / time
