def respond(state):

    # Skill already produced an answer
    if state["result"]:

        return state["result"]

    # Memory
    if state["memory"]["found"]:

        return state["memory"]["content"]

    # Knowledge
    if state["knowledge"]["found"]:

        return state["knowledge"]["content"]

    return (
        "I don't know yet. "
        "Please teach me."
    )
