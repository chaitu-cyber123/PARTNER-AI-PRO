import json
import os

STATE_FILE = "world/state.json"


DEFAULT_STATE = {

    "current_project": None,

    "current_goal": None,

    "current_task": None,

    "completed_tasks": [],

    "active_file": None,

    "conversation_topic": None,

    "mode": "normal"

}


def load():

    if not os.path.exists(STATE_FILE):

        save(DEFAULT_STATE)

    with open(STATE_FILE, "r") as f:

        return json.load(f)


def save(state):

    with open(STATE_FILE, "w") as f:

        json.dump(state, f, indent=4)


def update(key, value):

    state = load()

    state[key] = value

    save(state)


def get(key):

    state = load()

    return state.get(key)
