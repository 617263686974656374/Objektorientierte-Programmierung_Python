class Bank_Account:
    def __init__(self, Name, Balance, ID):
        self.Name = Name
        self.Balance = int(Balance)
        self.ID = ID

    def deposit(self):
        try:
            amount = float(input("Wie viel möchten Sie einzahlen? "))
            self.Balance += amount
            print(f"Eingezahlt: {amount}€")
        except:
            print("Bitte eine Zahl eingeben!")

    def withdraw(self):
        try:
            amount = float(input("Wie viel möchten Sie abheben? "))
            if self.Balance >= amount:
                self.Balance -= amount
                print(f"Abgehoben: {amount}€")
            else:
                print("Kontostand zu gering.")
        except:
            print("Bitte eine Zahl eingeben!")

    def display(self):
        print(f"Kontostand von {self.Name}: {self.Balance}€")
