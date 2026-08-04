from core.context_engine import get_context


def resolve_reference(message):

    text = message.lower()

    reference_words = [
        "it",
        "that",
        "this file",
        "last file",
        "previous file"
    ]

    if not any(word in text for word in reference_words):
        return None


    # Only return reference
    # Actual action will decide what to do

    last_file = get_context("last_file")

    return last_file
