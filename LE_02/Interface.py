from ClassManage import *
import os
from AddPerson import add_customer, add_employee
from FilterPerson import filter_person_in_list
from EditAndDelete import edit_or_delete


def run_interface():
    while True:
        file_name = input("Enter file name: ")
        mp = ManagePerson()
        if os.path.exists(file_name):
            mp.load_data(file_name)
            break
        else:
            choice_04 = input("This file does not exist.\nDo you want to create a new file? (y/n) ")
            if choice_04 == "y":
                break
            else:
                pass
    while True:
        try:
            choice_01 = int(input("Menu:\n"
                                  "-------\n"
                                  "1. Enter new Customer.\n"
                                  "2. Enter new Employee.\n"
                                  "3. Filter people.\n"
                                  "4. Edit or delete entry.\n"
                                  "5. Display.\n"
                                  "6. Save and Exit.\n"))
            if choice_01 == 1:
                add_customer(mp)
                mp.save_data(file_name)
            elif choice_01 == 2:
                add_employee(mp)
                mp.save_data(file_name)
            elif choice_01 == 3:
                filter_person_in_list(mp)
            elif choice_01 == 4:
                edit_or_delete(mp, file_name)
            elif choice_01 == 5:
                mp.display()
            elif choice_01 == 6:
                mp.save_data(file_name)
                break
        except:
            print("Please choose a valid option.")
            pass
