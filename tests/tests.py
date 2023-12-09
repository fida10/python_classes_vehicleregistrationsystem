import unittest
from src.ans import VehicleRegistry

class TestVehicleRegistry(unittest.TestCase):
    def setUp(self):
        self.registry = VehicleRegistry("City Registry")

    def test_register_vehicle(self):
        self.registry.register_vehicle("ABC123", "John Doe", "Car")
        self.assertIn("ABC123", self.registry.registered_vehicles)
        self.assertEqual(
            self.registry.registered_vehicles["ABC123"], ("John Doe", "Car"))

    def test_deregister_vehicle(self):
        self.registry.register_vehicle("XYZ789", "Jane Smith", "Truck")
        self.registry.deregister_vehicle("XYZ789")
        self.assertNotIn("XYZ789", self.registry.registered_vehicles)

    def test_list_vehicles(self):
        self.registry.register_vehicle("ABC123", "John Doe", "Car")
        expected_list = ["ABC123: John Doe - Car"]
        self.assertEqual(self.registry.list_vehicles(), expected_list)


if __name__ == '__main__':
    unittest.main()
