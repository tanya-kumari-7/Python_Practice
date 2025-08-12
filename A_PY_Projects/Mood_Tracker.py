'''
1️ Daily Mood Tracker
What it does: You record your mood every day (e.g., happy, stressed, tired), and at the end of the week/month, it shows a summary of your moods.

What you’ll learn:

Storing and retrieving data from a file or database

Working with dates

Creating simple summaries and statistics

'''

# import datetime
def add_header():
    with open("mood_book.txt", 'a') as file:
        file.write("Date | Mood_Status\n")

def add_mood_status(date,Mood_Status):
    if not date or not Mood_Status:
        print("Please add date and how's your mode today")
        return
    else:
        date = date.strip()
        Mood_Status = Mood_Status.strip()
        with open("mood_book.txt", 'a') as file:
            file.write(f"{date} | {Mood_Status}\n")
            print(" Your Status is Successfully Added !!! ")
            return
        
def add_dumy_data():
    data = [
        ("2025-08-01", "happy"),
        ("2025-08-02", "sad"),
        ("2025-08-03", "excited"),
        ("2025-08-04", "tired"),
        ("2025-08-05", "relaxed"),
        ("2025-08-06", "angry"),
        ("2025-08-07", "motivated"),
        ("2025-08-08", "lazy"),
        ("2025-08-09", "stressed"),
        ("2025-08-10", "joyful"),
        ("2025-08-11", "nervous"),
        ("2025-08-12", "content"),
        ("2025-08-13", "bored"),
        ("2025-08-14", "hopeful"),
        ("2025-08-15", "grateful"),
        ("2025-08-16", "frustrated"),
        ("2025-08-17", "proud"),
        ("2025-08-18", "worried"),
        ("2025-08-19", "cheerful"),
        ("2025-08-20", "energetic"),
        ("2025-08-21", "lonely"),
        ("2025-08-22", "optimistic"),
        ("2025-08-23", "calm"),
        ("2025-08-24", "curious"),
        ("2025-08-25", "sad"),
        ("2025-08-26", "happy"),
        ("2025-08-27", "peaceful"),
        ("2025-08-28", "annoyed"),
        ("2025-08-29", "excited"),
        ("2025-08-30", "tired")
    ]

    for date, mood in data:
        add_mood_status(date, mood)

def check():

          


#add_header()
# add_dumy_data()
# add_mood_status("2025-08-01","")


