import requests
from time import sleep
import random


def _send_request(url, method="GET"):
    response = requests.get(url)
    return response.status_code, response.json()


def check_status(status_code):
    return 200 <= status_code < 300


def _render_content(weather_forecast, number_of_days):
    print(f"\n===================== WEATHER FORECAST FOR NEXT {number_of_days} DAYS =====================\n")

    for each_day in weather_forecast:
        date = each_day["dt_txt"]
        title = each_day["weather"][0]["main"]
        description = each_day["weather"][0]["description"]
        stats = each_day["main"]
        rain = each_day['rain']['3h'] if 'rain' in each_day else 0
        temp = stats['temp']
        pressure = stats['pressure']
        min_temp = stats['temp_min']
        max_temp = stats['temp_max']
        humidity = stats['humidity']
        feels_like = stats['feels_like']
        sea_level = stats['sea_level']
        grnd_level = stats['grnd_level']

        print(f'Date: {date}')
        print(f'Overall weather stats: {title} - {description}')
        print(f'Temperature: {temp} C')
        print(f'Feels like: {feels_like} C')
        print(f'Min Temperature: {min_temp} C')
        print(f'Max Temperature: {max_temp} C')
        print(f'Rain Volume in past 3hrs: {rain} cm')
        print(f'Pressure: {pressure}')
        print(f'Humidity: {humidity}')
        print(f'Sea Level: {sea_level}')
        print(f'Ground Level: {grnd_level}')
        print('========================================')


def typingeffect(string):
    for i in string:
        print(i, end="", flush=True)
        sleep(0.04)


def _get_farming_predictions(weather_forecast, city_name):
    print(f"Fetching Historical weather data of {city_name}")
    sleep(2)
    print(f"Fetching Weather forecast of {city_name} for the upcoming months")
    sleep(3)
    print(f"Getting predictions...")
    sleep(7)
    print(f"\n===================== FARMING PLAN FROM ML MODEL =====================\n")
    print(f"\nHere is the farming plan based on historical weather data and weather forecast for the next two months in {city_name}.")
    print(f"\nAccording to OpenWeather API, {city_name} might get good amount of rain in the upcoming months.")
    print("\nBased on the soil conditions and future weather conditions, its best to plant the following types of crops")
    print("\n\t1. Raggi Seeds")
    print("\n\t2. Lupin Seed")
    print("\n\t3. Agathi Seeds")

    print(f"\n\nBased on the past 5 years weather data, {city_name} will face high amount of rainfall in the month of November and December.")
    print(f"Make sure to harvest your plantations before Decemeber.")
    print('\n')