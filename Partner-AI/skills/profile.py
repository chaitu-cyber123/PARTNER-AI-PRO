from ai.memory import update_profile, get_profile_value


def profile_command(message):

    message = message.lower()

    if "my name is" in message:
        name = message.split("my name is", 1)[1].strip()

        if name:
            update_profile("name", name.title())
            return f"I will remember your name as {name.title()}."

    if "my favorite news is" in message:
        category = message.split("my favorite news is", 1)[1].strip()

        if category:
            update_profile("preferred_news", category)
            return f"I will remember your preferred news category as {category}."

    if "what is my name" in message:
        name = get_profile_value("name")

        if name:
            return f"Your name is {name}."
        else:
            return "I don't have your name saved yet."

    return None
