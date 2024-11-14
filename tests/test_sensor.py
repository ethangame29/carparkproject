import unittest
from sensor import EntrySensor, ExitSensor
from car_park import CarPark


class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)
        self.entry_sensor = EntrySensor(1, True, self.car_park)
        self.exit_sensor = ExitSensor(2, True, self.car_park)

    def test_sensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.entry_sensor, EntrySensor)
        self.assertIsInstance(self.exit_sensor, ExitSensor)
        self.assertIsInstance(self.car_park, CarPark)
        self.car_park.register(self.entry_sensor)
        self.car_park.register(self.exit_sensor)
        self.assertEqual(self.car_park.sensors, [self.entry_sensor, self.exit_sensor])
        self.assertEqual(self.entry_sensor.id, 1)
        self.assertEqual(self.entry_sensor.is_active, True)
        self.assertIsInstance(self.entry_sensor.car_park, CarPark)
        self.assertEqual(self.exit_sensor.id, 2)
        self.assertEqual(self.exit_sensor.is_active, True)
        self.assertIsInstance(self.exit_sensor.car_park, CarPark)

    def test_detect_vehicle_entry(self):
        self.entry_sensor.detect_vehicle()
        self.assertIn("FAKE", self.car_park.plates[-1])


if __name__ == '__main__':
    unittest.main()