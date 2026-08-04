from ai.thinking import think


def infer(user_message):

    thought = think(user_message)

    memory = thought["memory"]
    knowledge = thought["knowledge"]

    # Combine facts
    if memory and knowledge:
        return {
            "type": "combined",
            "answer": f"{knowledge}\n\nBased on what I remember: {memory}"
        }

    # Memory only
    if memory:
        return {
            "type": "memory",
            "answer": memory
        }

    # Knowledge only
    if knowledge:
        return {
            "type": "knowledge",
            "answer": knowledge
        }

    # Unknown
    return {
        "type": "unknown",
        "answer": None
    }
