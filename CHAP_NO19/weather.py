import requests
from dotenv import load_dotenv
import os
from pprint import pprint
load_dotenv()

def get_curr_weather():
    city = input("/Please enter your city")
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}"
    weather_data = requests.get(request_url).json()
    print(f"\nCurrent weather data for {weather_data["name"]}")
    print(f"\nThe temp is {weather_data["main"]["temp"]}")
    print(f"\nFeels like {weather_data["main"]["feels_like"]} and {weather_data["weather"][0]["description"]}")




if __name__ == "__main__":
    get_curr_weather()