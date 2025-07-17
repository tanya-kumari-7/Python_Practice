def create_task(task,task_added_on,task_due_on,status)
    if not task or not task_added_on or not task_due_on or not status:
        return "Please Add Tasks"
    else:
        with open("taskManagerbook.txt","a") as file:
            file.write(f"{task} | {task_added_on} | {task_due_on} | {status}\n")
            return "Task Added"
        



