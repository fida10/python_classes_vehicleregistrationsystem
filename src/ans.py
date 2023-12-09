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