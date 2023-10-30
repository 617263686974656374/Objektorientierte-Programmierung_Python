#The program is a simple vehicle management system consisting of a `Garage` 
#class and several subclasses representing different types of vehicles. 
#It tracks each vehicle's details and the total number of vehicles. 
#It allows creating individual vehicle objects with specific attributes 
#and provides a method to print out these details. 
#The subclasses include `PKW` for cars, `LKW` for trucks, `Motorrad` for motorcycles,
#and `Fahrrad` for bicycles. The program also attempts to track the count of each type of vehicle and the total count of all vehicles.


class Garage:
    Type_count = 0
    Total_count = 0

    @classmethod
    def IncreaseTypeCount(cls):
        cls.Type_count += 1

    def __init__(self, type, make, colour, plate, location, fuel, km):
        self.type = type
        self.make = make
        self.colour = colour
        self.plate = plate
        self.location = location
        self.fuel = fuel
        self.km = km
        self.IncreaseTypeCount()
        Garage.Total_count += 1

    def printcar(self):
        print(f"Art: {self.type}\n"
        f"Marke: {self.make}\n"
        f"Farbe: {self.colour}\n"
        f"Kennzeichen: {self.plate}\n"
        f"Stellplatz: {self.location}\n"
        f"Tank: {self.fuel}\n"
        f"Kilometerstand: {self.km}\n"
        f"Anzahl {self.type}: {self.Type_count}\n"
        f"Fahrzeuge gesamt: {Garage.Total_count}\n")

class PKW(Garage):
    pass


class LKW(Garage):
    pass


class Motorrad(Garage):
    pass


class Fahrrad(Garage):
    def __init__(self, type, make, colour, location):
        self.type = type
        self.make = make
        self.colour = colour
        self.location = location
        self.IncreaseTypeCount()
        Garage.Total_count += 1

    def printcar(self):
        print(f"Art: {self.type}\n"
        f"Marke: {self.make}\n"
        f"Farbe: {self.colour}\n"
        f"Stellplatz: {self.location}\n"
        f"Anzahl {self.type}: {self.Type_count}\n"
        f"Fahrzeuge gesamt: {Garage.Total_count}\n")

vehicle_0 = PKW("PKW", "Mercedes", "weiß", "G-239DS", "A1", "35 L", "123000 Km")
vehicle_1 = PKW("PKW", "Audi", "grau", "G-903UZ", "A2", "24 L", "56000 Km")
vehicle_2 = PKW("PKW", "Bmw", "schwarz", "G-736AL", "A3", "58 L", "84000 Km")
vehicle_3 = PKW("PKW", "VW", "pink", "G-378BT", "A4", "33 L", "152000 Km")
vehicle_4 = PKW("PKW", "Volvo", "blau", "G-823KS", "A5", "42 L", "42000 Km")
vehicle_5 = LKW("LKW", "Mercedes", "weiß", "G-378JJ", "B1", "67 L", "273000Km ")
vehicle_6 = LKW("LKW", "Mercedes", "grün", "G-329GZ", "B2", "53 L", "99000 Km")
vehicle_7 = LKW("LKW", "Mercedes", "rot", "G-384OP", "B3", "73 L", "123000 Km")
vehicle_8 = Motorrad("Motorrad", "Kawasaki", "grün", "G-4KJ3", "C1", "17 L", "20000 Km")
vehicle_9 = Motorrad("Motorrad", "Yamaha", "blau", "G-T93L", "C2", "12 L", "7300 Km")
vehicle_10 = Fahrrad("Fahrrad", "KTM", "orange", "D1")
