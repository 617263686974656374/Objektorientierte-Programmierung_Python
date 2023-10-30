
from Function_c import *


class DepositWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Deposit Account")
        self.setGeometry(100, 100, 300, 200)

        self.withdraw_account_button = QPushButton("Deposit account")
        self.withdraw_account_button.clicked.connect(self.withdraw_account_button_clicked)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)

        self.account_name_label = QLabel('Choose account:')
        self.account_combo_box = QComboBox()
        self.account_combo_box.addItem("Choose account")


        accounts = Function.accounts  # získání seznamu účtů
        for account in accounts:
            self.account_combo_box.addItem(
                f"{account['name']} {account['surname']}")
        self.account_combo_box.currentIndexChanged.connect(self.update_balance_label)

        label_combo_layout = QHBoxLayout()
        label_combo_layout.addWidget(self.account_name_label)
        label_combo_layout.addWidget(self.account_combo_box)

        self.text_input_label = QLabel('Entry deposit')
        self.text_input = QLineEdit()
        self.text_input.setValidator(QIntValidator(0, 1000000))
        self.text_input.setText(str(0))

        text_input_layout = QHBoxLayout()
        text_input_layout.addWidget(self.text_input_label)
        text_input_layout.addWidget(self.text_input)

        self.balance_label = QLabel()

        account_layout = QVBoxLayout()
        account_layout.addLayout(label_combo_layout)
        account_layout.addLayout(text_input_layout)
        account_layout.addWidget(self.balance_label)
        account_layout.addWidget(self.withdraw_account_button)
        account_layout.addWidget(self.cancel_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(account_layout)

        self.setLayout(main_layout)

    def update_balance_label(self, index):
        if index > 0:
            selected_account = Function.accounts[index-1]['account']
            self.balance_label.setText(f"Account balance: {selected_account.get_balance()} euro")
        else:
            self.balance_label.setText("Account balance: 0 euro")

    def withdraw_account_button_clicked(self):
        index = self.account_combo_box.currentIndex()
        if index == 0:
            QMessageBox.warning(self, "Warning", "Please select an account")
            return

        amount = int(self.text_input.text())
        selected_account = Function.accounts[index - 1]['account']
        Function.deposit_money(selected_account, amount)

        Function.save_accounts_to_file(Function.accounts)
        self.update_balance_label(index)
        self.text_input.setText(str(0))
        QMessageBox.information(self, "Success", f"Deposit of {amount} euro was successful")

