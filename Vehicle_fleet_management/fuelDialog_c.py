from PyQt5 import QtWidgets


class FuelDialog(QtWidgets.QDialog):
    def __init__(self, vehicle):
        super().__init__()
        self.vehicle = vehicle
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Refuel")
        self.setGeometry(100, 100, 200, 100)

        self.label = QtWidgets.QLabel(
            f"Enter the amount of fuel (max. {self.vehicle.tank_capacity - self.vehicle.current_fuel}):")
        self.fuel_input = QtWidgets.QSpinBox()
        self.fuel_input.setRange(1, self.vehicle.tank_capacity - self.vehicle.current_fuel)
        self.fuel_input.setSuffix(" l")

        self.ok_button = QtWidgets.QPushButton("OK")
        self.cancel_button = QtWidgets.QPushButton("Cancel")

        self.ok_button.clicked.connect(self.ok_button_clicked)
        self.cancel_button.clicked.connect(self.cancel_button_clicked)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.fuel_input)
        layout.addWidget(self.ok_button)
        layout.addWidget(self.cancel_button)
        self.setLayout(layout)

    def ok_button_clicked(self):
        fuel_amount = self.fuel_input.value()
        self.vehicle.refuel(fuel_amount)
        self.accept()

    def cancel_button_clicked(self):
        self.reject()
