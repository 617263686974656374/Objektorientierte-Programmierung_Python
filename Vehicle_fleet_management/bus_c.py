from vehicle_c import Vehicle
class Bus(Vehicle):
    def __init__(self, mark, model, year, fuel_type, tank_capacity, current_fuel, num_passengers, **kwargs):
        super().__init__(mark, model, year, fuel_type, tank_capacity, current_fuel)
        self.num_passengers = num_passengers
        self.refuel_history = kwargs.get('refuel_history', [])
