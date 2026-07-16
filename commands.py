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
    automation = run_automation(text)

    if automation:
        return automation
    if text.startswith("remind me"):
        reminder = text.replace("remind me", "", 1).strip()
        return add_reminder(reminder)

    if "show reminders" in text:
        return show_reminders()
    if text.startswith("add note "):
        note = text.replace("add note ", "", 1)
        return add_note(note)


    if "show my notes" in text:
        return show_notes()
    # Open apps
    if text.startswith("open "):
        app_name = text.replace("open ", "", 1).strip()
        return open_app(app_name)
    # Automatic memory
    if "my name is " in text:
        name = text.split("my name is ", 1)[1].strip()
        remember("name", name)
        return f"Nice to meet you, {name}. I'll remember your name."

    if "i am " in text:
        name = text.split("i am ", 1)[1].strip()
        remember("name", name)
        return f"Hello {name}! I'll remember your name."

    # Remember
    if text.startswith("remember "):
        content = text.replace("remember ", "", 1)

        if " is " in content:
            key, value = content.split(" is ", 1)
            key = clean_key(key)
            remember(key, value.strip())
            return f"I'll remember your {key}."

    # Recall
    elif text.startswith("what is "):
        key = clean_key(text.replace("what is ", "", 1))
        value = recall(key)

        if value:
            return f"Your {key} is {value}."

        return f"I don't know your {key} yet."

    # Forget
    elif text.startswith("forget "):
        key = clean_key(text.replace("forget ", "", 1))
        forget(key)
        return f"I forgot your {key}."
    if "system status" in text:
        return system_status()

    if "time" in text:
        return system_status()

    if "date" in text:
        return system_status()
    return "I don't understand that command yet."
