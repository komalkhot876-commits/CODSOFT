contacts = []


def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)

    print("CONTACT ADDED SUCCESSFULLY")


def view_contacts():

    if len(contacts) == 0:
        print("NO CONTACTS FOUND")

    else:
        print("\nCONTACT LIST")

        for index, contact in enumerate(contacts, 1):
            print(f"{index}. {contact['name']} | {contact['phone']} | {contact['email']}")


def search_contact():

    search_name = input("Enter name to search: ")

    found = False

    for contact in contacts:

        if contact['name'].lower() == search_name.lower():

            print("\nCONTACT FOUND")
            print(f"Name : {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")

            found = True

    if found == False:
        print("CONTACT NOT FOUND")


def delete_contact():

    view_contacts()

    if len(contacts) == 0:
        return

    contact_num = int(input("Enter contact number to delete: "))

    if 1 <= contact_num <= len(contacts):

        removed_contact = contacts.pop(contact_num - 1)

        print(f"{removed_contact['name']} DELETED SUCCESSFULLY")

    else:
        print("INVALID CONTACT NUMBER")


def menu():

    while True:

        print("\n----- CONTACT BOOK -----")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            delete_contact()

        elif choice == "5":
            print("EXITING CONTACT BOOK")
            break

        else:
            print("INVALID CHOICE")


menu()
