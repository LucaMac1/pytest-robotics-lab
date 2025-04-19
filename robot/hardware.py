# robot/hardware.py

class Motor:
    def __init__(self, id=None):
        self.id = id
        self.status = "stopped"

    def start(self):
        self.status = "running"

    def stop(self):
        self.status = "stopped"
