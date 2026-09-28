import json

FILE_NAME = "contacts.json"


def load_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts(contacts)

    print("Contact added successfully.")


def search_contact(contacts):
    name = input("Enter the name to search: ")

    found = False

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("\nContact found:")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            found = True

    if not found:
        print("Contact not found.")


def display_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return

    print("\nContacts:")

    for contact in contacts:
        print("--------------------")
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])


def main():
    contacts = load_contacts()

    while True:
        print("\n=== CONTACT BOOK ===")
        print("1. Add contact")
        print("2. Search contact")
        print("3. Display contacts")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            search_contact(contacts)

        elif choice == "3":
            display_contacts(contacts)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
