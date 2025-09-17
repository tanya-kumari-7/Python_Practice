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
        with open("A_task_manager_sheet.txt","a") as file:
            file.write(f"{task_id} | {task_name} |{status} | {date}\n")
            return "Task Added !! :)"
        
add_task("1","Update Trade Deatils","Pending","2025-01-01")




