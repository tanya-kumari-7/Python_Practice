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
          

# add_mood_status("2025-08-01","")
#add_header()


