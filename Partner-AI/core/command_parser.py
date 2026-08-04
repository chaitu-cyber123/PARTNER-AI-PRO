def normalize_command(message):

    text = message.lower().strip()


    replacements = {

        "can you show": "show",

        "please show": "show",

        "tell me": "",

        "what are my": "show my",

        "what is my": "",

        "give me": "show",

        "remove my": "delete",

        "erase my": "delete",

        "delete my": "delete",

        "set a": "create",

        "make a": "create"

    }


    for old, new in replacements.items():

        text = text.replace(
            old,
            new
        )


    return text.strip()
