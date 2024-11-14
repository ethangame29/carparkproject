from display import Display
from sensor import Sensor
from pathlib import Path
from datetime import datetime
import json


class CarPark:

    def __init__(self, location=None, capacity=None, plates=None, sensors=None, displays=None, log_file=Path("log.txt"), config_file=Path("config.json")):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        self.log_file.touch(exist_ok=True)
        self.config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        self.config_file.touch(exist_ok=True)

    def __str__(self):
        return f"Car Park {self.location} with {self.capacity} capacity"

    @property
    def available_bays(self):
        if len(self.plates) <= self.capacity:
            return self.capacity - len(self.plates)
        else:
            return 0

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()
        self._log_car_activity(plate, "Entered")

    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_displays()
        self._log_car_activity(plate, "Exited")

    def update_displays(self):
        info = {"available_bays": self.available_bays, "temperature": 25}
        for display in self.displays:
            display.update(info)

    def _log_car_activity(self, plate, action):
        with self.log_file.open("a") as file:
            file.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")

    def write_config(self):
        with open("config.json", "w") as f:
            json.dump({"location": self.location, "capacity": self.capacity, "log_file": str(self.log_file)}, f)

    @classmethod
    def from_config(cls, config_file):
        with config_file.open() as file:
            config = json.load(file)
        return cls(config["location"], config["capacity"], log_file=config["log_file"])