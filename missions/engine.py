import json

FILE = "missions/storage.json"


def load():

    with open(FILE, "r") as f:
        return json.load(f)


def save(data):

    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


def create(title):

    data = load()

    mission = {

        "title": title,

        "status": "active",

        "tasks": [],

        "progress": 0

    }

    data["missions"].append(mission)

    save(data)


def add_task(title, task):

    data = load()

    for mission in data["missions"]:

        if mission["title"] == title:

            mission["tasks"].append({

                "task": task,

                "done": False

            })

    save(data)


def complete(title, task):

    data = load()

    for mission in data["missions"]:

        if mission["title"] == title:

            for t in mission["tasks"]:

                if t["task"] == task:

                    t["done"] = True

            total = len(mission["tasks"])

            finished = sum(
                1 for t in mission["tasks"]
                if t["done"]
            )

            if total:

                mission["progress"] = int(
                    finished / total * 100
                )

    save(data)


def list_missions():

    return load()["missions"]
