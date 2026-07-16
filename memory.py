import json
import os

FILE = "data/memory.json"

def load_memory():
    if not os.path.exists(FILE):
        return {}

    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_memory(memory):
    os.makedirs("data", exist_ok=True)

    with open(FILE, "w") as f:
        json.dump(memory, f, indent=4)

def remember(key, value):
    memory = load_memory()
    memory[key] = value
    save_memory(memory)

def recall(key):
    memory = load_memory()
    return memory.get(key, None)

def forget(key):
    memory = load_memory()

    if key in memory:
        del memory[key]
        save_memory(memory)
