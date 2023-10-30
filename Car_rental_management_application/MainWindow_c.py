import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QPushButton, QVBoxLayout
from VehicleDialog_c import *
from CustomerDialog_c import *
from ReservationDialog_c import *
from classes import *
class Car_rental_management(QMainWindow):
    def __init__(self):
        super().__init__()
        self.vehicles = []
        self.customers = []
        self.reservations = []
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        vehicle_button = QPushButton('Vehicle Management')
        customer_button = QPushButton('Customer Management')
        reservation_button = QPushButton('Reservation Management')

        layout.addWidget(vehicle_button)
        layout.addWidget(customer_button)
        layout.addWidget(reservation_button)

        central_widget.setLayout(layout)

        vehicle_button.clicked.connect(self.vehicle_management)
        customer_button.clicked.connect(self.customer_management)
        reservation_button.clicked.connect(self.reservation_management)

        self.setWindowTitle('Car Rental Management')
        self.show()

    def vehicle_management(self):
        # Load vehicles from JSON file
        self.vehicles = VehicleDialog.load_vehicles()

        # Open the vehicle management window
        vehicle_dialog = VehicleDialog(self.vehicles, self)
        if vehicle_dialog.exec() == QDialog.DialogCode.Accepted:
            vehicle_data = vehicle_dialog.get_vehicle_data()
            self.vehicles.append(vehicle_data)

    def customer_management(self):
        # Load vehicles from JSON file
        self.customers = CustomerDialog.load_customers()
        # Open the customer management window
        customer_dialog = CustomerDialog(self.customers, self)
        if customer_dialog.exec() == QDialog.DialogCode.Accepted:
            customer_data = customer_dialog.get_customer_data()
            self.customers.append(customer_data)

    def reservation_management(self):
        reservations = ReservationDialog.load_reservations()
        reservation_dialog = ReservationDialog(self)
        reservation_dialog.exec()
