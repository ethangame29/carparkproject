from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display


car_park = CarPark("Moondalup", 100, log_file="moondalup.txt")
entry_sensor = EntrySensor(1, True, car_park)
exit_sensor = ExitSensor(2, True, car_park)
display = Display(1, car_park, "Welcome to Moondalup", True)

x = 0
while x < 10:
    entry_sensor.detect_vehicle()
    x = x + 1

x = 0
while x < 2:
    exit_sensor.detect_vehicle()
    x = x + 1
