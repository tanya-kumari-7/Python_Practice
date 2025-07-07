def create_to_do(Notes,status,notes_due_date,notes_added_on):
    if not Notes.strip():
        return 'Notes Cant be Blank'
    if not status.strip():
        return 'status Cant be Blank'
    if not notes_due_date.strip():
        return 'notes_due_date Cant be Blank'
    if not notes_added_on.strip():
        return 'notes_added_on Cant be Blank'
    
    with open("to_do_book.txt","a") as file:
        file.write(f'{Notes} | {status} | {notes_due_date} | {notes_added_on} \n')
        return "Notes Added"
    
## print(create_to_do("Call maa", "Pending", "2025-08-08", "2025-07-07"))

