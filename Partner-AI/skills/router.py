from skills.system import system_command
from skills.browser import browser_command
from skills.calculator import calculator_command
from skills.weather import weather_command
from services.news import get_news
from skills.briefing import briefing_command
from skills.profile import profile_command
from skills.memory import memory_command
from skills.status import status_command
from skills.tasks import task_command
from skills.reminders import reminder_command
def news_command(message):

    if "tech news" in message or "technology news" in message:
        return get_news("tech")

    if "sports news" in message or "sports update" in message:
        return get_news("sports")

    if "world news" in message or "international news" in message:
        return get_news("world")

    if "india news" in message or "indian news" in message:
        return get_news("india")

    if (
        "news" in message
        or "headlines" in message
        or "what's happening" in message
        or "what is happening" in message
        or "today's updates" in message
    ):
        return get_news()

    return None


def handle_command(message):
    message = message.lower().strip()

    for handler in (
        system_command,
        browser_command,
        calculator_command,
        weather_command,
        briefing_command,
        profile_command,
        news_command,
        memory_command,
        status_command,
        task_command,
        reminder_command,
    ):
        result = handler(message)

        if result is not None:
            return result

    return None
