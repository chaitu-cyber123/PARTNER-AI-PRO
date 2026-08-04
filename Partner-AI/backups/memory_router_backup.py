from ai.memory import remember
from ai.knowledge import save_knowledge


def process_memory(text):

    original = text.strip()
    lower = original.lower()


    # -------------------------
    # PERSONAL FACTS
    # -------------------------

    if lower.startswith("my "):

        if " is " in lower:

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
    # KNOWLEDGE LEARNING
    # -------------------------

    # Ignore questions
    if lower.startswith(
        (
            "what",
            "who",
            "where",
            "when",
            "why",
            "how",
            "can",
            "do",
            "does"
        )
    ):
        return None


    if " is " in original:

        question, answer = original.split(
            " is ",
            1
        )

        question = (
            "what is "
            + question.strip()
        )

        save_knowledge(
            question,
            answer.strip()
        )

        return (
            "I learned that information "
            "and stored it permanently."
        )
