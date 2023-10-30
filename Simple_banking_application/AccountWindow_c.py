
from Function_c import *


class AccountWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Create Account")
        self.setGeometry(100, 100, 300, 200)

        self.create_account_button = QPushButton("Create account")
        self.create_account_button.clicked.connect(self.create_account_button_clicked)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)

        self.account_name = QLineEdit()
        self.account_surname = QLineEdit()
        self.account_balance = QLineEdit()
        self.account_balance.setValidator(QIntValidator(0, 1000000))
        self.account_balance.setText(str(0))

        self.account_name_label = QLabel('Name')
        self.account_surname_label = QLabel('Surname')
        self.account_balance_label = QLabel('First withdraw')


        account_layout = QVBoxLayout()
        account_layout.addWidget(self.account_name_label)
        account_layout.addWidget(self.account_name)
        account_layout.addWidget(self.account_surname_label)
        account_layout.addWidget(self.account_surname)
        account_layout.addWidget(self.account_balance_label)
        account_layout.addWidget(self.account_balance)
        account_layout.addWidget(self.create_account_button)
        account_layout.addWidget(self.cancel_button)

        button_layout = QHBoxLayout()
        button_layout.addLayout(account_layout)

        main_layout = QVBoxLayout()
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def create_account_button_clicked(self):
        name = self.account_name.text()
        surname = self.account_surname.text()
        balance = float(self.account_balance.text())
        Function.create_account(name, surname, balance)
        self.accept()

