
import json
from PyQt6.QtWidgets import (QDialog, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QFormLayout,
                             QDialogButtonBox, QMessageBox, QListWidget, QListWidgetItem, QMenu, QComboBox, QDateTimeEdit)
from PyQt6.QtGui import QIntValidator, QAction, QCursor
from PyQt6.QtCore import Qt, QDateTime


class ReservationDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.vehicles = self.load_vehicles()
        self.customers = self.load_customers()
        self.reservations = self.load_reservations()

        self.setWindowTitle("Reservation Management")

        self.form_layout = QFormLayout()

        self.vehicle_label = QLabel("Vehicle:")
        self.vehicle_combo = QComboBox()
        for vehicle in self.vehicles:
            self.vehicle_combo.addItem(
                f"{vehicle['brand']} {vehicle['model']} ({vehicle['year']})"
            )
        self.form_layout.addRow(self.vehicle_label, self.vehicle_combo)

        self.customer_label = QLabel("Customer:")
        self.customer_combo = QComboBox()
        for customer in self.customers:
            self.customer_combo.addItem(
                f"{customer['name']} ({customer['mobil']})"
            )
        self.form_layout.addRow(self.customer_label, self.customer_combo)

        self.start_date_label = QLabel("Start Date:")
        self.start_date_edit = QDateTimeEdit(QDateTime.currentDateTime())
        self.form_layout.addRow(self.start_date_label, self.start_date_edit)

        self.end_date_label = QLabel("End Date:")
        self.end_date_edit = QDateTimeEdit(QDateTime.currentDateTime())
        self.form_layout.addRow(self.end_date_label, self.end_date_edit)

        self.button_box = QDialogButtonBox()
        # self.button_ok = self.button_box.addButton(QDialogButtonBox.StandardButton.Ok)
        self.button_ok = self.button_box.addButton("Save", QDialogButtonBox.ButtonRole.AcceptRole)
        self.button_cancel = self.button_box.addButton(QDialogButtonBox.StandardButton.Cancel)
        self.button_input_reservation = QPushButton("Input Reservation")

        self.button_box.accepted.connect(self.save_reservations)
        self.button_box.rejected.connect(self.reject)
        self.button_input_reservation.clicked.connect(self.add_reservation)
        self.start_date_edit.dateTimeChanged.connect(self.update_end_date_minimum)


        self.reservation_list = QListWidget()
        for reservation in self.reservations:
            self.reservation_list.addItem(
                f"{reservation['customer']['name']} - {reservation['vehicle']['brand']} {reservation['vehicle']['model']} ({reservation['start_date']} - {reservation['end_date']})"
            )

        self.layout = QVBoxLayout()
        self.layout.addLayout(self.form_layout)
        self.layout.addWidget(self.button_input_reservation)
        self.layout.addWidget(self.reservation_list)

        self.button_edit = QPushButton("Edit")
        self.button_delete = QPushButton("Delete")
        self.button_edit.clicked.connect(self.edit_selected_reservation)
        self.button_delete.clicked.connect(self.delete_selected_reservation)

        self.layout.addWidget(self.reservation_list)
        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.button_edit)
        self.button_layout.addWidget(self.button_delete)
        self.layout.addLayout(self.button_layout)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.button_ok)
        self.button_layout.addWidget(self.button_cancel)
        self.layout.addLayout(self.button_layout)

        self.setLayout(self.layout)

        self.update_end_date_minimum()
    def save_reservations(self):
        with open("reservation.json", "w") as file:
            json.dump(self.reservations, file)

        for reservation_data in self.reservations:
            vehicle = reservation_data['vehicle']
            customer = reservation_data['customer']

            for v in self.vehicles:
                if v == vehicle:
                    v['reserved'] = True
                    v['reserved_from'] = reservation_data['start_date']
                    v['reserved_to'] = reservation_data['end_date']
                    break

            for c in self.customers:
                if c == customer:
                    c['has_reservation'] = True
                    break

        self.accept()

    def add_reservation(self):
        reservation_data = self.get_reservation_data()

        if self.is_vehicle_available(reservation_data['vehicle'], reservation_data['start_date'], reservation_data['end_date']):
            self.reservations.append(reservation_data)
            self.reservation_list.addItem(
                f"{reservation_data['customer']['name']} - {reservation_data['vehicle']['brand']} {reservation_data['vehicle']['model']} ({reservation_data['start_date']} - {reservation_data['end_date']})"
            )
        else:
            QMessageBox.warning(self, "Error", "Vehicle is already reserved for the selected time period.")


    def get_reservation_data(self):
        return {
            'vehicle': self.vehicles[self.vehicle_combo.currentIndex()],
            'customer': self.customers[self.customer_combo.currentIndex()],
            'start_date': self.start_date_edit.dateTime().toString("yyyy-MM-dd hh:mm"),
            'end_date': self.end_date_edit.dateTime().toString("yyyy-MM-dd hh:mm")
        }

    def delete_reservation(self, item):
        row = self.reservation_list.row(item)
        del self.reservations[row]
        self.reservation_list.takeItem(row)

    def edit_selected_reservation(self):
        selected_items = self.reservation_list.selectedItems()
        if selected_items:
            row = self.reservation_list.row(selected_items[0])
            reservation = self.reservations[row]

            vehicle_index = self.vehicles.index(reservation['vehicle'])
            customer_index = self.customers.index(reservation['customer'])
            self.vehicle_combo.setCurrentIndex(vehicle_index)
            self.customer_combo.setCurrentIndex(customer_index)
            self.start_date_edit.setDateTime(QDateTime.fromString(reservation['start_date'], "yyyy-MM-dd hh:mm"))
            self.end_date_edit.setDateTime(QDateTime.fromString(reservation['end_date'], "yyyy-MM-dd hh:mm"))

            self.button_input_reservation.clicked.disconnect()
            self.button_input_reservation.clicked.connect(lambda: self.update_reservation(row))


    def update_reservation(self, row):
        reservation_data = self.get_reservation_data()
        self.reservations[row] = reservation_data
        self.reservation_list.item(row).setText(
            f"{reservation_data['customer']['name']} - {reservation_data['vehicle']['brand']} {reservation_data['vehicle']['model']} ({reservation_data['start_date']} - {reservation_data['end_date']})"
        )

        self.button_input_reservation.clicked.disconnect()
        self.button_input_reservation.clicked.connect(self.add_reservation)

    @staticmethod
    def load_reservations():
        try:
            with open("reservation.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    @staticmethod
    def load_vehicles():
        try:
            with open("vehicles.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    @staticmethod
    def load_customers():
        try:
            with open("customers.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def delete_selected_reservation(self):
        selected_items = self.reservation_list.selectedItems()
        if selected_items:
            self.delete_reservation(selected_items[0])

    def is_vehicle_available(self, vehicle, start_date, end_date):
        start_date = QDateTime.fromString(start_date, "yyyy-MM-dd hh:mm")
        end_date = QDateTime.fromString(end_date, "yyyy-MM-dd hh:mm")

        for reservation in self.reservations:
            if reservation['vehicle'] == vehicle:
                reservation_start_date = QDateTime.fromString(reservation['start_date'], "yyyy-MM-dd hh:mm")
                reservation_end_date = QDateTime.fromString(reservation['end_date'], "yyyy-MM-dd hh:mm")

                if (start_date >= reservation_start_date and start_date < reservation_end_date) or \
                   (end_date > reservation_start_date and end_date <= reservation_end_date) or \
                   (start_date <= reservation_start_date and end_date >= reservation_end_date):
                    return False
        return True

    def update_end_date_minimum(self):
        self.end_date_edit.setMinimumDateTime(self.start_date_edit.dateTime())
