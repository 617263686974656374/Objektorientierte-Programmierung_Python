from vehicle_c import Vehicle
class Car(Vehicle):
    def __init__(self, mark, model, year, fuel_type, tank_capacity, current_fuel, num_doors, **kwargs):
        super().__init__(mark, model, year, fuel_type, tank_capacity, current_fuel)
        self.num_doors = num_doors
        self.refuel_history = kwargs.get('refuel_history', [])
