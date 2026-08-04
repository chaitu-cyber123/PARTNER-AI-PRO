from skills.router import handle_command


def execute(state):

    intent = state["plan"]["intent"]

    if intent == "conversation":

        return None

    message = state["input"]

    result = handle_command(message)

    return result

