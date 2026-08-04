import json
import os

CONTEXT_FILE = "data/context_engine.json"

DEFAULT = {
    "last_file": None,
    "last_folder": None,
    "last_note": None,
    "last_image": None,
    "last_project": None,
    "last_task": None,
    "last_command": None,
    "last_website": None
}


def load_context():

    if not os.path.exists(CONTEXT_FILE):

        save_context(DEFAULT)

        return DEFAULT.copy()

    with open(CONTEXT_FILE, "r") as f:

        return json.load(f)


def save_context(context):

    with open(CONTEXT_FILE, "w") as f:

        json.dump(context, f, indent=4)


def set_context(key, value):

    context = load_context()

    context[key] = value

    save_context(context)


def get_context(key):

    context = load_context()

    return context.get(key)


def clear_context():

    save_context(DEFAULT.copy())
