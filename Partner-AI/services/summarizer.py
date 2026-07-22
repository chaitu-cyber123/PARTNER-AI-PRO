from ai.brain import ask


def summarize_news(headlines):
    prompt = f"""
Summarize these news headlines in a simple way.
Give a short 3-4 line explanation.

Headlines:
{headlines}
"""

    try:
        return ask(prompt)

    except Exception:
        return headlines
