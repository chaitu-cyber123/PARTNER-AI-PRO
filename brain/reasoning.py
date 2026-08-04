def reason(state):

    thoughts = []

    if state["memory"]["found"]:
        thoughts.append("Relevant memory found.")

    if state["knowledge"]["found"]:
        thoughts.append("Relevant knowledge found.")

    if not thoughts:
        thoughts.append("No matching memory or knowledge.")

    return {
        "thoughts": thoughts,
        "confidence": (
            state["memory"]["found"] * 50 +
            state["knowledge"]["found"] * 50
       )
    }
