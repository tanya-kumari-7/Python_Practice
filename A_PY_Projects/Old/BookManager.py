def add_book_func(title,author,status):
        if not title.strip() or not author.strip() or not status.strip():
            return "title,author,status can't be blank,Please add details to proceed further"
        else:
            with open('booktracker.txt','a') as file:
                file.write(f'{title} | {author} |{status}\n')
        return "Book details added to BookTracker"


def readbook():
    try:
        with open("booktracker.txt", "r") as file:
            book_details = file.readlines()
            if not book_details:
                print("📭 No brook detail found.")
            else:
                for i,lines in enumerate(book_details,start=1):
                    title,author,status =  lines.strip().split("|")
                    print(f"{i}.title: {title.strip()} , author{author.strip()}, status: {status.strip()}")
                    
    except FileNotFoundError:
        print("⚠️ File not found. Add a note first.") 

def searchbytitle(title):
    try:
        with open('booktracker.txt','r') as file:
            book_details = file.readlines()
            
            found = False
            for i,line in enumerate(book_details,start=1):
                if title.lower() in line.lower():
                    title,author,status =  line.strip().split("|")
                    print(f"{i}.title: {title.strip()} , author{author.strip()}, status: {status.strip()}")
                found = True
            if not found:
                print("🔍 No notes found with that keyword.")

    except FileNotFoundError:
        print("⚠️ File not found.")


def delete_by_title(title):
    try:
        with open("booktracker.txt", "r") as file:
            book_details = file.readlines()

        found = False
        for i, line in enumerate(book_details):
            if title.lower() in line.lower():
                deleted = book_details.pop(i)
                found = True
                break

        if found:
            with open("booktracker.txt", "w") as file:
                file.writelines(book_details)
            print(f"🗑️ title deleted: {deleted.strip()}")
        else:
            print("❌ title not found.")

    except FileNotFoundError:
        print("⚠️ titel not found.")


# ✅ Main menu loop
while True:
    print("\n📇 book Manager")
    print("1. Add title")
    print("2. View All title")
    print("3. Search titlr")
    print("4. Delete book title by Title")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        title = input("Enter note content: ")
        author = input("Enter added_on date (e.g. 2024-06-27): ")
        status = input("Enter due_date (optional or deadline): ")
        print(add_book_func(title, author, status))

    elif choice == "2":
        readbook()

    elif choice == "3":
        keyword = input("Enter keyword to search: ")
        searchbytitle(keyword)

    elif choice == "4":
        title = input("Enter any part of note content to delete: ")
        delete_by_title(title)

    elif choice == "5":
        print("👋 Exiting Notes Manager.")
        break

    else:
        print("❌ Invalid choice.")

        