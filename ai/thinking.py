from ai.memory import smart_recall
from ai.knowledge import search_knowledge


def think(user_message):

    result = {
        "memory": None,
        "knowledge": None,
        "confidence": 0
    }

    # Search memory
    memory = smart_recall(user_message)

    if memory:
        result["memory"] = memory
        result["confidence"] += 50

    # Search knowledge
    knowledge = search_knowledge(user_message)

    if knowledge:
        result["knowledge"] = knowledge
        result["confidence"] += 50

    return result
