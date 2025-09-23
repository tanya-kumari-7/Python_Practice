"""
To-Do List App (Console)
Add, delete, update tasks.
Save tasks in a text file or JSON.
Learn basics of lists, loops, and file handling.
"""
# Imports 
from datetime import datetime

#  Create a text file and add tasks 

def add_task(task_id,task_name,status,date):
    if not (task_id and task_name and status and date):
        return "Enter complete task details :task_id,task_name,status,date(format: yyyy-mm-dd)"
    else:
        with open("text_book.txt","a") as file:
            file.write(f"{task_id} | {task_name} |{status} | {date}\n")
            return "Task Added !! :)"
        
add_task("1", "Update Trade Details", "Pending", "2025-01-01")
add_task("2", "Check Payment Records", "In Progress", "2025-01-03")
add_task("3", "Review Client Feedback", "Completed", "2025-01-05")
add_task("4", "Prepare Monthly Report", "Pending", "2025-01-07")
add_task("5", "Fix Dashboard Bugs", "In Progress", "2025-01-10")
add_task("6", "Conduct Team Meeting", "Pending", "2025-01-12")
add_task("7", "Update API Documentation", "Completed", "2025-01-15")
add_task("8", "Test New Features", "Pending", "2025-01-18")
add_task("9", "Analyze Market Data", "In Progress", "2025-01-20")
add_task("10", "Optimize SQL Queries", "Pending", "2025-01-22")
add_task("11", "Clean User Database", "Completed", "2025-01-25")
add_task("12", "Design New Dashboard", "Pending", "2025-01-27")
add_task("13", "Review Security Logs", "Pending", "2025-01-28")
add_task("14", "Check Backup Files", "Completed", "2025-01-29")
add_task("15", "Send Invoice Reminders", "In Progress", "2025-02-01")
add_task("16", "Verify Tax Filings", "Pending", "2025-02-03")
add_task("17", "Train New Employees", "Completed", "2025-02-05")
add_task("18", "Prepare Presentation", "Pending", "2025-02-07")
add_task("19", "Update User Permissions", "In Progress", "2025-02-10")
add_task("20", "Plan Product Launch", "Pending", "2025-02-12")


def delete_task_by_id(task_id):
    input_task_id = str(task_id)

    # Step 1: Read all tasks
    with open("text_book.txt", "r") as file:
        task_details = file.readlines()
        for line in task_details:
            task_id,task_name,status,date = line.strip().split("|")
            if task_id == input_task_id:
                print(line)
            else:
                continue

delete_task_by_id(20)