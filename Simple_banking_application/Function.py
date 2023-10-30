from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QLineEdit,QPlainTextEdit,QLabel,QHBoxLayout,QVBoxLayout, QDialog, QMainWindow, QStackedLayout, QComboBox, QMessageBox
from PyQt6.QtGui import QIntValidator
import json


class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def get_balance(self):
        return self.balance


class Function:
    accounts = []

    @staticmethod
    def load_accounts_from_file():
        try:
            with open('accounts.json', 'r') as f:
                data = json.load(f)
                accounts = []
                for account_data in data['accounts']:
                    name = account_data['name']
                    surname = account_data['surname']
                    account = Account(account_data['account']['balance'])
                    accounts.append({'name': name, 'surname': surname, 'account': account})
        except FileNotFoundError:
            accounts = []
        Function.accounts = accounts
        return accounts

    @staticmethod
    def save_accounts_to_file(accounts):
        data = {'accounts': []}
        for account_info in accounts:
            name = account_info['name']
            surname = account_info['surname']
            account = account_info['account']
            account_data = {
                'name': name,
                'surname': surname,
                'account': {
                    'balance': account.get_balance()
                }
            }
            data['accounts'].append(account_data)

        with open('accounts.json', 'w') as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def create_account(name, surname, balance):
        account = Account(balance)
        account_info = {
            'name': name,
            'surname': surname,
            'account': account
        }
        Function.accounts.append(account_info)
        Function.save_accounts_to_file(Function.accounts)

    @staticmethod
    def delete_account(name, surname):
        for account in Function.accounts:
            if account['name'] == name and account['surname'] == surname:
                Function.accounts.remove(account)
                return True
        return False

    @staticmethod
    def withdraw_money(account, amount):
        if account.get_balance() >= amount:
            account.balance -= amount
            return True
        else:
            return False

    @staticmethod
    def deposit_money(account, amount):
        account.balance += amount
        return True

    @staticmethod
    def show_account_info(main_window, name=None, surname=None):
        if name is None and surname is None:
            for account in Function.accounts:
                account_info = f"Name: {account['name']}\nSurname: {account['surname']}\nBalance: {account['account'].get_balance()}\n\n"
                main_window.output.appendPlainText(account_info)
        else:
            found = False
            for account in Function.accounts:
                if account['name'] == name and account['surname'] == surname:
                    account_info = f"Name: {account['name']}\nSurname: {account['surname']}\nBalance: {account['account'].get_balance()}\n\n"
                    main_window.output.appendPlainText(account_info)
                    found = True
                    break
            if not found:
                main_window.output.appendPlainText(f"No account found for {name} {surname}")



accounts = Function.load_accounts_from_file()

