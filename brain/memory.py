from ai.memory import smart_recall


def recall(state):

    message = state["input"]

    memory = smart_recall(message)

    if memory:

        return {

            "found": True,

            "content": memory

        }

    return {

        "found": False,

        "content": None

    }
