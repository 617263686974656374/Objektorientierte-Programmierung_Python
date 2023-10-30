from Function_c import *
from AccountWindow_c import *
from DeleteWindow_c import *
from WithdrawWindow_c import *
from DepositWindow_c import *
from  DisplayWindow_c import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        Function.accounts = Function.load_accounts_from_file()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Bank SZF")
        layout = QVBoxLayout()

        btn = QPushButton("Create account")
        btn.clicked.connect(self.create_account_button_clicked)
        layout.addWidget(btn)

        btn = QPushButton("Delete account")
        btn.clicked.connect(self.delete_account_button_clicked)
        layout.addWidget(btn)

        btn = QPushButton("Withdrawal of money")
        btn.clicked.connect(self.withdrawal_button_clicked)
        layout.addWidget(btn)

        btn = QPushButton("Deposit money")
        btn.clicked.connect(self.deposit_button_clicked)
        layout.addWidget(btn)

        btn = QPushButton("Display individual account")
        btn.clicked.connect(self.display_one_account_button_clicked)
        layout.addWidget(btn)

        btn = QPushButton("Display all accounts")
        btn.clicked.connect(self.display_all_account_button_clicked)
        layout.addWidget(btn)

        self.output = QPlainTextEdit()
        layout.addWidget(self.output)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def create_account_button_clicked(self):
        self.output.clear()
        dialog = AccountWindow()
        result = dialog.exec()
        if result == QDialog.accepted:
            Function.save_accounts_to_file(Function.accounts) # Add this line to save the updated accounts
            self.output.appendPlainText(f'Account created !')

    def delete_account_button_clicked(self):
        self.output.clear()
        dialog = DeleteWindow()
        dialog.exec()
        Function.save_accounts_to_file(Function.accounts) # Add this line to save the updated accounts
        self.output.appendPlainText(f'Account deleted !')

    def withdrawal_button_clicked(self):
        self.output.clear()
        dialog = WithdrawWindow()
        dialog.exec()


    def deposit_button_clicked(self):
        self.output.clear()
        dialog = DepositWindow()
        dialog.exec()

    def display_one_account_button_clicked(self):
        self.output.clear()
        dialog = DisplayWindow()
        dialog.exec()


    def display_all_account_button_clicked(self):
        self.output.clear()
        Function.show_account_info(self, name=None, surname=None)
        self.output.appendPlainText('All accounts displayed!')

