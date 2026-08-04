from datetime import datetime
from services.news import get_news
from skills.weather import weather_command
from ai.memory import get_profile_value


def briefing_command(message):

    if "briefing" not in message and "good morning" not in message:
        return None

    name = get_profile_value("name")
    news_preference = get_profile_value("preferred_news")

    if name:
        greeting = f"Good morning {name}."
    else:
        greeting = "Good morning sir."

    now = datetime.now()

    response = f"""
{greeting}

Current time is {now.strftime('%I:%M %p')}.

Here are your updates:
"""

    try:
        weather = weather_command("weather")
        if weather:
            response += f"\nWeather:\n{weather}\n"
    except:
        pass

    try:
        response += "\nNews:\n"

        if news_preference:
            response += get_news(news_preference)
        else:
            response += get_news()

    except:
        response += "\nNews service unavailable."

    return response
