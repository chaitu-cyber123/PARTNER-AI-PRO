import json
import os

TASK_FILE = "data/tasks.json"


def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []

    with open(TASK_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def task_command(message):
    text = message.lower().strip()

    tasks = load_tasks()

    # Add task
    if text.startswith("add task"):
        task = message[8:].strip()

        if not task:
            return "Please tell me what task to add."

        tasks.append({
            "title": task,
            "done": False
        })

        save_tasks(tasks)

        return f"Task added: {task}"

    # Show tasks
    if text in ["show tasks", "my tasks", "list tasks"]:

        if not tasks:
            return "You have no tasks."

        output = []

        for i, task in enumerate(tasks, start=1):
            mark = "✓" if task["done"] else "•"
            output.append(f"{i}. {mark} {task['title']}")

        return "\n".join(output)

    # Complete task
    if text.startswith("complete task"):

        try:
            number = int(text.replace("complete task", "").strip())

            tasks[number - 1]["done"] = True

            save_tasks(tasks)

            return "Task completed."

        except:
            return "Invalid task number."

    # Delete task
    if text.startswith("delete task"):

        try:
            number = int(text.replace("delete task", "").strip())

            removed = tasks.pop(number - 1)

            save_tasks(tasks)

            return f"Deleted: {removed['title']}"

        except:
            return "Invalid task number."

    # Clear tasks
    if text == "clear tasks":

        save_tasks([])

        return "All tasks cleared."

    return None
