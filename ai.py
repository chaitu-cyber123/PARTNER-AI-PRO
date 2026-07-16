import requests
from config import API_KEY, MODEL

URL = "https://openrouter.ai/api/v1/chat/completions"

def ask(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": "You are JARVIS, Tony Stark's intelligent AI assistant. Reply briefly, professionally and helpfully."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    try:
        response = requests.post(URL, headers=headers, json=data, timeout=30)

        if response.status_code != 200:
            return f"API Error {response.status_code}: {response.text}"

        result = response.json()
        return result["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Error: {e}"
