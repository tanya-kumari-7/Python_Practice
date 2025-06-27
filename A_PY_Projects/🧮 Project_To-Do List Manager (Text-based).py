""" Creating a function to add task in a file """

def add_task(task):
    if not task.strip():
        return "❌ Task cannot be empty."

    with open("tasks.txt", "a") as file:
        file.write(task + " | Not Done\n")
    return "✅ Task added!"


def read_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("📭 No tasks found.")
            else:
                print("📝 Your Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("⚠️ Task file not found. Add a task first.")
        
def delete_task_by_name(task_name):
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        task_found = False
        for i, task in enumerate(tasks):
            if task_name in task:
                deleted = tasks.pop(i)
                task_found = True
                break

        if task_found:
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print(f"🗑️ Task deleted: {deleted.strip()}")
        else:
            print("❌ Task not found.")

    except FileNotFoundError:
        print("⚠️ Task file not found.")