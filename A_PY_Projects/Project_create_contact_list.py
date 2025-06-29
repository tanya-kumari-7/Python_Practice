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
                print("📝 Your Contacts:")
                for i, contact in enumerate(contacts, start=1):
                    print(f"{i}. {contact.strip()}")
    except FileNotFoundError:
        print("⚠️ Contact list file not found. Add a contact first.")


