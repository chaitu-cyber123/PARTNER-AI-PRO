from datetime import datetime, timedelta

def datetime_command(query):

    text = query.lower()

    now = datetime.now()
    tomorrow = now + timedelta(days=1)

    # Tomorrow's date
    if "tomorrow" in text and "date" in text:
        return tomorrow.strftime("Tomorrow's date is %d %B %Y.")

    # Tomorrow's day
    if "tomorrow" in text and "day" in text:
        return tomorrow.strftime("Tomorrow is %A.")

    # Today's date
    if "today" in text and "date" in text:
        return now.strftime("Today's date is %d %B %Y.")

    # Today's day
    if "today" in text and "day" in text:
        return now.strftime("Today is %A.")

    # Generic date
    if "date" in text:
        return now.strftime("Today's date is %d %B %Y.")

    # Generic day
    if (
        "what day" in text
        or "which day" in text
        or text.strip() == "day"
    ):
        return now.strftime("Today is %A.")

    # Time
    if "time" in text:
        return now.strftime("Current time is %I:%M %p.")

    return None
