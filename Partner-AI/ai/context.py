import json
import os

CONTEXT_FILE = "data/context.json"


def load_context():

    if not os.path.exists(CONTEXT_FILE):
        return []

    with open(CONTEXT_FILE,"r") as f:
        return json.load(f)



def save_context(context):

    with open(CONTEXT_FILE,"w") as f:
        json.dump(
            context,
            f,
            indent=4
        )



def add_context(role, message):

    context = load_context()

    context.append({
        "role": role,
        "message": message
    })


    # Keep last 20 messages only
    context = context[-20:]


    save_context(context)



def get_context():

    return load_context()
