from flask import Flask, jsonify, request
from constants import GEOCODING_API_ENDPOINT, FORECAST_API_ENDPOINT, API_KEY
from mock import DIRECT_GEOCODING, FORECAST
import requests


app = Flask(__name__)


@app.route('/city/coordinates/<city_name>', methods=['GET'])
def get_coordinates(city_name):
    url = f"{GEOCODING_API_ENDPOINT}?q={city_name}&appid={API_KEY}"
    # response = requests.get(url)
    # response = response.json()
    response = DIRECT_GEOCODING

    if not response:
        return jsonify({})

    return jsonify(response[0])


@app.route('/city/forecast/<lat>/<lon>/<number_of_days>', methods=['GET'])
def get_forecast(lat, lon, number_of_days):
    number_of_days = int(number_of_days)
    url = f"{FORECAST_API_ENDPOINT}?lat={lat}&lon={lon}&appid={API_KEY}"
    # response = requests.get(url)
    # response = response.json()
    response = FORECAST
    days_report = response['list']
    result = []
    days_report.insert(0, {})

    for index in range(len(days_report) + 1):
        if index and index % 8 == 0 or index == 1:
            result.append(days_report[index])

    result = result[1:number_of_days + 1]

    return result


if __name__ == "__main__":
    app.run(debug=True)
