import argparse
from constants.api_constants import SERVER_ENDPOINT
from helper import _send_request, check_status, _render_content, _get_farming_predictions


def parse_options():
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('-c', '--city-name', type=str, required=False, help="Name of the city")
    my_parser.add_argument('-n', '--number-of-days', type=str, required=False, help="Get the forecast details for the next `N` days. Specify the value of `N` here")
    my_parser.add_argument('-G', '--get-farming-predictions', action='store_true')
    my_parser.add_argument('-t', '--interval', action='store_true')

    return my_parser.parse_args()


def get_coordinates(city_name):
    url = f"{SERVER_ENDPOINT}/city/coordinates/{city_name}"
    status_code, response = _send_request(url, method="GET")

    if not check_status(status_code):
        raise ValueError(f"Request failed: {response}")

    return response


def get_forecast(lat, lon, number_of_days, interval):
    url = f"{SERVER_ENDPOINT}/city/forecast/{lat}/{lon}/{number_of_days}/{interval}"
    status_code, response = _send_request(url, method="GET")

    if not check_status(status_code):
        raise ValueError(f"Request failed: {response}")

    return response


def main():
    args = parse_options()
    coordinates = get_coordinates(args.city_name)

    if not coordinates:
        raise ValueError("Couldn't fetch the coordinates of the city")

    if not args.number_of_days:
        number_of_days = 1
        interval = 1
    else:
        number_of_days = int(args.number_of_days)
        interval = 8

    if not args.get_farming_predictions:
        weather_forecast = get_forecast(coordinates['lat'], coordinates['lon'], number_of_days, interval)
    else:
        weather_forecast = None

    if not args.get_farming_predictions:
        _render_content(weather_forecast, number_of_days)
    else:
        _get_farming_predictions(weather_forecast, args.city_name)


if __name__ == '__main__':
    main()

