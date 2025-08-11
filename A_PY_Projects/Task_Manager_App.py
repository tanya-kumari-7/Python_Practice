import os
import datetime

def show_menu():
    print("Welcome to Task Manager App")
    print("Hope You're Doing Great!") 
    print("Here is your Menu")
    print(" 1. Add Task")
    print(" 2. View Tasks")
    print(" 3. Update Task")
    print(" 4. Delete Task")
    print(" 5. Exit")

def initialize_file_with_header():
    header = "Date | Task | due_date | task_status | task_completed_on\n"
    if not os.path.exists("task_book.txt") or os.stat("task_book.txt").st_size == 0:
        with open("task_book.txt", 'w') as file:
            file.write(header)

def Add_task_func(Date, Task, due_date, task_status, task_completed_on):
    if not Date or not Task or not due_date or not task_status or not task_completed_on:
        print("Please Enter Complete Details: Date, Task, due_date, task_status, task_completed_on")
    else:
        with open("task_book.txt", 'a') as file:
            file.write(f"{Date} | {Task} | {due_date} | {task_status} | {task_completed_on}\n")
            print(f"Task Added: {Date} | {Task} | {due_date} | {task_status} | {task_completed_on}")

def add_buck_task_func():
        Add_task_func("14-03-2025", "Homework", "14-03-2025", "Pending", "Null")
        Add_task_func("15-03-2025", "Pay electricity bill", "16-03-2025", "Pending", "Null")
        Add_task_func("16-03-2025", "Team meeting", "17-03-2025", "Completed", "17-03-2025")
        Add_task_func("17-03-2025", "Buy groceries", "18-03-2025", "Pending", "Null")
        Add_task_func("18-03-2025", "Call plumber", "19-03-2025", "Completed", "19-03-2025")
        Add_task_func("19-03-2025", "Project submission", "20-03-2025", "Pending", "Null")
        Add_task_func("20-03-2025", "Doctor appointment", "21-03-2025", "Completed", "21-03-2025")
        Add_task_func("21-03-2025", "Gym session", "22-03-2025", "Pending", "Null")
        Add_task_func("22-03-2025", "Read book", "25-03-2025", "Pending", "Null")
        Add_task_func("23-03-2025", "Dentist visit", "24-03-2025", "Completed", "24-03-2025")

def view_task():
    with open("task_book.txt", 'r') as file:
        content = file.read()
        print(content)

def mark_task_done_by_task_func(input_task, status_to_be_updated, task_completed_on_to_be_updated):
    with open("task_book.txt", 'r') as file:
        file_detail = file.readlines()

    updated_lines = []
    task_found = False

    for content in file_detail:
        try:
            Date, Task, due_date, task_status, task_completed_on = content.strip().split("|")
            if input_task.strip() == Task.strip():
                task_status = status_to_be_updated.strip()
                task_completed_on = task_completed_on_to_be_updated.strip()
                task_found = True
            updated_line = "|".join([
                Date.strip(), Task.strip(), due_date.strip(),
                task_status.strip(), task_completed_on.strip()
            ])
            updated_lines.append(updated_line + "\n")
        except ValueError:
            updated_lines.append(content)  # Keep malformed lines as-is

    with open("task_book.txt", 'w') as file:
        file.writelines(updated_lines)

    if task_found:
        print(f"Task '{input_task}' updated successfully.")
    else:
        print(f"Task '{input_task}' not found.")

def delete_task_By_Task_name_func(input_task_name):
    with open("task_book.txt", 'r') as file:
        file_content = file.readlines()

    updated_task = []
    task_found = False

    for content in file_content:
        try:
            Date, Task, due_date, task_status, task_completed_on = content.strip().split("|")
            if input_task_name.strip() != Task.strip():
                updated_task.append(content)
            else:
                task_found = True
        except ValueError:
            updated_task.append(content)

    with open("task_book.txt", 'w') as file:
        file.writelines(updated_task)

    if task_found:
        print(f"Task '{input_task_name}' deleted successfully.")
    else:
        print(f"Task '{input_task_name}' not found.")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        Date = input("Enter Date: ")
        Task = input("Enter Task: ")
        due_date = input("Enter Due_date: ")
        task_status = input("Enter task_status: ")
        task_completed_on = input("Enter task_completed_on (if any): ")
        print(Add_task_func(Date, Task, due_date, task_status, task_completed_on))

    elif choice == "2":
        view_task()

    elif choice == "3":
        input_task = input("Enter Task which Nedd to be updated: ")
        status_to_be_updated = input("Enter Updated Task Status: ")
        task_completed_on_to_be_updated = input("Enter Task Completed On: ")
        mark_task_done_by_task_func(input_task, status_to_be_updated, task_completed_on_to_be_updated)

    elif choice == "4":
        input_task = input("Enter Task which Nedd to be Deleted: ")
        delete_task_By_Task_name_func(input_task)

    elif choice == "5":
        print("Exiting Task Book.")
        break

    else:
        print("Invalid choice.")




# Example usage:
# initialize_file_with_header()
# add_buck_task_func()
# view_task()
# mark_task_done_by_task_func("Dentist visit", "Completed", "27-03-2025")
# delete_task_By_Task_name_func("Homework")
        
