from fastapi import FastAPI
from typing import Optional
import pandas as pd
from task_apis import add_task, view_all_task, view_task_by_id, delete_task_by_id, update_status_date_by_id, task_summary_by_status, month_wise_task_summary

app = FastAPI()

@app.post("/add_task")
def api_add_task(task_id: str, task_name: str, status: str, date: str):
    return {"result": add_task(task_id, task_name, status, date)}

@app.get("/view_all_task")
def api_view_all_task():
    return {"tasks": view_all_task()}

@app.get("/view_task_by_id/{task_id}")
def api_view_task_by_id(task_id: str):
    return {"result": view_task_by_id(task_id)}

@app.delete("/delete_task_by_id/{task_id}")
def api_delete_task_by_id(task_id: str):
    return {"result": delete_task_by_id(task_id)}

@app.put("/update_status_date_by_id/{task_id}")
def api_update_status_date_by_id(task_id: str, updated_status: str, date: str):
    return {"result": update_status_date_by_id(task_id, updated_status, date)}

@app.get("/task_summary_by_status")
def api_task_summary_by_status():
    summary = task_summary_by_status()
    if hasattr(summary, 'to_dict'):
        return summary.to_dict()
    return {"result": summary}

@app.get("/month_wise_task_summary")
def api_month_wise_task_summary():
    summary = month_wise_task_summary()
    if hasattr(summary, 'to_dict'):
        return summary.to_dict()
    return {"result": summary}
