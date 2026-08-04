from ai.memory import load_memory, forget, clear_memory


def memory_command(message):

    if "what do you remember" in message:
        memory = load_memory()

        if not memory:
            return "I don't have any saved memories yet."

        report = "PERSONAL PROFILE\n\n"

        if "profile" in memory:
            report += "PROFILE:\n"
            for key, value in memory["profile"].items():
                report += f"- {key.title()}: {value}\n"

        if "preferences" in memory:
            report += "\nPREFERENCES:\n"
            for key, value in memory["preferences"].items():
                report += f"- {key.replace('_',' ').title()}: {value}\n"

        if "facts" in memory and memory["facts"]:
            report += "\nFACTS:\n"
            for key, value in memory["facts"].items():
                report += f"- {key.title()}: {value}\n"

        return report


    if message.startswith("forget my "):
        key = message.replace("forget my ", "").strip()

        forget(key)

        return f"I forgot your {key}."


    if "clear my memory" in message:
        clear_memory()

        return "All memories cleared."


    return None
