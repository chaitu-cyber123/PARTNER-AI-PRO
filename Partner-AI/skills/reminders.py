import json
import os
from datetime import datetime
import dateparser

REMINDER_FILE = "data/reminders.json"


def load_reminders():
    if not os.path.exists(REMINDER_FILE):
        return []

    with open(REMINDER_FILE, "r") as f:
        return json.load(f)


def save_reminders(reminders):
    with open(REMINDER_FILE, "w") as f:
        json.dump(reminders, f, indent=4)


def reminder_command(message):

    text = message.lower().strip()
    reminders = load_reminders()

    # Add reminder
    if text.startswith("remind me"):

        if " to " not in message.lower():
            return "Please tell me what to remind you about."

        before, title = message.split(" to ", 1)

        when = before.lower().replace("remind me", "").strip()

        print("WHEN =", repr(when))

        dt = dateparser.parse(
            when,
            settings={
                "PREFER_DATES_FROM": "future"
            }
        )

        print("PARSED =", dt)
        if dt is None:
            return "I couldn't understand the reminder time."

        reminder = {
            "id": len(reminders) + 1,
            "title": title.strip(),
            "time": dt.strftime("%Y-%m-%d %H:%M:%S"),
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "completed": False
        }

        reminders.append(reminder)
        save_reminders(reminders)

        return f"Reminder added for {reminder['time']}."

    # Show reminders
    if text in ["show reminders", "my reminders"]:

        if not reminders:
            return "You have no reminders."

        lines = []

        for r in reminders:
            mark = "✓" if r["completed"] else "•"
            lines.append(
                f"{r['id']}. {mark} {r['title']} ({r['time']})"
            )

        return "\n".join(lines)

    # Delete reminder
    if text.startswith("delete reminder"):

        try:
            number = int(text.replace("delete reminder", "").strip())

            reminders = [
                r for r in reminders
                if r["id"] != number
            ]

            # Re-number IDs
            for i, r in enumerate(reminders, start=1):
                r["id"] = i

            save_reminders(reminders)

            return "Reminder deleted."

        except:
            return "Invalid reminder number."

    # Clear reminders
    if text == "clear reminders":

        save_reminders([])

        return "All reminders cleared."

    return None
