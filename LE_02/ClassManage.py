import pickle
from tabulate import tabulate
from ClassPerson import *


class ManagePerson:
    def __init__(self):
        self.list_of_people = []
        self.list_of_filtered_people = []

    def add_people(self, people):
        self.list_of_people.append(people)

    def add_filtered_people(self, people):
        self.list_of_filtered_people.append(people)

    def filter(self, filter_operator):
        return [people for people in self.list_of_people if filter_operator(people)]

    def load_data(self, file_name):
        with open(file_name, "rb") as f:
            self.list_of_people = pickle.load(f)

    def save_data(self, file_name):
        with open(file_name, "wb") as f:
            pickle.dump(self.list_of_people, f)

    def save_filtered_data(self, file_name):
        with open(file_name, "wb") as f:
            pickle.dump(self.list_of_filtered_people, f)

    def display(self):
        headers = ["Name", "Age", "Phone Number", "Email", "Address", "ID"]
        rows = []
        for people in self.list_of_people:
            if isinstance(people, Customer):
                rows.append(("Customer", people.get_name(), people.get_age(), people.get_pnum(),
                             people.get_email(), people.get_address(), f"CID {people.get_cid()}"))
            elif isinstance(people, Employee):
                rows.append(("Employee", people.get_name(), people.get_age(), people.get_pnum(),
                             people.get_email(), people.get_address(), f"EID {people.get_eid()}"))
            else:
                print("Fehler")
        print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))

    def display_filtered(self):
        headers = ["Name", "Age", "Phone Number", "Email", "Address", "ID"]
        rows = []
        for people in self.list_of_filtered_people:
            if isinstance(people, Customer):
                rows.append(("Customer", people.get_name(), people.get_age(), people.get_pnum(),
                             people.get_email(), people.get_address(), f"CID {people.get_cid()}"))
            elif isinstance(people, Employee):
                rows.append(("Employee", people.get_name(), people.get_age(), people.get_pnum(),
                             people.get_email(), people.get_address(), f"EID {people.get_eid()}"))
            else:
                print("Fehler")
        print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))

    def display_numerated(self):
        headers = ["Name", "Age", "Phone Number", "Email", "Address", "ID"]
        rows = []
        i = 0
        for people in self.list_of_people:
            i += 1
            if isinstance(people, Customer):
                rows.append((i, "Customer", people.get_name(), people.get_age(), people.get_pnum(),
                             people.get_email(), people.get_address(), f"CID {people.get_cid()}"))
                # Nice
            elif isinstance(people, Employee):
                rows.append((i, "Employee", people.get_name(), people.get_age(), people.get_pnum(),
                             people.get_email(), people.get_address(), f"EID {people.get_eid()}"))
            else:
                print("Fehler")
        print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))

    def display_specific(self, edit_entry):
        headers = ["Name", "Age", "Phone Number", "Email", "Address", "ID"]
        rows = []
        if isinstance(edit_entry, Customer):
            rows.append(("Customer", edit_entry.get_name(), edit_entry.get_age(), edit_entry.get_pnum(),
                         edit_entry.get_email(), edit_entry.get_address(), f"CID {edit_entry.get_cid()}"))
        elif isinstance(edit_entry, Employee):
            rows.append(("Employee", edit_entry.get_name(), edit_entry.get_age(), edit_entry.get_pnum(),
                         edit_entry.get_email(), edit_entry.get_address(), f"EID {edit_entry.get_eid()}"))
        else:
            print("Fehler")
        print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))


def filter_dict(list_of_dict, search_operator):
    def iterator_func(x):
        for items in x.values():
            if search_operator in items:
                return True
        return False
    return filter(iterator_func, list_of_dict)
