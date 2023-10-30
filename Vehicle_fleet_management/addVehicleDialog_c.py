from PyQt5 import QtWidgets, QtCore
from car_c import Car
from truck_c import Truck
from bus_c import Bus



class AddVehicleDialog(QtWidgets.QDialog):
    def __init__(self, fleet):
        super().__init__()
        self.fleet = fleet
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Add vehicle")
        self.setGeometry(100, 100, 300, 200)

        self.mark_label = QtWidgets.QLabel("Mark:")
        self.mark_input = QtWidgets.QLineEdit()

        self.model_label = QtWidgets.QLabel("Model:")
        self.model_input = QtWidgets.QLineEdit()

        self.year_label = QtWidgets.QLabel("Made(year):")
        self.year_input = QtWidgets.QSpinBox()
        self.year_input.setRange(1900, 2023)

        self.fuel_type_label = QtWidgets.QLabel("Type fuel:")
        self.fuel_type_input = QtWidgets.QComboBox()
        self.fuel_type_input.addItems(["Petrol", "Diesel", "Electro"])

        self.tank_capacity_label = QtWidgets.QLabel("Tank capacity (l):")
        self.tank_capacity_input = QtWidgets.QSpinBox()
        self.tank_capacity_input.setRange(1, 1000)

        self.ok_button = QtWidgets.QPushButton("OK")
        self.ok_button.clicked.connect(self.ok_button_clicked)

        self.cancel_button = QtWidgets.QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)

        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.mark_label, 0, 0)
        layout.addWidget(self.mark_input, 0, 1)
        layout.addWidget(self.model_label, 1, 0)
        layout.addWidget(self.model_input, 1, 1)
        layout.addWidget(self.year_label, 2, 0)
        layout.addWidget(self.year_input, 2, 1)
        layout.addWidget(self.fuel_type_label, 3, 0)
        layout.addWidget(self.fuel_type_input, 3, 1)
        layout.addWidget(self.tank_capacity_label, 4, 0)
        layout.addWidget(self.tank_capacity_input, 4, 1)
        layout.addWidget(self.ok_button, 5, 0)
        layout.addWidget(self.cancel_button, 5, 1)

        self.setLayout(layout)

    def ok_button_clicked(self):
        mark = self.mark_input.text()
        model = self.model_input.text()
        year = self.year_input.value()
        fuel_type = self.fuel_type_input.currentText()
        tank_capacity = self.tank_capacity_input.value()
        current_fuel = 0
        vehicle_type, ok = QtWidgets.QInputDialog.getItem(self, "Vehicle type", "Select vehicle type:",
                                                          ["Car", "Truck", "Bus"], 0, False)
        if ok and vehicle_type:
            if vehicle_type == "Car":
                num_doors, ok = QtWidgets.QInputDialog.getInt(self, "Number of doors", "Enter the number of doors:", 2, 2, 5)
                if ok:
                    vehicle = Car(mark, model, year, fuel_type, tank_capacity, current_fuel, num_doors)
                    self.fleet.add_car(vehicle)
                else:
                    QtWidgets.QMessageBox.warning(self, "Error", "Enter a valid number of doors.")
                    return
            elif vehicle_type == "Truck":
                max_load, ok = QtWidgets.QInputDialog.getInt(self, "Maximum load capacity",
                                                             "Enter the maximum load capacity (kg):", 1000, 1, 100000)
                if ok:
                    vehicle = Truck(mark, model, year, fuel_type, tank_capacity, current_fuel, max_load)
                    self.fleet.add_truck(vehicle)
                else:
                    QtWidgets.QMessageBox.warning(self, "Error", "Enter a valid maximum load capacity.")
                    return
            elif vehicle_type == "Bus":
                num_passengers, ok = QtWidgets.QInputDialog.getInt(self, "Number of passengers",
                                                                   "Enter the number of passengers:", 20, 1, 200)
                if ok:
                    vehicle = Bus(mark, model, year, fuel_type, tank_capacity, current_fuel, num_passengers)
                    self.fleet.add_bus(vehicle)
                else:
                    QtWidgets.QMessageBox.warning(self, "Error", "Please enter a valid number of passengers.")
                    return
            self.accept()
