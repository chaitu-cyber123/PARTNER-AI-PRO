import json
import os
import threading
import time
from datetime import datetime

from services.voice import speak

NOTIFICATION_FILE = "data/notifications.json"
REMINDER_FILE = "data/reminders.json"


def load_json_file(filepath, default):
    """Safely load JSON data without crashing Partner."""

    if not os.path.exists(filepath):
        return default

    try:
        with open(filepath, "r") as f:
            data = json.load(f)

        return data

    except (json.JSONDecodeError, OSError) as e:
        print(f"⚠️ Could not read {filepath}: {e}")
        return default


def save_json_file(filepath, data):
    """Safely save JSON data."""

    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)

        return True

    except OSError as e:
        print(f"❌ Could not save {filepath}: {e}")
        return False


def save_notification(message):

    notifications = load_json_file(NOTIFICATION_FILE, [])

    if not isinstance(notifications, list):
        notifications = []

    notifications.append({
        "message": message,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    save_json_file(NOTIFICATION_FILE, notifications)


def check_reminders():

    reminders = load_json_file(REMINDER_FILE, [])

    if not isinstance(reminders, list):
        print(f"⚠️ Invalid reminder format in {REMINDER_FILE}")
        return []

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    triggered = []
    changed = False

    for reminder in reminders:

        if not isinstance(reminder, dict):
            continue

        if (
            reminder.get("completed") is False
            and reminder.get("time")
            and reminder["time"] <= now
        ):
            triggered.append(reminder)
            reminder["completed"] = True
            changed = True

    if changed:
        save_json_file(REMINDER_FILE, reminders)

    return triggered


def reminder_worker():

    print("🔔 Reminder worker started")

    while True:

        try:
            reminders = check_reminders()

            for reminder in reminders:

                message = f"Reminder. {reminder.get('title', 'You have a reminder')}"

                save_notification(message)

                print("🔔 REMINDER:", message)

                # Browser/HUD voice can handle this later.
                # speak(message)

        except Exception as e:
            print(f"❌ Reminder worker error: {e}")

        time.sleep(60)


def start_reminder_service():

    thread = threading.Thread(
        target=reminder_worker,
        daemon=True
    )

    thread.start()

