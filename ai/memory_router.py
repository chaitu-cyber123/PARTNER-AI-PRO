from ai.memory import remember
from ai.knowledge import save_knowledge


def process_memory(text):

    original = text.strip()
    lower = original.lower()


    # -------------------------
    # PERSONAL MEMORY
    # -------------------------

    if lower.startswith("my ") and " is " in lower:

        key, value = original.split(
            " is ",
            1
        )

        key = key.replace(
            "my ",
            ""
        ).strip()


        remember(
            key,
            value.strip()
        )


        return (
            f"I will remember that "
            f"your {key} is {value.strip()}."
        )


    # -------------------------
    # PROJECT MEMORY
    # -------------------------

    project_words = [
        "i am building",
        "i'm building",
        "i am working on",
        "i'm working on",
        "my project is"
    ]


    for word in project_words:

        if lower.startswith(word):

            remember(
                "project",
                original
            )

            return "I will remember your project details."



    # -------------------------
    # KNOWLEDGE LEARNING
    # -------------------------

    if " is " in lower:

        question, answer = original.split(
            " is ",
            1
        )


        # Ignore questions
        if question.lower().startswith(
            (
                "what",
                "who",
                "where",
                "when",
                "why",
                "how"
            )
        ):
            return None


        save_knowledge(
            "what is " + question.strip(),
            answer.strip()
        )


        return (
            "I learned that information "
            "and stored it permanently."
        )


    return None
