
import json
from PyQt6.QtWidgets import (QDialog, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QFormLayout,
                             QDialogButtonBox, QMessageBox, QListWidget, QListWidgetItem, QMenu)
from PyQt6.QtGui import QIntValidator, QAction
from PyQt6.QtCore import Qt


class VehicleDialog(QDialog):
    def __init__(self, vehicles, parent=None):
        super().__init__(parent)

        self.vehicles = vehicles
        self.setWindowTitle("Vehicle Management")

        self.form_layout = QFormLayout()

        self.brand_label = QLabel("Brand:")
        self.brand_edit = QLineEdit()
        self.form_layout.addRow(self.brand_label, self.brand_edit)

        self.model_label = QLabel("Model:")
        self.model_edit = QLineEdit()
        self.form_layout.addRow(self.model_label, self.model_edit)

        self.year_label = QLabel("Year:")
        self.year_edit = QLineEdit()
        self.year_edit.setValidator(QIntValidator(1900, 2023))
        self.form_layout.addRow(self.year_label, self.year_edit)

        self.button_box = QDialogButtonBox()
        # self.button_ok = self.button_box.addButton(QDialogButtonBox.StandardButton.Ok)
        self.button_ok = self.button_box.addButton("Save", QDialogButtonBox.ButtonRole.AcceptRole)
        self.button_cancel = self.button_box.addButton(QDialogButtonBox.StandardButton.Cancel)
        self.button_input_car = QPushButton("Input Car")

        self.button_box.accepted.connect(self.save_vehicle)
        self.button_box.rejected.connect(self.reject)
        self.button_input_car.clicked.connect(self.add_vehicle)

        # Connect itemClicked signal to the vehicle_item_clicked function
        self.vehicle_list = QListWidget()
        for vehicle in self.vehicles:
            self.vehicle_list.addItem(f"{vehicle['brand']} {vehicle['model']} {vehicle['year']}")

        self.vehicle_list.itemClicked.connect(self.vehicle_item_clicked)


        self.vehicle_list = QListWidget()
        for vehicle in self.vehicles:
            self.vehicle_list.addItem(f"{vehicle['brand']} {vehicle['model']} {vehicle['year']}")

        self.layout = QVBoxLayout()
        self.layout.addLayout(self.form_layout)
        self.layout.addWidget(self.button_input_car)
        self.layout.addWidget(self.vehicle_list)

        # Add these lines after creating the vehicle_list widget
        self.button_edit = QPushButton("Edit")
        self.button_delete = QPushButton("Delete")
        self.button_edit.clicked.connect(self.edit_selected_vehicle)
        self.button_delete.clicked.connect(self.delete_selected_vehicle)

        # Add the new buttons to the layout
        self.layout.addWidget(self.vehicle_list)
        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.button_edit)
        self.button_layout.addWidget(self.button_delete)
        self.layout.addLayout(self.button_layout)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.button_ok)
        self.button_layout.addWidget(self.button_cancel)
        self.layout.addLayout(self.button_layout)

        self.setLayout(self.layout)

    def save_vehicle(self):
        with open("vehicles.json", "w") as file:
            json.dump(self.vehicles, file)
        self.accept()


    def add_vehicle(self):
        if self.validate_inputs():
            vehicle_data = self.get_vehicle_data()
            self.vehicles.append(vehicle_data)
            self.vehicle_list.addItem(f"{vehicle_data['brand']} {vehicle_data['model']} {vehicle_data['year']}")
            self.clear_inputs()
        else:
            QMessageBox.warning(self, "Warning", "Please fill in all fields.")

    def get_vehicle_data(self):
        return {
            'brand': self.brand_edit.text(),
            'model': self.model_edit.text(),
            'year': self.year_edit.text()
        }

    def validate_inputs(self):
        return bool(self.brand_edit.text() and self.model_edit.text() and self.year_edit.text())

    def clear_inputs(self):
        self.brand_edit.clear()
        self.model_edit.clear()
        self.year_edit.clear()

    def vehicle_item_clicked(self, item):
        menu = QMenu()
        delete_action = QAction("Delete")
        edit_action = QAction("Edit")

        delete_action.triggered.connect(lambda: self.delete_vehicle(item))
        edit_action.triggered.connect(lambda: self.edit_vehicle(item))

        menu.addAction(edit_action)
        menu.addAction(delete_action)
        menu.exec(Qt.GlobalPos())

    def delete_vehicle(self, item):
        row = self.vehicle_list.row(item)
        del self.vehicles[row]
        self.vehicle_list.takeItem(row)

    def edit_vehicle(self, item):
        row = self.vehicle_list.row(item)
        vehicle = self.vehicles[row]

        self.brand_edit.setText(vehicle['brand'])
        self.model_edit.setText(vehicle['model'])
        self.year_edit.setText(vehicle['year'])

        self.button_input_car.clicked.disconnect()
        self.button_input_car.clicked.connect(lambda: self.update_vehicle(row))

    def update_vehicle(self, row):
        if self.validate_inputs():
            vehicle_data = self.get_vehicle_data()
            self.vehicles[row] = vehicle_data
            self.vehicle_list.item(row).setText(
                f"{vehicle_data['brand']} {vehicle_data['model']} {vehicle_data['year']}")
            self.clear_inputs()

            self.button_input_car.clicked.disconnect()
            self.button_input_car.clicked.connect(self.add_vehicle)
    @staticmethod
    def load_vehicles():
        try:
            with open("vehicles.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def edit_selected_vehicle(self):
        selected_items = self.vehicle_list.selectedItems()
        if selected_items:
            self.edit_vehicle(selected_items[0])

    def delete_selected_vehicle(self):
        selected_items = self.vehicle_list.selectedItems()
        if selected_items:
            self.delete_vehicle(selected_items[0])
