import pandas as pd
import os

def create_account():
    lstname = []
    lstbalance = []
    lstID = []

    try:
        with open(f"Accounts.csv", "r") as f:
            for count, line in enumerate(f):
                pass
        f.close()
        count += 1
    except:
        count = 1
    i = 101
    lstname.append(input("Geben Sie den Namen des Kontoinhabers oder abbrechen ein: "))
    if lstname[0] != "abbrechen":
        dfdaten = pd.read_csv("Accounts.csv")
        while (f"ID{i}" in dfdaten["ID"].values) is True:
            i += 1
        lstbalance.append(0)
        lstID.append(f"ID{i}")

        accountframe = {
            "Name": lstname,
            "Balance": lstbalance,
            "ID": lstID
        }
        datenliste = pd.DataFrame(accountframe)
        if not os.path.exists("Accounts.csv"):
            datenliste.to_csv(f"Accounts.csv", mode="a+", index=False)
        else:
            datenliste.to_csv(f"Accounts.csv", mode="a+", index=False, header=False)
        print(f"Ihre ID Nummer ist {i}.\n"
              f"Merken Sie sich diese um wieder auf Ihr Konto zuzugreifen.")
    else:
        print("Vorgang abgebrochen.")
