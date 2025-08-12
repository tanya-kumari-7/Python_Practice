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
    with open("mood_book.txt", 'a') as file:


#add_header()


