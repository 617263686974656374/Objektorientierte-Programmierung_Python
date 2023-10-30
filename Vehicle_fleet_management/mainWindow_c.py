from PyQt5 import QtWidgets
from fleet_c import Fleet
from fuelDialog_c import FuelDialog
from addVehicleDialog_c import AddVehicleDialog


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.fleet = Fleet()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Car park")
        self.setGeometry(100, 100, 300, 200)

        self.add_vehicle_button = QtWidgets.QPushButton("Add Car")
        self.add_vehicle_button.clicked.connect(self.add_vehicle_button_clicked)

        self.show_cars_button = QtWidgets.QPushButton("Show cars")
        self.show_cars_button.clicked.connect(self.show_cars_button_clicked)

        self.show_trucks_button = QtWidgets.QPushButton("Show trucks")
        self.show_trucks_button.clicked.connect(self.show_trucks_button_clicked)

        self.show_buses_button = QtWidgets.QPushButton("Show buses")
        self.show_buses_button.clicked.connect(self.show_buses_button_clicked)

        # Add refuel button
        self.refuel_button = QtWidgets.QPushButton("Add fuel")
        self.refuel_button.clicked.connect(self.refuel_button_clicked)

        # Add fuel consumption button
        self.show_fuel_consumption_button = QtWidgets.QPushButton("Show fuel consumption")
        self.show_fuel_consumption_button.clicked.connect(self.show_fuel_consumption_button_clicked)

        # Add fuel by month button
        self.fuel_by_month_button = QtWidgets.QPushButton("Fuel by month")
        self.fuel_by_month_button.clicked.connect(self.fuel_by_month_button_clicked)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.add_vehicle_button)
        layout.addWidget(self.show_cars_button)
        layout.addWidget(self.show_trucks_button)
        layout.addWidget(self.show_buses_button)
        layout.addWidget(self.refuel_button) # add refuel button to layout
        layout.addWidget(self.show_fuel_consumption_button) # add fuel consumption
        layout.addWidget(self.fuel_by_month_button)

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def add_vehicle_button_clicked(self):
        dialog = AddVehicleDialog(self.fleet)
        dialog.exec_()

    def show_cars_button_clicked(self):
        self.fleet.show_cars()

    def show_trucks_button_clicked(self):
        self.fleet.show_trucks()

    def show_buses_button_clicked(self):
        self.fleet.show_buses()

    def cancel_button_clicked(self):
        self.reject()

    def refuel_button_clicked(self):
        vehicles = self.fleet.cars + self.fleet.trucks + self.fleet.buses
        if not vehicles:
            QtWidgets.QMessageBox.warning(self, "Error", "There are no vehicles available.")
            return
        vehicle_names = [f"{type(vehicle).__name__} {vehicle.mark} {vehicle.model}" for vehicle in vehicles]
        selected_vehicle_name, ok = QtWidgets.QInputDialog.getItem(
            self, "Select a vehicle", "Select the vehicle you want to refuel:", vehicle_names, 0, False)
        if ok and selected_vehicle_name:
            for vehicle in vehicles:
                if f"{type(vehicle).__name__} {vehicle.mark} {vehicle.model}" == selected_vehicle_name:
                    dialog = FuelDialog(vehicle)
                    dialog.exec_()
                    break

    def show_fuel_consumption_button_clicked(self):
        total_fuel_consumption = sum(
            vehicle.current_fuel for vehicle in self.fleet.cars + self.fleet.trucks + self.fleet.buses)
        QtWidgets.QMessageBox.information(self, "Fuel consumption",
                                          f"Total fuel consumption is {total_fuel_consumption} liters.")

    def fuel_by_month_button_clicked(self):
        fuel_by_month = {}
        for vehicle in self.fleet.cars + self.fleet.trucks + self.fleet.buses:
            if hasattr(vehicle, 'get_refuel_history_by_month'):
                fuel_history_by_month = vehicle.get_refuel_history_by_month()
                for fuel_type, fuel_data in fuel_history_by_month.items():
                    if fuel_type not in fuel_by_month:
                        fuel_by_month[fuel_type] = {}
                    for month, fuel_amount in fuel_data.items():
                        if month not in fuel_by_month[fuel_type]:
                            fuel_by_month[fuel_type][month] = 0
                        fuel_by_month[fuel_type][month] += fuel_amount
        message = ""
        for fuel_type, fuel_data in fuel_by_month.items():
            message += f"{fuel_type}\n"
            for month, fuel_amount in fuel_data.items():
                message += f"{month}: {fuel_amount}\n"
            message += "\n"
        QtWidgets.QMessageBox.information(self, "Fuel by month", message)
