import argparse
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from constants.api_constants import SERVER_ENDPOINT
from helper import _send_request, check_status, parse_content


def parse_options():
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('-c', '--city-name', type=str, required=True, help="Name of the city")
    my_parser.add_argument('-d', '--number-of-days', type=str, required=True, help="Get the forecast details for the next `N` days. Specify the value of `N` here")
    my_parser.add_argument('-p', '--ph', type=str, required=False, help="Soil pH")
    my_parser.add_argument('-K', '--potassium-level', type=str, required=False, help="Potassium Content")
    my_parser.add_argument('-g', '--get-crop-predictions', action='store_true')
    return my_parser.parse_args()


def get_coordinates(city_name):
    url = f"{SERVER_ENDPOINT}/city/coordinates/{city_name}"
    status_code, response = _send_request(url, method="GET")

    if not check_status(status_code):
        raise ValueError(f"Request failed: {response}")

    return response


def get_forecast(lat, lon, number_of_days):
    url = f"{SERVER_ENDPOINT}/city/forecast/{lat}/{lon}/{number_of_days}"
    status_code, response = _send_request(url, method="GET")

    if not check_status(status_code):
        raise ValueError(f"Request failed: {response}")

    return response


def main():
    console = Console()
    args = parse_options()
    coordinates = get_coordinates(args.city_name)

    if not coordinates:
        raise ValueError("Couldn't fetch the coordinates of the city")

    weather_forecast = get_forecast(coordinates['lat'], coordinates['lon'], args.number_of_days)
    user_renderables = [Panel(parse_content(each_day), expand=True) for each_day in weather_forecast]
    console.print(Columns(user_renderables))

    if args.get_crop_predictions:
        print("\n Suitable Crops Prediction")
        print("1. Paddy")
        print("2. Wheat")
        print('\n')


if __name__ == '__main__':
    main()

