def create_contact_list(name, email, phone):
    if not name.strip():
        return "❌ Contact name cannot be empty."
    if not email.strip():
        return "❌ email cannot be empty."
    if not phone.strip():
        return "❌ phone cannot be empty."

    with open("contact_list.txt", "a") as file:
        file.write(f"{name} | {email} | {phone}\n")
    return "✅ Contact added!"
def read_contacts():
    try:
        with open("contact_list.txt", "r") as file:
            contacts = file.readlines()
            if not contacts:
                print("📭 No contacts found.")
            else:
                print("📇 Your Contact List:")
                for i, line in enumerate(contacts, start=1):
                    name, email, phone = line.strip().split("|")
                    print(f"{i}. Name: {name.strip()}, Email: {email.strip()}, Phone: {phone.strip()}")
    except FileNotFoundError:
        print("⚠️ File not found. Add a contact first.")


def search_contact(keyword):
    try:
        with open("contact_list.txt", "r") as file:
            contacts = file.readlines()

        found = False
        for i, line in enumerate(contacts, start=1):
            if keyword.lower() in line.lower():
                name, email, phone = line.strip().split("|")
                print(f"{i}. Name: {name.strip()}, Email: {email.strip()}, Phone: {phone.strip()}")
                found = True

        if not found:
            print("🔍 No contact found with that keyword.")

    except FileNotFoundError:
        print("⚠️ File not found.")

def delete_contact_by_phone(phone):
    try:
        with open("contact_list.txt", "r") as file:
            contacts = file.readlines()

        contact_found = False
        for i, line in enumerate(contacts):
            if phone in line:
                deleted = contacts.pop(i)
                contact_found = True
                break

        if contact_found:
            with open("contact_list.txt", "w") as file:
                file.writelines(contacts)
            print(f"🗑️ Contact deleted: {deleted.strip()}")
        else:
            print("❌ Contact not found.")

    except FileNotFoundError:
        print("⚠️ File not found.")


# ✅ Main menu loop
while True:
    print("\n📇 Contact Book")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone: ")
        print(create_contact_list(name, email, phone))

    elif choice == "2":
        read_contacts()

    elif choice == "3":
        keyword = input("Enter name or phone to search: ")
        search_contact(keyword)

    elif choice == "4":
        phone = input("Enter phone number to delete: ")
        delete_contact_by_phone(phone)

    elif choice == "5":
        print("👋 Exiting Contact Book.")
        break

    else:
        print("❌ Invalid choice.")


