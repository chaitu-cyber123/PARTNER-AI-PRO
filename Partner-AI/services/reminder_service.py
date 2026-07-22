import json
import os
import threading
import time
from datetime import datetime

from services.voice import speak

NOTIFICATION_FILE = "data/notifications.json"


def save_notification(message):

    notifications = []

    if os.path.exists(NOTIFICATION_FILE):
        with open(NOTIFICATION_FILE, "r") as f:
            notifications = json.load(f)

    notifications.append({
        "message": message,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    with open(NOTIFICATION_FILE, "w") as f:
        json.dump(notifications, f, indent=4)
REMINDER_FILE = "data/reminders.json"


def check_reminders():

    if not os.path.exists(REMINDER_FILE):
        return []

    with open(REMINDER_FILE, "r") as f:
        reminders = json.load(f)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    triggered = []
    changed = False

    for reminder in reminders:

         if (
    reminder.get("completed") == False
    and reminder["time"] <= now
):
            triggered.append(reminder)
            reminder["completed"] = True
            changed = True

    if changed:
        with open(REMINDER_FILE, "w") as f:
            json.dump(reminders, f, indent=4)

    return triggered


def reminder_worker():

    while True:

        reminders = check_reminders()

        for reminder in reminders:

            message = f"Reminder. {reminder['title']}"
            save_notification(message)
            print("🔔 REMINDER:", message)

            #speak(message)

        time.sleep(60)


def start_reminder_service():

    thread = threading.Thread(
        target=reminder_worker,
        daemon=True
    )

    thread.start()
