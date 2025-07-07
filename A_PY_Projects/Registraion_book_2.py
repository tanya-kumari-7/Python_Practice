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

    def view_to_do_book():
        try:
            with open("to_do_book.txt","r") as file:
                book_content = file.readlines()
                
                if not book_content:
                    print("No Content Found, Please add your notes to view")
                
                for i , line in enumerate(book_content,start=1):
                    Notes,status,notes_due_date,notes_added_on = line.strip().split("|")
                    print(f"{i}. Notes: {Notes.strip()}, status: {status.strip()}, notes_due_date: {notes_due_date.strip()}, notes_added_on: {notes_added_on.strip()}")
        except Exception as a:
            print("check error",a) 

    print(view_to_do_book())

def update_to_do(index, Notes, status, notes_due_date, notes_added_on):
    try:
        with open("to_do_book.txt", "r") as file:
            lines = file.readlines()
        
        if index < 1 or index > len(lines):
            return "Invalid index"
        
        lines[index-1] = f"{Notes} | {status} | {notes_due_date} | {notes_added_on}\n"
        
        with open("to_do_book.txt", "w") as file:
            file.writelines(lines)
    
        return "Notes Updated Successfully"
    except Exception as e:
        return f"Error: {e}"
    
# Example usage:
print(update_to_do(1, "Call maa", "not need to call", "2025-08-08", "2025-07-07"))


def delete_to_do(index):
    try:
        with open("to_do_book.txt", "r") as file:
            lines = file.readlines()
        
        if index < 1 or index > len(lines):
            return "Invalid index"
        
        del lines[index-1]
        
        with open("to_do_book.txt", "w") as file:
            file.writelines(lines)
    
        return "Notes Deleted Successfully"
    except Exception as e:
        return f"Error: {e}"
    
# Example usage:
print(delete_to_do(3))


def search_to_do(search_term):
    try:
        with open("to_do_book.txt", "r") as file:
            lines = file.readlines()
        
        results = []
        for i, line in enumerate(lines, start=1):
            if search_term.lower() in line.lower():
                results.append(f"{i}. {line.strip()}")
        
        if not results:
            return "No matching notes found"
        
        return "\n".join(results)
    except Exception as e:
        return f"Error: {e}"

# Example usage:
print(search_to_do("Call maa"))  # Replace "Call maa" with your search term


def delete_duplicate_notes():
    try:
        with open("to_do_book.txt", "r") as file:
            lines = file.readlines()
        
        unique_lines = list(set(lines))
        
        with open("to_do_book.txt", "w") as file:
            file.writelines(unique_lines)
        
        return "Duplicate notes deleted successfully"
    except Exception as e:
        return f"Error: {e}"
    
# Example usage:
print(delete_duplicate_notes())  # Deletes duplicate notes from the to-do book


