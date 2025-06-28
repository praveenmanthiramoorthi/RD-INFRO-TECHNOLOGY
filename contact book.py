contacts = []
def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")
    contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
    print("Contact added.\n")

def view_contacts():
    if not contacts:
        print("No contacts.\n")
        return
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} - {c['phone']}")
    print()

def search_contact():
    query = input("Search name/phone: ")
    for c in contacts:
        if query.lower() in c['name'].lower() or query in c['phone']:
            print(f"\nName: {c['name']}\nPhone: {c['phone']}\nEmail: {c['email']}\nAddress: {c['address']}\n")
            return
    print("Not found.\n")

def update_contact():
    query = input("Enter name to update: ")
    for c in contacts:
        if c['name'].lower() == query.lower():
            c['name'] = input("New name: ") or c['name']
            c['phone'] = input("New phone: ") or c['phone']
            c['email'] = input("New email: ") or c['email']
            c['address'] = input("New address: ") or c['address']
            print("Contact updated.\n")
            return
    print("Contact not found.\n")

def delete_contact():
    query = input("Enter name to delete: ")
    for c in contacts:
        if c['name'].lower() == query.lower():
            contacts.remove(c)
            print("Contact deleted.\n")
            return
    print("Contact not found.\n")

while True:
    print("1. Add\n2. View\n3. Search\n4. Update\n5. Delete\n0. Exit")
    ch = input("Choice: ")
    if ch == '1':
        add_contact()
    elif ch == '2':
        view_contacts()
    elif ch == '3':
        search_contact()
    elif ch == '4':
        update_contact()
    elif ch == '5':
        delete_contact()
    elif ch == '0':
        break
    else:
        print("Invalid choice.\n")
