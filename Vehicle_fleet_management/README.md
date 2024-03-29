This program is a vehicle fleet management application with a graphical user interface (GUI) built using PyQt5. It allows users to manage a fleet of different types of vehicles (cars, trucks, buses) by performing several actions:

- Add a new vehicle to the fleet.
- View all vehicles within each category (cars, trucks, buses).
- Refuel a vehicle and log the refueling history.
- Show total fuel consumption and fuel consumption by month for all vehicles.
- Save the fleet data to a JSON file.

The `MainWindow` class is the main window of the application, offering buttons for each functionality, such as adding a new vehicle, showing all vehicles, and refueling operations. The `AddVehicleDialog` class is a dialog window that captures the information necessary to add a new vehicle, like the make, model, year, fuel type, and tank capacity.

The fleet of vehicles is managed by the `Fleet` class, which maintains separate lists for cars, trucks, and buses. It also provides functionality to save the current state of the fleet to a JSON file, ensuring data persistence between sessions.

The `Vehicle` class and its subclasses `Car`, `Truck`, and `Bus` represent the different types of vehicles. Each has attributes suitable for their category, such as `num_doors` for cars, `max_load` for trucks, and `num_passengers` for buses.

The `FuelDialog` class is used to input the amount of fuel when refueling a vehicle. It updates the vehicle's current fuel level and records the refueling event.

Overall, this application is designed to streamline the process of managing a diverse vehicle fleet with a user-friendly interface.
