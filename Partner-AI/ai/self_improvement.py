import json
import os

LOG_FILE = "data/improvements.json"


def load_logs():
    if not os.path.exists(LOG_FILE):
        return []

    with open(LOG_FILE, "r") as f:
        return json.load(f)


def save_logs(logs):
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)


def learn_from_feedback(user_input, response, feedback):

    logs = load_logs()

    logs.append({
        "user": user_input,
        "response": response,
        "feedback": feedback
    })

    save_logs(logs)
