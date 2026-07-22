from datetime import datetime

def system_command(message):
    message = message.lower()

    if "time" in message:
        return f"The current time is {datetime.now().strftime('%I:%M %p')}."

    if "date" in message:
        return f"Today's date is {datetime.now().strftime('%d %B %Y')}."

    return None
