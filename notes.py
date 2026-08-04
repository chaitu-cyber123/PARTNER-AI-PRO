import json
import os

FILE = "data/notes.json"


def load_notes():
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r") as f:
        return json.load(f)


def save_notes(notes):
    os.makedirs("data", exist_ok=True)

    with open(FILE, "w") as f:
        json.dump(notes, f, indent=4)


def add_note(note):
    notes = load_notes()
    notes.append(note)
    save_notes(notes)

    return "Note saved."


def show_notes():
    notes = load_notes()

    if not notes:
        return "You have no notes."

    return "Your notes are: " + ", ".join(notes)
