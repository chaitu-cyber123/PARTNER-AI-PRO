import requests
from config import WEATHER_API_KEY

def weather_command(message):
    text = message.lower().strip()

    if not text.startswith("weather in "):
        return None

    city = message[11:].strip()

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={WEATHER_API_KEY}&units=metric"
    )

    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        print(data)

        if data.get("cod") != 200:
            return f"API Error: {data}"

        temp = data["main"]["temp"]
        feels = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"].title()

        return (
            f"Weather in {city.title()}:\n"
            f"🌡 Temperature: {temp}°C\n"
            f"🤗 Feels like: {feels}°C\n"
            f"💧 Humidity: {humidity}%\n"
            f"☁ Condition: {description}"
        )

    except Exception as e:
        return f"Weather error: {e}"
