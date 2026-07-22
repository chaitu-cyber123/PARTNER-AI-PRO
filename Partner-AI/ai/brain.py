import requests
from config import API_KEY, MODEL, BASE_URL, SYSTEM_PROMPT
from ai.memory import (
    remember,
    recall,
    forget,
    load_context,
    add_context
)
def ask(prompt):
    text = prompt.lower().strip()

    # Remember name
    if "my name is" in text:
        name = prompt.lower().split("my name is", 1)[1].strip().title()
        remember("name", name)
        return f"Nice to meet you, {name}. I'll remember your name."

    # Recall name
    if "what is my name" in text or "what's my name" in text:
        name = recall("name")
        if name:
            return f"Your name is {name}."
        return "I don't know your name yet."
    # Remember facts
    if text.startswith("remember "):
        fact = prompt[9:].strip()

        if " is " in fact:
            key, value = fact.split(" is ", 1)
            remember(key.strip().lower(), value.strip())
            return f"I'll remember that {key.strip()} is {value.strip()}."

    # Recall facts
    if text.startswith("what is my "):
        key = text.replace("what is my ", "").replace("?", "").strip()
        value = recall(key)

        if value:
            return f"Your {key} is {value}."

        return f"I don't know your {key} yet."

    # Forget facts
    if text.startswith("forget my "):
        key = text.replace("forget my ", "").strip()
        forget(key)
        return f"I forgot your {key}."
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://partner-ai.local",
        "X-Title": "Partner AI"
    }

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    messages.extend(load_context())

    messages.append({
        "role": "user",
        "content": prompt
    })

    add_context("user", prompt)


    payload = {
        "model": MODEL,
        "messages": messages
    }

    try:
        response = requests.post(
            BASE_URL,
            headers=headers,
            json=payload,
            timeout=60
        )

        response.raise_for_status()

        data = response.json()

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Error: {e}"
