import requests


def _send_request(url, method="GET"):
    response = requests.get(url)
    return response.status_code, response.json()


def check_status(status_code):
    return 200 <= status_code < 300


def parse_content(each_day):
    date = each_day["dt_txt"]
    title = each_day["weather"][0]["main"]
    description = each_day["weather"][0]["description"]
    stats = each_day["main"]
    rain = each_day['rain']['3h'] if 'rain' in each_day else 0
    return f"[b]{date}[/b]\n[yellow]{title} - {description}\n\n[green]Temp: {stats['temp']} C \n[green]Min Temp: {stats['temp_min']} C \n[green]Max Temp: {stats['temp_max']} C \n[green]Humidity: {stats['temp_max']} C \n[green]Sea Level: {stats['temp_max']}\n[green]Ground Level: {stats['temp_max']}\n[green]Wind speed: {each_day['wind']['speed']} m/s\n[green]Visibility: {each_day['visibility']}\n[green]RainVolume in last 3 hrs: {rain}"
