from PyQt5 import QtWidgets
import json
from car_c import Car
from truck_c import Truck
from bus_c import Bus

class Fleet:
    def __init__(self):
        self.cars = []
        self.trucks = []
        self.buses = []

        try:
            with open("fleet.json", "r") as f:
                data = json.load(f)

            for vehicle_data in data["cars"]:
                vehicle = Car(**vehicle_data)
                self.add_car(vehicle)

            for vehicle_data in data["trucks"]:
                vehicle = Truck(**vehicle_data)
                self.add_truck(vehicle)

            for vehicle_data in data["buses"]:
                vehicle = Bus(**vehicle_data)
                self.add_bus(vehicle)

        except FileNotFoundError:
            pass

    def save_to_json(self, filename):
        data = {
            "cars": [vars(car) for car in self.cars],
            "trucks": [vars(truck) for truck in self.trucks],
            "buses": [vars(bus) for bus in self.buses],
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4, default=str)

        # save the refuel_history_by_month in the instance to avoid recalculation
        for vehicle in self.cars + self.trucks + self.buses:
            if vehicle.refuel_history_by_month:
                vehicle_data = next(filter(lambda x: x["mark"] == vehicle.mark and x["model"] == vehicle.model,
                                           data["cars"] + data["trucks"] + data["buses"]), None)
                if vehicle_data is not None:
                    vehicle_data["refuel_history_by_month"] = vehicle.refuel_history_by_month

    def refuel_all(self, fuel_amount):
        for vehicle in self.cars + self.trucks + self.buses:
            vehicle.refuel(fuel_amount)
        self.save_to_json("fleet.json")

    def add_car(self, car):
        self.cars.append(car)
        self.save_to_json("fleet.json")

    def add_truck(self, truck):
        self.trucks.append(truck)
        self.save_to_json("fleet.json")

    def add_bus(self, bus):
        self.buses.append(bus)
        self.save_to_json("fleet.json")

    def show_cars(self):
        car_info = "\n".join([f"{car.mark} {car.model} ({car.year}) - {car.current_fuel}/{car.tank_capacity} {car.fuel_type} - {car.num_doors} doors" for car in self.cars])
        QtWidgets.QMessageBox.information(None, "Cars", car_info)

    def show_trucks(self):
        truck_info = "\n".join([f"{truck.mark} {truck.model} ({truck.year}) - {truck.current_fuel}/{truck.tank_capacity} {truck.fuel_type} - maximum weight: {truck.max_load} kg" for truck in self.trucks])
        QtWidgets.QMessageBox.information(None, "Trucks", truck_info)

    def show_buses(self):
        bus_info = "\n".join([f"{bus.mark} {bus.model} ({bus.year}) - {bus.current_fuel}/{bus.tank_capacity} {bus.fuel_type} - maximum passengers: {bus.num_passengers}" for bus in self.buses])
        QtWidgets.QMessageBox.information(None, "Buses", bus_info)
