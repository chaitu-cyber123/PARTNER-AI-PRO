import json
from ai.memory import save_memory, load_memory


def clean_memory():

    memory = load_memory()


    # Remove duplicate facts

    if "facts" in memory:

        remove_keys = []

        for key in memory["facts"]:

            if key.startswith("that what"):

                remove_keys.append(key)


        for key in remove_keys:

            del memory["facts"][key]



    # Move duplicate colour fact

    if "facts" in memory:

        if "my favourite colour" in memory["facts"]:

            value = memory["facts"].pop(
                "my favourite colour"
            )

            memory.setdefault(
                "preferences",
                {}
            )

            memory["preferences"][
                "favorite color"
            ] = value



    save_memory(memory)

    return "Memory cleaned."
