def detect_intent(message):

    text = message.lower().strip()


    # -------------------------
    # FILES
    # -------------------------

    file_words = [
        "file",
        "files",
        "document",
        "folder",
        ".py",
        ".txt"
    ]

    file_actions = [
        "open",
        "read",
        "show",
        "list",
        "find",
        "copy",
        "move",
        "rename"
    ]

    if any(word in text for word in file_words):

        if any(action in text for action in file_actions):

            if "open" in text or "read" in text:
                return "open_file"

            if "list" in text or "show" in text:
                return "list_files"


    # -------------------------
    # CALCULATOR
    # -------------------------

    if any(word in text for word in [
        "calculate",
        "calculator",
        "solve",
        "what is",
        "+",
        "-",
        "*",
        "/"
    ]):
        return "calculator"


    # -------------------------
    # NEWS
    # -------------------------

    if any(word in text for word in [
        "news",
        "headline",
        "headlines",
        "updates",
        "what happened"
    ]):
        return "news"


    # -------------------------
    # WEATHER
    # -------------------------

    if any(word in text for word in [
        "weather",
        "temperature",
        "forecast",
        "weather today",
        "what is weather today",
        "what is weather tomorrow",
        "rain"
    ]):
        return "weather"


    # -------------------------
    # NOTES
    # -------------------------

    if "note" in text or "notes" in text:

        if any(word in text for word in [
            "show",
            "list",
            "have",
            "see"
        ]):
            return "show_notes"

        if any(word in text for word in [
            "create",
            "add",
            "save",
            "make"
        ]):
            return "create_note"


    # -------------------------
    # REMINDERS
    # -------------------------

    if any(word in text for word in [
        "remind",
        "reminder",
        "schedule"
    ]):

        if any(word in text for word in [
            "show",
            "list",
            "what"
        ]):
            return "show_reminders"

        return "create_reminder"


    # -------------------------
    # DATE / TIME
    # -------------------------

    if text in [
       "today",
       "what day is today",
       "what is today's date",
       "what time is it",
       "current time"
]:
        return "datetime"


    # -------------------------
    # PROFILE
    # -------------------------

    if any(word in text for word in [
        "my name",
        "who am i",
        "profile",
        "about me"
    ]):
        return "profile"


    # -------------------------
    # STATUS
    # -------------------------

    if any(word in text for word in [
        "status",
        "system status",
        "health"
    ]):
        return "status"


    # -------------------------
    # TASKS
    # -------------------------

    if any(word in text for word in [
        "task",
        "todo",
        "to do"
    ]):
        return "tasks"


    # -------------------------
    # CONVERTER
    # -------------------------

    if any(word in text for word in [
        "convert",
        "conversion",
        "kg",
        "km",
        "meter",
        "celsius",
        "fahrenheit"
    ]):
        return "converter"


    # -------------------------
    # BROWSER
    # -------------------------

    if any(word in text for word in [
        "search",
        "google",
        "open website",
        "browser"
    ]):
        return "browser"


    # -------------------------
    # SYSTEM
    # -------------------------

    if any(word in text for word in [
        "shutdown",
        "restart",
        "terminal",
        "command"
    ]):
        return "system"


    # -------------------------
    # DEFAULT
    # -------------------------

    return "conversation"
