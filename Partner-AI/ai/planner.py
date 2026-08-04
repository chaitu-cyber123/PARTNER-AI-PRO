from core.intent import detect_intent


SKILL_MAP = {

    "list_files": "files",
    "open_file": "files",

    "show_notes": "notes",
    "create_note": "notes",

    "create_reminder": "reminders",
    "show_reminders": "reminders",

    "calculator": "calculator",

    "news": "briefing",

    "weather": "weather",

    "browser": "browser",

    "converter": "converter",

    "profile": "profile",

    "status": "status",

    "tasks": "tasks",

    "system": "system"
}


def plan(user_message):

    intent = detect_intent(user_message)


    if intent == "conversation":

        return {
            "action": "chat",
            "intent": intent
        }


    if intent in SKILL_MAP:

        return {
            "action": "skill",
            "skill": SKILL_MAP[intent],
            "intent": intent
        }


    return {
        "action": "chat",
        "intent": intent
    }
