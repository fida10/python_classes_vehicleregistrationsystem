""" 
Question 1: Vehicle Registration System

Description:

Create a class called VehicleRegistry. It should have the following attributes and methods:

Attributes: registry_name (string) and registered_vehicles (dictionary with vehicle license plate numbers as keys and a tuple (owner_name, vehicle_type) as values).

Methods:

register_vehicle(license_plate, owner_name, vehicle_type): Registers a new vehicle.

deregister_vehicle(license_plate): Removes a vehicle from the registry.

list_vehicles(): Returns a list of all registered vehicles in the format "License Plate: Owner - Vehicle Type".
"""

class VehicleRegistry:
    
    def __init__(self, registry_name):
        self.registry_name = registry_name
        self.registered_vehicles = {}
    
    def register_vehicle(self, reg_no, owner, vehicle_type):
        self.registered_vehicles[reg_no] = (owner, vehicle_type)

    def deregister_vehicle(self, reg_no):
        self.registered_vehicles.pop(reg_no)
    
    def list_vehicles(self):
        ans = []
        for key, value in self.registered_vehicles.items():
            ans.append(f'{key}: {value[0]} - {value[1]}')
        return ans