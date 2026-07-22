import requests
from config import NEWS_API_KEY
from services.summarizer import summarize_news

def get_news(category="general"):

    queries = {
        "tech": "technology AI gadgets startups",
        "sports": "sports cricket football",
        "world": "world international news",
        "india": "India news",
        "general": "latest news"
    }

    query = queries.get(category, queries["general"])

    url = "https://newsapi.org/v2/everything"

    params = {
        "q": query,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 5,
        "apiKey": NEWS_API_KEY
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if data.get("status") != "ok":
            return "Sorry sir, I couldn't fetch news right now."

        articles = data.get("articles", [])

        if not articles:
            return "Sorry sir, no news found."

        news = f"Here are the latest {category} headlines, sir:\n"

        for i, article in enumerate(articles[:5], 1):
            news += f"{i}. {article.get('title')}\n"

        return summarize_news(news)

    except Exception as e:
        return f"News error: {e}"
