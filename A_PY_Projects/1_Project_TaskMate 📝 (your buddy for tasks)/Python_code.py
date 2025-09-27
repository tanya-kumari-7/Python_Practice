"""
To-Do List App (Console)
Add, delete, update tasks.
Save tasks in a text file or JSON.
Learn basics of lists, loops, and file handling.
"""
# Imports 
from datetime import datetime
import pandas as pd

#  Create a text file and add tasks 

def add_task(task_id,task_name,status,date):
    if not (task_id and task_name and status and date):
        return "Enter complete task details :task_id,task_name,status,date(format: yyyy-mm-dd)"
    else:
        with open("text_book.txt","a") as file:
            file.write(f"{task_id}|{task_name}|{status}|{date}\n")
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


def view_all_task():
    with open("text_book.txt", "r") as file:
        file_details = file.readlines()

        for line in file_details:
            print(line.strip())  # removes \n so it looks clean
   
view_all_task()

def view_task_by_id(id):
    if not id:
        print("Please enter your task id")
    else:
        case_status = False
        input_id = str(id).strip()
        with open("text_book.txt", "r") as file:
            file_details = file.readlines()

            for line in file_details:
                task_id,task_name,status,date = line.strip().split("|")
                if task_id == input_id:
                    case_status = True
                    return line.strip()
                else:
                    continue
        if not case_status:
            print(f"{input_id} : Id not found, please enter vaild id or please add task with this id [If ANY]")

view_task_by_id(19)



def delete_task_by_id(task_id):
    input_task_id = str(task_id)

    with open("text_book.txt","r") as file:
        task_details = file.readlines()

        update_task = []
        case_status = False

        for line in task_details:
            task_id,task_name,status,date = line.strip().split("|")
            if task_id == input_task_id:
                print(f"Task Found: It will be deleted fro the book",{line})
                case_status = True
                continue
            else:
                update_task.append(line)

        with open("text_book.txt","w") as file:
            file.writelines(update_task)

        if not case_status:
            print(f"{input_task_id}, Not found in the book")

delete_task_by_id(20)

def update_status_date_by_id (id,updated_status,date):
    if not updated_status or not date or not id:
        print("Please enter status which need to be updated and date")
    else:
        id
        input_updated_status = updated_status.strip()
        input_date = str(date).strip()
        input_id = str(id).strip()

        updated_list = []
        case_status= False
        with open("text_book.txt","r") as file:
            file_details = file.readlines()

            for line in file_details:
                task_id,task_name,status,date = line.strip().split("|")
                if str(task_id) == str(input_id):
                    case_status = True
                    new_line =f"{task_id}|{task_name}|{input_updated_status}|{input_date}\n"
                    updated_list.append(new_line)
                    print("Details updated")
                else:
                    updated_list.append(line)
            with open("text_book.txt","w") as file:
                file.writelines(updated_list)

            if not case_status:
                print(f"{input_id} id not found in the book, please re-check")

update_status_date_by_id(19,"Completed","2025-09-26")   


def task_summary_by_status():
    with open("text_book.txt","r") as file:
        file_details = file.readlines()

        for line in file_details:
            # task_id,task_name,status,date 
            df = pd.read_csv("text_book.txt",
                             sep="|",
                             header= None,
                             names=["task_id","task_name","status","date"])
            task_distribution = df.groupby("status")["task_id"].count()
            return task_distribution

task_summary_by_status()

def month_wise_task_summary():
    with open("text_book.txt","r") as file:
        file_details = file.readlines()

        for line in file_details:

            df = pd.read_csv("text_book.txt",
                             sep="|",
                             header= None,
                             names=["task_id","task_name","status","date"])
            return df
        
month_wise_task_summary()
        




                

                    
            
                    


