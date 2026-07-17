from memory import remember, recall, forget
from apps import open_app
from system_info import system_status
from notes import add_note, show_notes
from reminders import add_reminder, show_reminders
from automation import run_automation


def clean_key(text):
    text = text.lower()
    text = text.replace("my ", "")
    text = text.replace("the ", "")
    text = text.replace("favourite", "favorite")
    text = text.replace("colour", "color")
    return text.strip()


def handle_command(text):
    text = text.lower().strip()

    # Greetings
    if "hello" in text or "hi" in text or "hey" in text:
        return "Hello sir. Partner AI is online. How may I assist you?"

    # Automation
    automation = run_automation(text)
    if automation:
        return automation

    # Reminders
    if text.startswith("remind me"):
        reminder = text.replace("remind me", "", 1).strip()
        return add_reminder(reminder)

    if "show reminders" in text:
        return show_reminders()

    # Notes
    if text.startswith("add note "):
        note = text.replace("add note ", "", 1)
        return add_note(note)

    if "show my notes" in text:
        return show_notes()
#open apps

    if text.startswith("open "):

    app = text.replace("open ", "", 1).strip()

    with open("action.txt", "w") as f:
        f.write(app)

    return f"Opening {app}..."
    # Learn user's name
    if "my name is " in text:
        name = text.split("my name is ", 1)[1].strip()
        remember("name", name)
        return f"Nice to meet you, {name}. I'll remember your name."

    if "i am " in text:
        name = text.split("i am ", 1)[1].strip()
        remember("name", name)
        return f"Hello {name}! I'll remember your name."

    # Remember facts
    if text.startswith("remember "):
        content = text.replace("remember ", "", 1)

        if " is " in content:
            key, value = content.split(" is ", 1)
            remember(clean_key(key), value.strip())
            return f"I'll remember your {clean_key(key)}."

    # Recall facts
    if text.startswith("what is "):
        key = clean_key(text.replace("what is ", "", 1))
        value = recall(key)

        if value:
            return f"Your {key} is {value}."

        return None

    # Forget
    if text.startswith("forget "):
        key = clean_key(text.replace("forget ", "", 1))
        forget(key)
        return f"I forgot your {key}."

    # System
    if "system status" in text or "time" in text or "date" in text:
        return system_status()

    # Unknown command
    return None
