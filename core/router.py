def detect_intent(prompt):

    text = prompt.lower().strip()

    if text.startswith("my "):
        return "MEMORY"

    if text.startswith((
        "what",
        "who",
        "where",
        "when",
        "why",
        "how"
    )):
        return "KNOWLEDGE"

    return "GENERAL"
