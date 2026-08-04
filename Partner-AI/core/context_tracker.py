from core.context_engine import set_context


def update_context(message, result=None):

    text = message.lower()


    # File tracking
    if "open " in text or "read " in text:

        words = message.split()

        for word in words:

            if "." in word:
                set_context(
                    "last_file",
                    word
                )
                break


    # Project tracking
    if "project" in text:

        set_context(
            "last_project",
            message
        )


    # Website tracking
    if "http" in text or "www" in text:

        set_context(
            "last_website",
            message
        )


    # Command tracking
    set_context(
        "last_command",
        message
    )
