def edit_or_delete(mp, file_name):
    while True:
        try:
            mp.display_numerated()
            choice_02 = int(input("Which entry do you want to edit or delete?\n[0] to exit.\n"))
            if choice_02 == 0:
                break
            edit_entry = mp.list_of_people[choice_02 - 1]
            mp.display_specific(edit_entry)
            choice_03 = input("What attribute do you want to edit?\n[exit] to exit, [delete] to delete\n")
            if choice_03 == "Name":
                edit_entry.set_name(input("Enter new Name: "))
            elif choice_03 == "Age":
                edit_entry.set_age(input("Enter new Age: "))
            elif choice_03 == "Phone Number":
                edit_entry.set_pnum(input("Enter new Phone Numer: "))
            elif choice_03 == "Email":
                edit_entry.set_email(input("Enter new Email: "))
            elif choice_03 == "Address":
                edit_entry.set_address(input("Enter new Address: "))
            elif choice_03 == "ID":
                edit_entry.set_ID(input("Enter new ID: "))
            elif choice_03 == "delete":
                mp.list_of_people.pop(choice_02 - 1)
            elif choice_03 == "exit":
                break
            mp.save_data(file_name)
        except:
            pass
