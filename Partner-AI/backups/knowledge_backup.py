import json
import os


KNOWLEDGE_DIR = "knowledge"


def normalize(text):
    return (
        text.lower()
        .replace("?", "")
        .strip()
    )


def search_knowledge(question):

    question = normalize(question)

    if not os.path.exists(KNOWLEDGE_DIR):
        return None

    words = set(question.split())

    best_score = 0
    best_answer = None


    for filename in os.listdir(KNOWLEDGE_DIR):

        if not filename.endswith(".json"):
            continue

        path = os.path.join(
            KNOWLEDGE_DIR,
            filename
        )

        try:

            with open(path, "r") as f:
                data = json.load(f)


            for item in data:

                stored = normalize(
                    item["question"]
                )

                stored_words = set(
                    stored.split()
                )


                # Remove common words
                ignore = {
                    "what",
                    "is",
                    "the",
                    "a",
                    "an",
                    "my",
                    "your",
                    "tell",
                    "me",
                    "about"
                }


                clean_question = words - ignore
                clean_stored = stored_words - ignore


                if not clean_question:
                    continue


                match = len(
                    clean_question &
                    clean_stored
                )


                score = match / len(clean_question)


                if score > best_score:
                    best_score = score
                    best_answer = item["answer"]


        except Exception:
            pass


    # Only accept strong matches
    if best_score >= 0.6:
        return best_answer


    return None

def save_knowledge(question, answer):

    os.makedirs(
        KNOWLEDGE_DIR,
        exist_ok=True
    )


    file = os.path.join(
        KNOWLEDGE_DIR,
        "custom.json"
    )


    data = []


    if os.path.exists(file):

        with open(file,"r") as f:
            data = json.load(f)


    data.append({
        "question": question,
        "answer": answer
    })


    with open(file,"w") as f:
        json.dump(
            data,
            f,
            indent=4
        )
