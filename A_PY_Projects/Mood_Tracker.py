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
    with open("mood_book.text", 'a') as file:
        file.writelines(["Date,Mood_Status\n"])

add_header()




# def mood_tracker(date,Mood_status):
