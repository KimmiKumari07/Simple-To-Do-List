import json
import os


class Task:
    def __init__(self, title, description, category, completed=False):
        self.title = title
        self.description = description
        self.category = category
        self.completed = completed

    def mark_completed(self):
        self.completed = True


FILE_NAME = "tasks.json"


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump([task.__dict__ for task in tasks], file, indent=4)


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        data = json.load(file)
        return [Task(**task) for task in data]


def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    category = input("Enter category (Work/Personal/Urgent): ")

    task = Task(title, description, category)
    tasks.append(task)

    print("Task added successfully!")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\n----- TASK LIST -----")

    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task.completed else "Pending"

        print(f"\nTask {i}")
        print(f"Title       : {task.title}")
        print(f"Description : {task.description}")
        print(f"Category    : {task.category}")
        print(f"Status      : {status}")


def mark_completed(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_num = int(input("\nEnter task number to mark completed: "))

        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1].mark_completed()
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_num = int(input("\nEnter task number to delete: "))

        if 1 <= task_num <= len(tasks):
            deleted = tasks.pop(task_num - 1)
            print(f"Task '{deleted.title}' deleted successfully!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = load_tasks()

    while True:
        print("\n========== TO-DO LIST ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            mark_completed(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved successfully!")
            print("Exiting application...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()