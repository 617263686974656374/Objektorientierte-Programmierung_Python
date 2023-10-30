
from Function_c import *


class DeleteWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Delete account")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.account_combo_box = QComboBox()
        self.account_combo_box.addItem("Choose account")

        accounts = Function.accounts  # získání seznamu účtů
        for account in accounts:
            self.account_combo_box.addItem(
                f"{account['name']} {account['surname']}")

        layout.addWidget(self.account_combo_box)

        self.delete_button = QPushButton("Delete")
        self.delete_button.clicked.connect(self.delete_button_clicked)
        layout.addWidget(self.delete_button)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)
        layout.addWidget(self.cancel_button)

        self.setLayout(layout)

    def delete_button_clicked(self):
        selected_account = self.account_combo_box.currentText()
        name, surname = selected_account.split(' ')
        if Function.delete_account(name, surname):
            Function.save_accounts_to_file(Function.accounts)  # uloží změny do JSON souboru
            self.account_combo_box.removeItem(self.account_combo_box.currentIndex())  # odstraní účet z comboboxu
            self.accept()
        else:
            QMessageBox.warning(self, 'Chyba', f"Účet {selected_account} neexistuje!")

