import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
MEMORY_FILE = os.path.join(DATA_DIR, "memory.json")

os.makedirs(DATA_DIR, exist_ok=True)

if not os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "w") as f:
        json.dump({}, f)


def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except:
        return {}


def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)

def remember(key, value):

    memory = load_memory()

    key = key.lower().strip()

    # Profile information
    profile_words = [
        "name",
        "age",
        "location",
        "city",
        "country"
    ]

    # Preference information
    preference_words = [
        "favorite",
        "prefer",
        "like",
        "love"
    ]

    if any(word in key for word in profile_words):

        if "profile" not in memory:
            memory["profile"] = {}

        memory["profile"][key] = value


    elif any(word in key for word in preference_words):

        if "preferences" not in memory:
            memory["preferences"] = {}

        memory["preferences"][key] = value


    else:

        if "facts" not in memory:
            memory["facts"] = {}

        memory["facts"][key] = value


    save_memory(memory)

def recall(key):
    memory = load_memory()

    if key in memory:
        return memory[key]

    if "profile" in memory and key in memory["profile"]:
        return memory["profile"][key]

    if "preferences" in memory and key in memory["preferences"]:
        return memory["preferences"][key]

    if "facts" in memory and key in memory["facts"]:
        return memory["facts"][key]

    return None

def forget(key):
    memory = load_memory()
    if key in memory:
        del memory[key]
        save_memory(memory)


def clear_memory():
    save_memory({})
def get_profile():
    memory = load_memory()
    return memory.get("profile", {})


def update_profile(key, value):
    memory = load_memory()

    if "profile" not in memory:
        memory["profile"] = {}

    memory["profile"][key] = value
    save_memory(memory)


def get_profile_value(key):
    profile = get_profile()
    return profile.get(key)

def smart_recall(query):

    query = query.lower().strip()

    memory = load_memory()

    sections = {
        "profile": memory.get("profile", {}),
        "preferences": memory.get("preferences", {}),
        "facts": memory.get("facts", {})
    }


    ignore = {
        "what",
        "is",
        "my",
        "do",
        "i",
        "know",
        "tell",
        "me",
        "remember",
        "the",
        "a",
        "about",
        "which",
        "what's",
        "are"
    }


    query_words = set(
        query.replace("?", "").split()
    ) - ignore


    best_value = None
    best_score = 0


    for category, items in sections.items():

        for key, value in items.items():

            key_words = set(
                key.lower().split()
            )


            # Direct keyword match

            score = len(
                query_words & key_words
            )


            # Semantic shortcuts

            if (
                "food" in query_words
                and "favorite" in key_words
            ):
                score += 2


            if (
                "like" in query_words
                and "favorite" in key_words
            ):
                score += 2


            if (
                "name" in query_words
                and key == "name"
            ):
                score += 3


            if score > best_score:

                best_score = score
                best_value = value


    if best_score > 0:
        return best_value


    return None
def load_context():
    context_file = os.path.join(DATA_DIR, "context.json")

    try:
        with open(context_file, "r") as f:
            return json.load(f)
    except:
        return []


def save_context(context):
    context_file = os.path.join(DATA_DIR, "context.json")

    with open(context_file, "w") as f:
        json.dump(context, f, indent=4)


def add_context(role, content):
    context = load_context()

    context.append({
        "role": role,
        "content": content
    })

    # Keep last 10 messages only
    context = context[-10:]

    save_context(context)
