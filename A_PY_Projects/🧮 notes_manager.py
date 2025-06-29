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

