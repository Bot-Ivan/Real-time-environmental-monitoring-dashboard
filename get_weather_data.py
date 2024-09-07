#This file will be used for getting the weather data from OpenWeatherMap and Worldwide Air Quality
import get_api_keys
import json
import requests

def fetch_weather_data(api_key, city, state):
    pass

def fetch_air_quality_data(api_key, city):
    pass

def get_opw_direct_geocoding_data(api_key, city, state):
    #OpenWeatherMap Direct geocoding
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state}&appid={api_key}"
    response = requests.get(url)

    #data should be a list of dictionaries, as seen here: https://openweathermap.org/api/geocoding-api#direct_name_how
    data = response.json()
    #200 - Success, and 404 - Not found
    if response.status_code == 200:
        return data

        # with open(f'..\\LocationInfo\\{city + state}_direct_geocoding_data.json', 'w', encoding='utf-8') as f:
        #     f.write(str(data))
        # with open(f'..\\LocationInfo\\{city + state}_direct_geocoding_data.json', 'r' ) as f:
        #     data = json.load(f)
        #     return data

weather_data_api_key = get_api_keys.getOpenWeatherMapAPIKey()
air_quality_data_api_key = get_api_keys.getWorldwideAirQualityAPIKey()

#region Testing
city = "Miami"
state = "Florida"

Miami_Florida_Data = get_opw_direct_geocoding_data(weather_data_api_key, city, state)
#endregion





