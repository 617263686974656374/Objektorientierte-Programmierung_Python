from vehicle_c import Vehicle
class Truck(Vehicle):
    def __init__(self, mark, model, year, fuel_type, tank_capacity, current_fuel, max_load, **kwargs):
        super().__init__(mark, model, year, fuel_type, tank_capacity, current_fuel)
        self.max_load = max_load
        self.refuel_history = kwargs.get('refuel_history', [])
