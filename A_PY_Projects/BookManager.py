def add_book_func(title,author,status):
        if not title.strip() or not author.strip() or not status.strip():
            return "title,author,status can't be blank,Please add details to proceed further"
        else:
            with open('booktracker.txt','a') as file:
                file.write(f'{title} | {author} |{status}\n')
        return "Book details added to BookTracker"


