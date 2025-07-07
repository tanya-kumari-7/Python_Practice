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

# print(view_to_do_book())

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
#print(update_to_do(1, "Call maa", "not need to call", "2025-08-08", "2025-07-07"))


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
#print(delete_to_do(3))


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
#print(search_to_do("Call maa"))  # Replace "Call maa" with your search term


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
#print(delete_duplicate_notes())  # Deletes duplicate notes from the to-do book



# ✅ Main menu loop
while True:
    print("\n📇 Notes Manager")
    print("1. Create Notes")
    print("2. View Notes")
    print("3. Update Notes")
    print("4. Delete Notes")
    print("5. Search Notes")
    print("6. Delete Duplicate Notes")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")
    if choice == "1":
        Notes = input("Enter Notes: ")
        status = input("Enter status: ")
        notes_due_date = input("Enter notes due date: ")
        notes_added_on = input("Enter notes added on: ")
        print(create_to_do(Notes, status, notes_due_date, notes_added_on))
    
    elif choice == "2":
        view_to_do_book()
    
    elif choice == "3":
        index = int(input("Enter the index of the note to update: "))
        Notes = input("Enter new Notes: ")
        status = input("Enter new status: ")
        notes_due_date = input("Enter new notes due date: ")
        notes_added_on = input("Enter new notes added on: ")
        print(update_to_do(index, Notes, status, notes_due_date, notes_added_on))
    
    elif choice == "4":
        index = int(input("Enter the index of the note to delete: "))
        print(delete_to_do(index))
    
    elif choice == "5":
        search_term = input("Enter search term: ")
        print(search_to_do(search_term))
    
    elif choice == "6":
        print(delete_duplicate_notes())
    
    elif choice == "7":
        print("Exiting Notes Manager. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")  