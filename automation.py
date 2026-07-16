from apps import open_app


def run_automation(command):

    command = command.lower()

    if "good morning" in command:
        return (
            "Good morning sir. "
            "Partner is ready for the day."
        )

    if "study mode" in command:
        return (
            "Study mode activated sir. "
            "Opening your study environment."
        )

    if "entertainment mode" in command:
        return open_app("youtube")

    if "shutdown mode" in command:
        return "Shutdown sequence initiated."

    return None
