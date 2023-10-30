from datetime import date
import json
MONTH_NAMES = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


class Vehicle:
    def __init__(self, mark, model, year, fuel_type, tank_capacity, current_fuel):
        self.mark = mark
        self.model = model
        self.year = year
        self.fuel_type = fuel_type
        self.tank_capacity = tank_capacity
        self.current_fuel = current_fuel
        self.refuel_history = []
        self.refuel_history_by_month = {}

    def refuel(self, fuel_amount):
        self.current_fuel = min(self.current_fuel + fuel_amount, self.tank_capacity)
        refuel_date = date.today()
        self.refuel_history.append((refuel_date, fuel_amount))
        # self.get_refuel_history_by_month()
        self.save_to_json("fleet.json")

    def get_refuel_history(self):
        return self.refuel_history

    def get_refuel_history_by_month(self):
        # check if previously calculated data exists in JSON file
        if self.refuel_history_by_month:
            return self.refuel_history_by_month

        # calculate the refuel history by month
        refuel_history_by_month = {"Petrol": [0] * 12, "Diesel": [0] * 12, "Electro": [0] * 12}
        for refuel_date, fuel_amount in self.refuel_history:
            month_index = refuel_date.month - 1
            fuel_type = self.fuel_type
            refuel_history_by_month[fuel_type][month_index] += fuel_amount
        refuel_history_by_month = {fuel_type: dict(zip(MONTH_NAMES, refuel_history)) for fuel_type, refuel_history in
                                   refuel_history_by_month.items()}

        # store calculated data in JSON file
        self.refuel_history_by_month = refuel_history_by_month
        self.save_to_json("fleet.json")

        return refuel_history_by_month

    def save_to_json(self, filename):
        with open(filename, "r") as f:
            data = json.load(f)

        for vehicle_data in data["cars"] + data["trucks"] + data["buses"]:
            if vehicle_data["mark"] == self.mark and vehicle_data["model"] == self.model:
                vehicle_data["current_fuel"] = self.current_fuel
                vehicle_data["refuel_history"] = self.refuel_history
                vehicle_data["refuel_history_by_month"] = self.refuel_history_by_month
                break

        with open(filename, "w") as f:
            json.dump(data, f, indent=4, default=str)
