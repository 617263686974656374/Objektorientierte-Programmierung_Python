
from Function_c import *


class DisplayWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Display Account")
        self.setGeometry(100, 100, 300, 200)

        self.display_account_button = QPushButton("Display account")
        self.display_account_button.clicked.connect(self.display_account_button_clicked)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)

        self.account_name_label = QLabel('Choose account:')
        self.combobox = QComboBox()
        #self.combobox.addItem("Choose account")

        accounts = Function.accounts
        for account in accounts:
            self.combobox.addItem(
                f"{account['name']} {account['surname']}")

        label_combo_layout = QHBoxLayout()
        label_combo_layout.addWidget(self.account_name_label)
        label_combo_layout.addWidget(self.combobox)


        self.output = QPlainTextEdit()

        #text_input_layout = QHBoxLayout()

        account_layout = QVBoxLayout()
        account_layout.addLayout(label_combo_layout)
        account_layout.addWidget(self.output)
        account_layout.addWidget(self.display_account_button)
        account_layout.addWidget(self.cancel_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(account_layout)

        self.setLayout(main_layout)

    def get_selected_account(self):
        selected_index = self.combobox.currentIndex()
        selected_account = Function.accounts[selected_index]
        return selected_account

    def display_account_button_clicked(self):
        selected_account = self.get_selected_account()
        self.output.clear()
        self.output.appendPlainText(
            f"Name: {selected_account['name']}\nSurname: {selected_account['surname']}\nBalance: {selected_account['account'].get_balance()}")
