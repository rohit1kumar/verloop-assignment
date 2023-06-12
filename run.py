import os
import requests
from flask import Flask, request, jsonify, Response
from xml.etree.ElementTree import Element, SubElement, tostring

app = Flask(__name__)

def fetch_data_by_city(city, output_format):
    headers = {
        'X-RapidAPI-Key': os.getenv('APIKEY'),
        'X-RapidAPI-Host': 'weatherapi-com.p.rapidapi.com'
    }
    query_params = {
        'q': city
    }
    API_URL = 'https://weatherapi-com.p.rapidapi.com/current.json'
    response = requests.get(API_URL, headers=headers, params=query_params)
    response.raise_for_status() # Raise exception if invalid response
    data = response.json()
    data = {
        'Weather': f"{data['current']['temp_c']}C",
        'Latitude': data['location']['lat'],
        'Longitude': data['location']['lon'],
        'City': f"{data['location']['name']} {data['location']['country']}"
    }

    if output_format == 'xml':
        return json_to_xml(data)
    elif output_format == 'json':
        return jsonify(data)
    else:
        return jsonify({'error': 'Invalid output_format specified, only json and xml are supported'}), 400


def json_to_xml(data):
    root = Element('root')
    for key, value in data.items():
        element = SubElement(root, key)
        element.text = str(value)
    return Response(tostring(root), mimetype='application/xml')

@app.route('/getCurrentWeather', methods=['POST'])
def get_current_weather():
    request_data = request.get_json()
    city = request_data.get('city')
    output_format = request_data.get('output_format', 'json')

    if city:
        try:
            return fetch_data_by_city(city, output_format)
        except requests.exceptions.HTTPError as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'city is required'}), 400


if __name__ == '__main__':
    app.run()
