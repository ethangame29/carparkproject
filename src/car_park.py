from display import Display
from sensor import Sensor


class CarPark:

    def __init__(self, location=None, capacity=None, plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []

    def __str__(self):
        return f"Car Park {self.location} with {self.capacity} capacity"

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plates):
        pass

    def remove_car(self, plates):
        pass

    def update_displays(self):
        pass