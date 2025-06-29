def create_notes(notes, added_on, due_date):
    if not notes.strip() or not added_on.strip() or not due_date.strip():
        return "❌ Notes content, added_on, or due_date can't be blank"

    with open("notesbook.txt", "a") as file:
        file.write(f"{notes} | {added_on} | {due_date}\n")
    return "✅ Notes added!"



