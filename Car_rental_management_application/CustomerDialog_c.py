
import json
from PyQt6.QtWidgets import (QDialog, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QFormLayout,
                             QDialogButtonBox, QMessageBox, QListWidget, QListWidgetItem, QMenu)
from PyQt6.QtGui import QIntValidator, QAction
from PyQt6.QtCore import Qt


class CustomerDialog(QDialog):
    def __init__(self, customers, parent=None):
        super().__init__(parent)

        self.customers = customers
        self.setWindowTitle("Customer Management")

        self.form_layout = QFormLayout()

        self.name_label = QLabel("Name:")
        self.name_edit = QLineEdit()
        self.form_layout.addRow(self.name_label, self.name_edit)

        self.address_label = QLabel("Address:")
        self.address_edit = QLineEdit()
        self.form_layout.addRow(self.address_label, self.address_edit)

        self.mobil_label = QLabel("Mobile:")
        self.mobil_edit = QLineEdit()
        self.mobil_edit.setValidator(QIntValidator(1111, 9999999))
        self.form_layout.addRow(self.mobil_label, self.mobil_edit)

        self.button_box = QDialogButtonBox()
        # self.button_ok = self.button_box.addButton(QDialogButtonBox.StandardButton.Ok)
        self.button_ok = self.button_box.addButton("Save", QDialogButtonBox.ButtonRole.AcceptRole)

        self.button_cancel = self.button_box.addButton(QDialogButtonBox.StandardButton.Cancel)
        self.button_input_customer = QPushButton("Input Customer")

        self.button_box.accepted.connect(self.save_customers)
        self.button_box.rejected.connect(self.reject)
        self.button_input_customer.clicked.connect(self.add_customer)

        # Connect itemClicked signal to the vehicle_item_clicked function
        self.customer_list = QListWidget()
        for customer in self.customers:
            self.customer_list.addItem(f"{customer['name']} {customer['address']} ({customer['mobil']})")

        self.customer_list.itemClicked.connect(self.customer_item_clicked)


        self.customer_list = QListWidget()
        for customer in self.customers:
            self.customer_list.addItem(f"{customer['name']} {customer['address']} ({customer['mobil']})")


        self.layout = QVBoxLayout()
        self.layout.addLayout(self.form_layout)
        self.layout.addWidget(self.button_input_customer)
        self.layout.addWidget(self.customer_list)


        # Add these lines after creating the vehicle_list widget
        self.button_edit = QPushButton("Edit")
        self.button_delete = QPushButton("Delete")
        self.button_edit.clicked.connect(self.edit_selected_customer)
        self.button_delete.clicked.connect(self.delete_selected_customer)

        # Add the new buttons to the layout
        self.layout.addWidget(self.customer_list)
        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.button_edit)
        self.button_layout.addWidget(self.button_delete)
        self.layout.addLayout(self.button_layout)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.button_ok)
        self.button_layout.addWidget(self.button_cancel)
        self.layout.addLayout(self.button_layout)

        self.setLayout(self.layout)

    def save_customers(self):
        with open("customers.json", "w") as file:
            json.dump(self.customers, file)
        self.accept()

    def add_customer(self):
        if self.validate_inputs():
            customer_data = self.get_customer_data()
            self.customers.append(customer_data)
            self.customer_list.addItem(f"{customer_data['name']} {customer_data['address']} ({customer_data['mobil']})")
            self.clear_inputs()
        else:
            QMessageBox.warning(self, "Warning", "Please fill in all fields.")

    def get_customer_data(self):
        return {
            'name': self.name_edit.text(),
            'address': self.address_edit.text(),
            'mobil': self.mobil_edit.text()
        }

    def validate_inputs(self):
        return bool(self.name_edit.text() and self.address_edit.text() and self.mobil_edit.text())

    def clear_inputs(self):
        self.name_edit.clear()
        self.address_edit.clear()
        self.mobil_edit.clear()

    def customer_item_clicked(self, item):
        menu = QMenu()
        delete_action = QAction("Delete")
        edit_action = QAction("Edit")

        delete_action.triggered.connect(lambda: self.delete_customer(item))
        edit_action.triggered.connect(lambda: self.edit_customer(item))

        menu.addAction(edit_action)
        menu.addAction(delete_action)
        menu.exec(Qt.GlobalPos())

    def delete_customer(self, item):
        row = self.customer_list.row(item)
        del self.customers[row]
        self.customer_list.takeItem(row)

    def edit_customer(self, item):
        row = self.customer_list.row(item)
        vehicle = self.customers[row]

        self.name_edit.setText(vehicle['name'])
        self.address_edit.setText(vehicle['address'])
        self.mobil_edit.setText(vehicle['mobil'])

        self.button_input_customer.clicked.disconnect()
        self.button_input_customer.clicked.connect(lambda: self.update_customer(row))

    def update_customer(self, row):
        if self.validate_inputs():
            customer_data = self.get_customer_data()
            self.customers[row] = customer_data
            self.customer_list.item(row).setText(
                f"{customer_data['name']} {customer_data['address']} ({customer_data['mobil']})")
            self.clear_inputs()

            self.button_input_customer.clicked.disconnect()
            self.button_input_customer.clicked.connect(self.add_customer)

    @staticmethod
    def load_customers():
        try:
            with open("customers.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def edit_selected_customer(self):
        selected_items = self.customer_list.selectedItems()
        if selected_items:
            self.edit_customer(selected_items[0])

    def delete_selected_customer(self):
        selected_items = self.customer_list.selectedItems()
        if selected_items:
            self.delete_customer(selected_items[0])