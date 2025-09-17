""" Creating a function to add task in a file """

def add_task(task):
    if not task.strip():
        return "Task cannot be empty."

    with open("tasks.txt", "a") as file:
        file.write(task + " | Not Done\n")
    return "Task added!"


def read_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("📭 No tasks found.")
            else:
                print("Your Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("Task file not found. Add a task first.")
        
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
            print(f"Task deleted: {deleted.strip()}")
        else:
            print("Task not found.")

    except FileNotFoundError:
        print("Task file not found.")
        
        
def mark_done(task_number):
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if 0 < task_number <= len(tasks):
            task_text = tasks[task_number - 1].split(" |")[0]
            tasks[task_number - 1] = f"{task_text} | Done\n"
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except FileNotFoundError:
        print("tasks.txt file not found.")
        
        
# ✅ Main menu loop (properly indented)
while True:
    print("\nTo-Do List Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task by Name")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        task = input("Enter task description: ")
        print(add_task(task))

    elif choice == "2":
        read_tasks()

    elif choice == "3":
        num = int(input("Enter task number to mark as done: "))
        mark_done(num)

    elif choice == "4":
        name = input("Enter task name to delete: ")
        delete_task_by_name(name)

    elif choice == "5":
        print("Exiting. Have a productive day!")
        break

    else:
        print("Invalid choice.")