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
