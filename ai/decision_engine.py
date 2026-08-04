from ai.inference import infer


def decide(user_message):

    result = infer(user_message)

    if result["type"] == "combined":
        return {
            "action": "respond",
            "answer": result["answer"]
        }

    if result["type"] == "memory":
        return {
            "action": "respond",
            "answer": result["answer"]
        }

    if result["type"] == "knowledge":
        return {
            "action": "respond",
            "answer": result["answer"]
        }

    return {
        "action": "learn",
        "answer": "I don't know that yet. Please teach me."
    }
