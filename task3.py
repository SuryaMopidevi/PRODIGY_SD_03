import json
import os

# File path for storing contacts
CONTACTS_FILE = "contacts.json"

def load_contacts():
    """
    Load contacts from the JSON file.
    If the file does not exist, return an empty dictionary.
    """
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                print("Error: The contacts file is corrupted. Starting fresh.")
                return {}
    return {}

def save_contacts(contacts):
    """
    Save contacts to the JSON file.
    Overwrites the file with the current state of the contacts dictionary.
    """
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)
    print("Contacts saved successfully to file.")

def add_contact(contacts):
    """
    Add a new contact to the contacts dictionary.
    """
    name = input("Enter name: ").strip()
    if name in contacts:
        print(f"Contact '{name}' already exists.")
        return
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!")

def view_contacts(contacts):
    """
    Display all contacts in the contacts dictionary.
    """
    if not contacts:
        print("No contacts available.")
        return
    print("\nContacts:")
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

def edit_contact(contacts):
    """
    Edit an existing contact in the contacts dictionary.
    """
    name = input("Enter the name of the contact to edit: ").strip()
    if name not in contacts:
        print(f"Contact '{name}' does not exist.")
        return
    print("Leave a field blank if you don't want to change it.")
    phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ").strip()
    email = input(f"Enter new email address (current: {contacts[name]['email']}): ").strip()
    if phone:
        contacts[name]["phone"] = phone
    if email:
        contacts[name]["email"] = email
    save_contacts(contacts)
    print(f"Contact '{name}' updated successfully!")

def delete_contact(contacts):
    """
    Delete a contact from the contacts dictionary.
    """
    name = input("Enter the name of the contact to delete: ").strip()
    if name not in contacts:
        print(f"Contact '{name}' does not exist.")
        return
    del contacts[name]
    save_contacts(contacts)
    print(f"Contact '{name}' deleted successfully!")

def main():
    """
    Main program loop for the contact management system.
    """
    contacts = load_contacts()

    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)  # Final save before exiting
            print("Have a good day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
