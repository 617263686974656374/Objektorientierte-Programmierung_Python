from KMS_1_03_LE_01_03_Data import *
from KMS_1_03_LE_01_03_Class import *
import os
import pandas as pd

bool_acccreation = False
while bool_acccreation is False:
    choice_1 = input("Besitzen Sie ein Konto? (y/n/beenden) ")
    if choice_1 == "n":
        create_account()
        dfdaten = pd.read_csv("Accounts.csv")
        dfdaten.sort_values(by=["ID"], ascending=True, inplace=True)
        dfdaten.to_csv(f"Accounts.csv", mode="w", index=False)
    elif choice_1 == "y":
        if os.path.exists("Accounts.csv"):
            dfdaten = pd.read_csv("Accounts.csv")
            bool_choice_2 = False
            while bool_choice_2 is False:
                try:
                    choice_2 = input("Bitte geben Sie ihre ID Nummer oder abbrechen ein: ")
                    if choice_2 == "abbrechen":
                        bool_choice_2 = True
                    else:
                        dffiltered = dfdaten.loc[dfdaten["ID"] == f"ID{int(choice_2)}"]
                        Account = Bank_Account(dffiltered.iloc[0, 0],
                                               dffiltered.iloc[0, 1],
                                               dffiltered.iloc[0, 2])
                        bool_withdrawdeposit = True
                        while bool_withdrawdeposit is True:
                            Account.display()
                            choice_3 = input("Wollen Sie abheben, einzahlen, auflösen oder abbrechen? ")
                            if choice_3 == "abheben":
                                Account.withdraw()
                                dffiltered.iloc[0, 1] = Account.Balance
                            elif choice_3 == "einzahlen":
                                Account.deposit()
                                dffiltered.iloc[0, 1] = Account.Balance
                            elif choice_3 == "abbrechen":
                                bool_withdrawdeposit = False
                                dffiltered.iloc[0, 1] = Account.Balance
                                dfdaten.loc[dfdaten["ID"] == f"ID{int(choice_2)}"] = dffiltered.loc[
                                    dffiltered["ID"] == f"ID{int(choice_2)}"]
                            elif choice_3 == "auflösen":
                                print(f"{dffiltered.iloc[0, 0]}s Konto wurde aufgelöst.")
                                dfdaten.loc[dfdaten["ID"] == f"ID{int(choice_2)}"] = dffiltered
                                dfdaten.drop(dffiltered.index, axis=0, inplace=True)
                                bool_withdrawdeposit = False
                            else:
                                print("Bitte geben Sie abheben, einzahlen, auflösen oder abbrechen ein.")
                            dfdaten.to_csv(f"Accounts.csv", mode="w+", index=False)
                        bool_choice_2 = True
                except:
                    print("Bitte geben Sie die ID Nummer eines existierenden Kontos an.")
        else:
            print("Diese Datei existiert nicht.")
    elif choice_1 == "ADMIN":
        if os.path.exists("Accounts.csv"):
            dfdaten = pd.read_csv("Accounts.csv")
            print(dfdaten)
        else:
            print("ERROR!\n"
                  "If you can read this I had a big whoopsie in my code.\n"
                  "I am sorry but I have ABSOLUTELY NO CLUE WHAT THE FUCK happened.\n"
                  "Just, idk, go outside, live your life, money is a construct.\n"
                  "Dont succumb to capitalism, live freely. #blessed\n"
                  "9/11 was an inside job, jet fuel cant melt steel beams.\n"
                  "Sarah dies in The Last of Us.\n"
                  "The Mario movie was bad.\n"
                  "Old Sonic from the movie trailers will haunt your dreams.\n"
                  "Darth Vader is Luke Skywalkers dad.\n"
                  "Jane Parker dies in The Amazing Spider-Man.\n"
                  "Nobody expects the spanish inquisition.")
    elif choice_1 == "beenden":
        bool_acccreation = True
    else:
        print("Bitte geben Sie y/n/beenden ein.")
