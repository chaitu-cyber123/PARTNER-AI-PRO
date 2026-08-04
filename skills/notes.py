import json
import os


NOTES_FILE = "data/notes.json"


def load_notes():

    if not os.path.exists(NOTES_FILE):
        return []

    with open(NOTES_FILE, "r") as f:
        return json.load(f)



def save_notes(notes):

    with open(NOTES_FILE, "w") as f:
        json.dump(
            notes,
            f,
            indent=4
        )



def notes_command(message):

    text = message.lower().strip()


    # Create note

    if (
        text.startswith("note ")
        or text.startswith("create note")
    ):

        if text.startswith("note "):
            note = message[5:].strip()

        else:
            note = message.replace(
                "create note",
                ""
            ).strip()


        notes = load_notes()

        notes.append(note)

        save_notes(notes)

        return "Note saved."



    # Show notes

    if (
        "show notes" in text
        or "show my notes" in text
        or "list notes" in text
        or "list my notes" in text
        or "what are my notes" in text
    ):

        notes = load_notes()


        if not notes:
            return "No notes saved."


        output = ""

        for i, note in enumerate(notes, 1):

            output += f"{i}. {note}\n"


        return output



    # Delete note

    if (
        text.startswith("delete note")
        or text.startswith("delete my note")
    ):

        try:

            number = int(
                text.replace(
                    "delete my note",
                    ""
                ).replace(
                    "delete note",
                    ""
                ).strip()
            )


            notes = load_notes()


            if number < 1 or number > len(notes):
                return "Invalid note number."


            deleted = notes.pop(
                number - 1
            )


            save_notes(notes)


            return f"Deleted note: {deleted}"


        except ValueError:

            return "Use: Delete note 1"



    return None
