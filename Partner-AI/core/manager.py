from core.router import detect_intent

from ai.memory_router import process_memory
from ai.knowledge import search_knowledge
from ai.memory import smart_recall


def process(prompt):

    # Smart memory lookup
    memory = smart_recall(prompt)
    if memory:
        return f"I remember that: {memory}"

    # Detect intent
    intent = detect_intent(prompt)

    # Save personal memory
    if intent == "MEMORY":
        result = process_memory(prompt)
        if result:
            return result

    # Knowledge lookup
    result = search_knowledge(prompt)
    if result:
        return result

    # Nothing found
    return (
    "I'm sorry, I don't know the answer yet. "
    "You can teach me using the learn command, "
    "or I'll answer it once a local AI model is connected."
)
