from urllib.parse import quote_plus

def browser_command(message):
    message = message.lower().strip()

    # Open websites
    websites = {
        "youtube": "https://youtube.com",
        "google": "https://google.com",
        "github": "https://github.com",
        "chatgpt": "https://chatgpt.com"
    }

    for name, url in websites.items():
        if message == f"open {name}":
            return {
                "reply": f"Opening {name}.",
                "action": "open_url",
                "url": url
            }

    # Google Search
    if message.startswith("search "):
        query = quote_plus(message.replace("search ", "", 1))
        return {
            "reply": f"Searching Google for '{message.replace('search ', '', 1)}'.",
            "action": "open_url",
            "url": f"https://www.google.com/search?q={query}"
        }

    # YouTube Search
    if message.startswith("search youtube for "):
        query = quote_plus(message.replace("search youtube for ", "", 1))
        return {
            "reply": "Searching YouTube.",
            "action": "open_url",
            "url": f"https://www.youtube.com/results?search_query={query}"
        }

    return None
