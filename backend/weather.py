import os
import requests
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


def get_weather(city):
    if not WEATHER_API_KEY:
        return {"error": "Missing WEATHER_API_KEY in .env"}

    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": WEATHER_API_KEY,
        "q": city
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code != 200:
            return {
                "error": data.get("error", {}).get("message", "Could not fetch weather data")
            }

        return {
            "city": data["location"]["name"],
            "region": data["location"]["region"],
            "country": data["location"]["country"],
            "temperature_f": data["current"]["temp_f"],
            "condition": data["current"]["condition"]["text"]
        }

    except Exception as e:
        return {"error": str(e)}