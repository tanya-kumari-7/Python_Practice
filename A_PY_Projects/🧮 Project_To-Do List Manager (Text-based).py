""" Creating a function to add task in a file """

def add_task(task):
    if not task.strip():
        return "❌ Task cannot be empty."

    with open("tasks.txt", "a") as file:
        file.write(task + " | Not Done\n")
    return "✅ Task added!"

