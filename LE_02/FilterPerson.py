from ClassManage import *
from ClassPerson import *


def filter_person_in_list(mp):
    mp.list_of_filtered_people = []
    list_of_dict = []
    for item in mp.list_of_people:
        list_of_dict.append(item.to_dict())
    search_operator = input("Enter search operator: ")
    list_of_dict = list(filter_dict(list_of_dict, search_operator))
    if len(list_of_dict) >= 1:
        for item in list_of_dict:
            if "eid" in item:
                name = item.get("name")
                age = item.get("age")
                pnum = item.get("pnum")
                email = item.get("email")
                address = item.get("address")
                eid = item.get("eid")
                mp.add_filtered_people(Employee(name, age, pnum, email, address, eid))
            elif 'cid' in item:
                name = item.get("name")
                age = item.get("age")
                pnum = item.get("pnum")
                email = item.get("email")
                address = item.get("address")
                cid = item.get("cid")
                mp.add_filtered_people(Customer(name, age, pnum, email, address, cid))
            else:
                pass
        mp.display_filtered()
        filter_check = input("Do you want to save the filtered list? (y/n) ")
        if filter_check == "y":
            mp.save_filtered_data(input("Enter file name for filtered list: "))
        else:
            pass
    else:
        print("\nNo matches found.\n")
