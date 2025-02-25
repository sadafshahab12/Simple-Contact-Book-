contact = {}

while True:
    print("Contact Book Menu")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Choose an option 1 - 5: ")

    if choice == "1":
        name = input("Enter contact name")
        phone = input("Enter Phone number")
        contact[name] = phone
        print(f"contact {name} added!")
    elif choice == "2":
        if contact:
            print("Contact List")
            for name , phone in contact.items():
                print(f"{name} {phone}")
        else:
            print("No Contact Found")
    elif choice == "3":
        name  = input("Enter Contact name to update:")
        if name in contact:
            new_phone = input("Enter New Number")
            contact[name]= new_phone
        else:
            print("No contact found")
    elif choice == "4":
        name = input("Enter contact name to delete:")
        if name in contact:
            del contact[name]
            print(f"contact {name} deleted!")
        else:
            print("Contact not found")
    elif choice == "5":
        print("Good bye!")
        break
    else:
        print("Invalid option : please enter a number between 1 - 5")