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




