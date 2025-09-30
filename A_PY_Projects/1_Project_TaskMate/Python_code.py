"""
To-Do List App (Console)
Add, delete, update tasks.
Save tasks in a text file or JSON.
Learn basics of lists, loops, and file handling.
"""
from fastapi import FastAPI
from typing import Optional
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import pandas as pd
import os

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
TASK_FILE = "text_book.txt"

#  Create a text file and add tasks 

def add_task(task_id,task_name,status,date):
    if not (task_id and task_name and status and date):
        return "Enter complete task details :task_id,task_name,status,date(format: yyyy-mm-dd)"
    else:
        with open(TASK_FILE,"a") as file:
            file.write(f"{task_id}|{task_name}|{status}|{date}\n")
            return "Task Added !! :)"

@app.post("/add_task")
def api_add_task(task_id: str, task_name: str, status: str, date: str):
    result = add_task(task_id, task_name, status, date)
    return {"result": result}
        
# add_task("1", "Update Trade Details", "Pending", "2025-01-01")
# add_task("2", "Check Payment Records", "In Progress", "2025-01-03")
# add_task("3", "Review Client Feedback", "Completed", "2025-01-05")
# add_task("4", "Prepare Monthly Report", "Pending", "2025-01-07")
# add_task("5", "Fix Dashboard Bugs", "In Progress", "2025-01-10")
# add_task("6", "Conduct Team Meeting", "Pending", "2025-01-12")
# add_task("7", "Update API Documentation", "Completed", "2025-01-15")
# add_task("8", "Test New Features", "Pending", "2025-01-18")
# add_task("9", "Analyze Market Data", "In Progress", "2025-01-20")
# add_task("10", "Optimize SQL Queries", "Pending", "2025-01-22")
# add_task("11", "Clean User Database", "Completed", "2025-01-25")
# add_task("12", "Design New Dashboard", "Pending", "2025-01-27")
# add_task("13", "Review Security Logs", "Pending", "2025-01-28")
# add_task("14", "Check Backup Files", "Completed", "2025-01-29")
# add_task("15", "Send Invoice Reminders", "In Progress", "2025-02-01")
# add_task("16", "Verify Tax Filings", "Pending", "2025-02-03")
# add_task("17", "Train New Employees", "Completed", "2025-02-05")
# add_task("18", "Prepare Presentation", "Pending", "2025-02-07")
# add_task("19", "Update User Permissions", "In Progress", "2025-02-10")
# add_task("20", "Plan Product Launch", "Pending", "2025-02-12")


def view_all_task():
    with open(TASK_FILE, "r") as file:
        file_details = file.readlines()
        for line in file_details:
            print(line.strip())  

@app.get("/view_all_task")
def api_view_all_task():
    if not os.path.exists(TASK_FILE):
        return {"tasks": []}
    with open(TASK_FILE, "r") as file:
        file_details = file.readlines()
    tasks = [line.strip() for line in file_details]
    return {"tasks": tasks}

def view_task_by_id(id):
    if not id:
        print("Please enter your task id")
    else:
        case_status = False
        input_id = str(id).strip()
        with open(TASK_FILE, "r") as file:
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

@app.get("/view_task_by_id")
def api_view_task_by_id(id: str):
    if not id:
        return {"error": "Please enter your task id"}
    case_status = False
    input_id = str(id).strip()
    if not os.path.exists(TASK_FILE):
        return {"error": "Task file not found"}
    with open(TASK_FILE, "r") as file:
        file_details = file.readlines()
        for line in file_details:
            task_id, task_name, status, date = line.strip().split("|")
            if task_id == input_id:
                case_status = True
                return {"task": line.strip()}
    return {"error": f"{input_id} : Id not found, please enter valid id or please add task with this id [If ANY]"}

# view_task_by_id(19)



def delete_task_by_id(task_id):
    input_task_id = str(task_id)
    with open(TASK_FILE,"r") as file:
        task_details = file.readlines()
        update_task = []
        case_status = False
        for line in task_details:
            tid,task_name,status,date = line.strip().split("|")
            if tid == input_task_id:
                print(f"Task Found: It will be deleted fro the book",{line})
                case_status = True
                continue
            else:
                update_task.append(line)
        with open(TASK_FILE,"w") as file:
            file.writelines(update_task)
        if not case_status:
            print(f"{input_task_id}, Not found in the book")

