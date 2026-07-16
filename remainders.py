import json
import os

FILE = "data/reminders.json"


def load_reminders():
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r") as f:
        return json.load(f)


def save_reminders(reminders):
    os.makedirs("data", exist_ok=True)

    with open(FILE, "w") as f:
        json.dump(reminders, f, indent=4)


def add_reminder(reminder):
    reminders = load_reminders()
    reminders.append(reminder)
    save_reminders(reminders)

    return "Reminder saved."


def show_reminders():
    reminders = load_reminders()

    if not reminders:
        return "You have no reminders."

    return "Your reminders are: " + ", ".join(reminders)
