def create_notes(notes, added_on, due_date):
    if not notes.strip() or not added_on.strip() or not due_date.strip():
        return "❌ Notes content, added_on, or due_date can't be blank"

    with open("notesbook.txt", "a") as file:
        file.write(f"{notes} | {added_on} | {due_date}\n")
    return "✅ Notes added!"

def read_notes():
    try:
        with open("notesbook.txt", "r") as file:
            notes_details = file.readlines()
            if not notes_details:
                print("📭 No notes found.")
            else:
                print("📇 Your Notes List:")
                for i, line in enumerate(notes_details, start=1):
                    notes, added_on, due_date = line.strip().split("|")
                    print(f"{i}. Notes: {notes.strip()}, Added On: {added_on.strip()}, Due Date: {due_date.strip()}")
    except FileNotFoundError:
        print("⚠️ File not found. Add a note first.")

def search_notes(keyword):
    try:
        with open("notesbook.txt", "r") as file:
            notes_details = file.readlines()

        found = False
        for i, line in enumerate(notes_details, start=1):
            if keyword.lower() in line.lower():
                notes, added_on, due_date = line.strip().split("|")
                print(f"{i}. Notes: {notes.strip()}, Added On: {added_on.strip()}, Due Date: {due_date.strip()}")
                found = True

        if not found:
            print("🔍 No notes found with that keyword.")

    except FileNotFoundError:
        print("⚠️ File not found.")

def delete_notes(title):
    try:
        with open("notesbook.txt", "r") as file:
            notes_details = file.readlines()

        found = False
        for i, line in enumerate(notes_details):
            if title.lower() in line.lower():
                deleted = notes_details.pop(i)
                found = True
                break

        if found:
            with open("notesbook.txt", "w") as file:
                file.writelines(notes_details)
            print(f"🗑️ Note deleted: {deleted.strip()}")
        else:
            print("❌ Note not found.")

    except FileNotFoundError:
        print("⚠️ File not found.")

# ✅ Main menu loop
while True:
    print("\n📇 Notes Manager")
    print("1. Add Note")
    print("2. View All Notes")
    print("3. Search Notes")
    print("4. Delete Note by Title")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        notes = input("Enter note content: ")
        added_on = input("Enter added_on date (e.g. 2024-06-27): ")
        due_date = input("Enter due_date (optional or deadline): ")
        print(create_notes(notes, added_on, due_date))

    elif choice == "2":
        read_notes()

    elif choice == "3":
        keyword = input("Enter keyword to search: ")
        search_notes(keyword)

    elif choice == "4":
        title = input("Enter any part of note content to delete: ")
        delete_notes(title)

    elif choice == "5":
        print("👋 Exiting Notes Manager.")
        break

    else:
        print("❌ Invalid choice.")