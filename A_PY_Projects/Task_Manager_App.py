import os
import datetime

def show_menu():
    print("Welcome to Task Manager App")
    print("Hope You're Doing Great!") 
    print("Here is your Menu")
    print(" 1. Add Task")
    print(" 2. View Tasks")
    print(" 3. Mark Task as Done")
    print(" 4. Update Task")
    print(" 5. Delete Task")
    print(" 6. Exit")

def initialize_file_with_header():
    header = "Date | Task | due_date | task_status | task_completed_on\n"
    if not os.path.exists("task_book.txt") or os.stat("task_book.txt").st_size == 0:
        with open("task_book.txt", 'w') as file:
            file.write(header)

# Initialize header if needed
# initialize_file_with_header()

def Add_task_func(Date, Task, due_date, task_status, task_completed_on):
    print("Please Note: Date should be in dd-mm-yyyy format")
    print("If task_completed_on is not applicable, mention 'Null'")
    if not Date or not Task or not due_date or not task_status or not task_completed_on:
        print("Please Enter Complete Details: Date, Task, due_date, task_status, task_completed_on")
    else:
        with open("task_book.txt", 'a') as file:
            file.write(f"{Date} | {Task} | {due_date} | {task_status} | {task_completed_on}\n")
            print(f"Task Added: {Date} | {Task} | {due_date} | {task_status} | {task_completed_on}")



# Example task addition
Add_task_func("14-03-2025", "Home Work to do", "14-03-2025", "Pending", "Null")

# Read File Data
# with open("task_book.txt", "r") as file:
#     content = file.read()
#     print(content)

# To delete file content, uncomment below:
# with open("task_book.txt", "w") as file:
#     pass
