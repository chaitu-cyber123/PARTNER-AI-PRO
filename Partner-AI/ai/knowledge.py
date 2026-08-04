import json
import os
import re

KNOWLEDGE_DIR = "knowledge"


IGNORE_WORDS = {
    "what",
    "is",
    "the",
    "a",
    "an",
    "my",
    "your",
    "tell",
    "me",
    "about",
    "explain",
    "please",
    "give",
    "information",
    "information",
    "define"
}


def normalize(text):

    text = text.lower()

    text = re.sub(
        r"[^a-z0-9 ]",
        "",
        text
    )

    return text.strip()



def extract_keywords(text):

    words = normalize(text).split()

    return set(
        word for word in words
        if word not in IGNORE_WORDS
    )



def search_knowledge(question):

    keywords = extract_keywords(question)

    if not keywords:
        return None


    if not os.path.exists(KNOWLEDGE_DIR):
        return None


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

            with open(path,"r") as f:

                data = json.load(f)


            for item in data:

                stored_keywords = set(
    item.get(
        "keywords",
        extract_keywords(item["question"])
    )
)

                match = len(
                    keywords & stored_keywords
                )


                if match == 0:
                    continue


                score = match / max(
                    len(keywords),
                    len(stored_keywords)
                )


                if score > best_score:

                    best_score = score

                    best_answer = item["answer"]


        except Exception:

            pass



    if best_score >= 0.4:

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



    # Prevent duplicates

    for item in data:

        if normalize(item["question"]) == normalize(question):

            return



    data.append({

        "question": question,

        "answer": answer,

        "category": "general",

        "keywords": list(
            extract_keywords(question)
        ),

        "confidence": 1,

        "times_used": 0

    })

    with open(file, "w") as f:

        json.dump(
            data,
            f,
            indent=4
        )