@app.delete("/delete_task_by_id")
def api_delete_task_by_id(task_id: str):
    input_task_id = str(task_id)
    if not os.path.exists(TASK_FILE):
        return {"error": "Task file not found"}
    with open(TASK_FILE, "r") as file:
        task_details = file.readlines()
    update_task = []
    case_status = False
    for line in task_details:
        tid, task_name, status, date = line.strip().split("|")
        if tid == input_task_id:
            case_status = True
            continue
        else:
            update_task.append(line)
    with open(TASK_FILE, "w") as file:
        file.writelines(update_task)
    if not case_status:
        return {"error": f"{input_task_id}, Not found in the book"}
    return {"message": "Task deleted if found"}

# delete_task_by_id(20)

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
        with open(TASK_FILE,"r") as file:
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
            with open(TASK_FILE,"w") as file:
                file.writelines(updated_list)
            if not case_status:
                print(f"{input_id} id not found in the book, please re-check")

@app.put("/update_status_date_by_id")
def api_update_status_date_by_id(id: str, updated_status: str, date: str):
    if not updated_status or not date or not id:
        return {"error": "Please enter status which need to be updated and date"}
    input_updated_status = updated_status.strip()
    input_date = str(date).strip()
    input_id = str(id).strip()
    if not os.path.exists(TASK_FILE):
        return {"error": "Task file not found"}
    updated_list = []
    case_status = False
    with open(TASK_FILE, "r") as file:
        file_details = file.readlines()
        for line in file_details:
            task_id, task_name, status, date = line.strip().split("|")
            if str(task_id) == str(input_id):
                case_status = True
                new_line = f"{task_id}|{task_name}|{input_updated_status}|{input_date}\n"
                updated_list.append(new_line)
            else:
                updated_list.append(line)
    with open(TASK_FILE, "w") as file:
        file.writelines(updated_list)
    if not case_status:
        return {"error": f"{input_id} id not found in the book, please re-check"}
    return {"message": "Details updated"}

# update_status_date_by_id(19,"Completed","2025-09-26")   


def task_summary_by_status():
    with open(TASK_FILE,"r") as file:
        file_details = file.readlines()
        for line in file_details:
            df = pd.read_csv(TASK_FILE,
                             sep="|",
                             header= None,
                             names=["task_id","task_name","status","date"])
            task_distribution = df.groupby("status")["task_id"].count()
            return task_distribution

@app.get("/task_summary_by_status")
def api_task_summary_by_status():
    if not os.path.exists(TASK_FILE):
        return {"summary": {}}
    df = pd.read_csv(TASK_FILE, sep="|", header=None, names=["task_id", "task_name", "status", "date"])
    task_distribution = df.groupby("status")["task_id"].count().to_dict()
    return {"summary": task_distribution}

# task_summary_by_status()

def month_wise_task_summary():
    with open(TASK_FILE,"r") as file:
        file_details = file.readlines()
        for line in file_details:
            df = pd.read_csv(TASK_FILE,
                             sep="|",
                             header= None,
                             names=["task_id","task_name","status","date"])
            df["date"] = pd.to_datetime(df["date"])
            df["month"] = df["date"].dt.month
            df["month_name"] = df["date"].dt.strftime("%B")
            month_wise_task_summary_ = df.groupby(["month_name","status"])["task_id"].count()
            return month_wise_task_summary_

@app.get("/month_wise_task_summary")
def api_month_wise_task_summary():
    if not os.path.exists(TASK_FILE):
        return {"summary": {}}
    df = pd.read_csv(TASK_FILE, sep="|", header=None, names=["task_id", "task_name", "status", "date"])
    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.month
    df["month_name"] = df["date"].dt.strftime("%B")
    month_wise_task_summary_ = df.groupby(["month_name", "status"])["task_id"].count().to_dict()
    return {"summary": month_wise_task_summary_}
        




                

                    
            
                    


