import requests
from config import API_KEY, MODEL

URL = "https://openrouter.ai/api/v1/chat/completions"


def ask(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://partner.local",
        "X-Title": "Partner AI"
    }

    payload = {
        "model": MODEL,
        "max_tokens": 1000,
        "messages": [
            {
                "role": "system",
                "content": """You are Partner, an advanced personal AI assistant.
Your name is Partner.
Address the user as sir.
Be intelligent, calm, professional, and helpful.
Keep answers clear and concise."""
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    try:
        response = requests.post(
            URL,
            headers=headers,
            json=payload,
            timeout=60
        )

        data = response.json()

        if "choices" not in data:
            return f"Partner AI error: {data}"

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Partner AI connection error: {e}"
