import requests
from config import API_KEY, MODEL

URL = "https://openrouter.ai/api/v1/chat/completions"

SYSTEM_PROMPT = """
You are Partner AI.

Your name is Partner.

You are calm, intelligent and professional.

Address the user as sir.

Keep replies short unless asked to explain.
"""

def ask(prompt):

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://partner-ai.local",
        "X-Title": "Partner AI"
    }

    payload = {
        "model": MODEL,
        "messages":[
            {
                "role":"system",
                "content":SYSTEM_PROMPT
            },
            {
                "role":"user",
                "content":prompt
            }
        ]
    }

    try:

        r = requests.post(
            URL,
            headers=headers,
            json=payload,
            timeout=60
        )

        data = r.json()

        return data["choices"][0]["message"]["content"]

    except Exception as e:

        return str(e)
