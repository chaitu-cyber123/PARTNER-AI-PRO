from ai.memory import remember


def process_correction(message):

    text = message.lower().strip()


    triggers = [
        "no,",
        "no ",
        "actually",
        "wrong",
        "change it to",
        "it is"
    ]


    if not any(t in text for t in triggers):
        return None


    # Example:
    # "Actually my favorite food is biryani"

    if "my " in text and " is " in text:

        data = message.split(
            " is ",
            1
        )


        key = data[0].replace(
            "Actually",
            ""
        ).replace(
            "actually",
            ""
        ).replace(
            "my ",
            ""
        ).strip()


        value = data[1].strip()


        remember(
            key,
            value
        )


        return (
            f"Understood. "
            f"I updated your {key} to {value}."
        )


    return None
