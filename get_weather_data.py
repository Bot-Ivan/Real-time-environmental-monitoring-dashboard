#This file will be used for getting the weather data from OpenWeatherMap 
import get_api_keys
import requests
from location import *
import json
def fetch_weather_data(api_key, coordinates):
    #example api call https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
    print(coordinates["lat"])
    print(coordinates["lon"])
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={coordinates['lat']}&lon={coordinates['lon']}&units=imperial&appid={api_key}"
    print(url)
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        return data
    else:
        print("The status code was not 200, fix this")
        print(response.status_code)


def get_location_coordinates(api_key, city, state):
    #OpenWeatherMap Direct geocoding
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state}&appid={api_key}"
    response = requests.get(url)
    #data should be a list of dictionaries, as seen here: https://openweathermap.org/api/geocoding-api#direct_name_how
    data = response.json()
    #200 - Success, and 404 - Not found
    if response.status_code == 200:

        #we only need the coordinates from this api call, we'll get the important data from the One Call API 3.0 in the fetch_weather_data function
        location_coordinates = {}
        location_coordinates["lat"] = data[0]["lat"]
        location_coordinates["lon"] = data[0]["lon"]
        return location_coordinates
    
    else:
        print("The status code was not 200, fix this")

weather_data_api_key = get_api_keys.getOpenWeatherMapAPIKey()
air_quality_data_api_key = get_api_keys.getWorldwideAirQualityAPIKey()

#region Testing
location_coordinates = get_location_coordinates(weather_data_api_key, "Miami", "Florida")
Miami_data = fetch_weather_data(weather_data_api_key,location_coordinates)

print(json.dumps(Miami_data, indent = 4))


#endregion
