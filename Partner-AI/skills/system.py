from datetime import datetime

def system_command(message):
    message = message.lower()

    if "time" in message and "tomorrow" not in message:
        return f"The current time is {datetime.now().strftime('%I:%M %p')}."

    # Date handling has been moved to skills/datetime.py

    return None
