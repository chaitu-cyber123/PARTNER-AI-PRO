from ai.knowledge import search_knowledge


def search(state):

    message = state["input"]

    answer = search_knowledge(message)

    if answer:

        return {

            "found": True,

            "content": answer

        }

    return {

        "found": False,

        "content": None

    }
