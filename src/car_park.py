class CarPark:

    def __init__(self, location=None, capacity=None, plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates
        self.sensors = sensors or []
        self.displays = displays

    def __str__(self):
        return f"Car Park {self.location} with {self.capacity} capacity"