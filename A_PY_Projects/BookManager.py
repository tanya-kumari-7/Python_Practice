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