import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("TaskMate - Task Manager UI")

menu = ["View All Tasks", "Add Task", "View Task by ID", "Delete Task", "Update Task", "Task Summary", "Month-wise Summary"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "View All Tasks":
    st.header("All Tasks")
    resp = requests.get(f"{API_URL}/view_all_task")
    if resp.ok:
        tasks = resp.json().get("tasks", [])
        for t in tasks:
            st.write(t)
    else:
        st.error("Failed to fetch tasks.")

elif choice == "Add Task":
    st.header("Add New Task")
    task_id = st.text_input("Task ID")
    task_name = st.text_input("Task Name")
    status = st.selectbox("Status", ["Pending", "In Progress", "Completed"])
    date = st.date_input("Date")
    if st.button("Add Task"):
        payload = {
            "task_id": task_id,
            "task_name": task_name,
            "status": status,
            "date": date.strftime("%Y-%m-%d")
        }
        resp = requests.post(f"{API_URL}/add_task", params=payload)
        st.success(resp.json().get("result", "Error"))

elif choice == "View Task by ID":
    st.header("View Task by ID")
    task_id = st.text_input("Enter Task ID")
    if st.button("View Task"):
        resp = requests.get(f"{API_URL}/view_task_by_id/{task_id}")
        st.write(resp.json().get("result", "Not found"))

elif choice == "Delete Task":
    st.header("Delete Task")
    task_id = st.text_input("Enter Task ID to Delete")
    if st.button("Delete Task"):
        resp = requests.delete(f"{API_URL}/delete_task_by_id/{task_id}")
        st.success(resp.json().get("result", "Error"))

elif choice == "Update Task":
    st.header("Update Task Status/Date")
    task_id = st.text_input("Task ID")
    updated_status = st.selectbox("Updated Status", ["Pending", "In Progress", "Completed"])
    date = st.date_input("Updated Date")
    if st.button("Update Task"):
        payload = {
            "updated_status": updated_status,
            "date": date.strftime("%Y-%m-%d")
        }
        resp = requests.put(f"{API_URL}/update_status_date_by_id/{task_id}", params=payload)
        st.success(resp.json().get("result", "Error"))

elif choice == "Task Summary":
    st.header("Task Summary by Status")
    resp = requests.get(f"{API_URL}/task_summary_by_status")
    if resp.ok:
        st.json(resp.json())
    else:
        st.error("Failed to fetch summary.")

elif choice == "Month-wise Summary":
    st.header("Month-wise Task Summary")
    resp = requests.get(f"{API_URL}/month_wise_task_summary")
    if resp.ok:
        st.json(resp.json())
    else:
        st.error("Failed to fetch summary.")
