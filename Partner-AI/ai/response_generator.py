import random


def generate_response(user_message, memory=None, knowledge=None):

    # -------------------------
    # MEMORY
    # -------------------------

    if memory:

        return f"I remember that {memory}."

    # -------------------------
    # KNOWLEDGE
    # -------------------------

    if knowledge:

        return knowledge

    # -------------------------
    # UNKNOWN
    # -------------------------

    replies = [

        "I don't know that yet. Please teach me.",

        "I haven't learned that yet.",

        "I don't have enough information to answer that.",

        "Could you teach me about that?",

        "I'm still learning. Can you explain it to me?"

    ]

    return random.choice(replies)
