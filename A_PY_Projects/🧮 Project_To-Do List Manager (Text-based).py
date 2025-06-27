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