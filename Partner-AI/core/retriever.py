from ai.memory import smart_recall
from ai.knowledge import search_knowledge


def reason(message):

    text = message.lower().strip()


    # Check memory first

    memory = smart_recall(text)

    if memory:
        return {
            "type": "memory",
            "data": memory
        }


    # Check knowledge

    knowledge = search_knowledge(text)

    if knowledge:
        return {
            "type": "knowledge",
            "data": knowledge
        }


    return None
