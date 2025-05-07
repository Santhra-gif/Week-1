import json
filename = 'contacts.json'

# To load contacts
def load_contacts():
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# To save contacts
def save_contacts(contacts):
    with open(filename, 'w') as f:
        json.dump(contacts, f)

# To view all contacts
def view_contacts(contacts):
    if not contacts:
        print("Contact book is empty.")
    else:
        print("\nContacts:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    print()

# Add a new contact
def add_contact(contacts):
    name = input("Enter name: ").strip()
    if name in contacts:
        print("This contact already exists. Updating phone number.")
    phone = input("Enter phone number: ").strip()
    contacts[name] = phone
    print("Contact added/updated.\n")

def main():
    contacts = load_contacts()
    
    while True:
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Save and Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            view_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            save_contacts(contacts)
            print("Contacts saved")
            break
        else:
            print("Invalid option. Try again.\n")

if __name__ == "__main__":
    main()
