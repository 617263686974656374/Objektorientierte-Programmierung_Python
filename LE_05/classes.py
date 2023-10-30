class Vehicle:
    def __init__(self, brand, model, Year):
        self.brand = brand
        self.model = model
        self.Year = Year

class Customer:
    def __init__(self, name, address, mobil):
        self.name = name
        self.address = address
        self.mobil = mobil

class Reservation:
    def __init__(self, customer, vehicle, start_date, end_date):
        self.customer = customer
        self.vehicle = vehicle
        self.start_date = start_date
        self.end_date = end_date
