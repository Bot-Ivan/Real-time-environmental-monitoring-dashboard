#this file will be used to get the API keys from the JSON files one folder up
import json
APIKeysFolder = "..\\API keys\\"


def getOpenWeatherMapAPIKey():
    location = APIKeysFolder + "OpenWeatherMapAPIKey.json"
    with open(location, 'r') as file:
        data = json.load(file)
    return data["key"]

def getWorldwideAirQualityAPIKey():
    location = APIKeysFolder + "WorldwideAirQualityAPIKey.json"
    with open(location, 'r') as file:
        data = json.load(file)
    return data["key"]


# print(getOpenWeatherMapAPIKey())
# print(getWorldwideAirQualityAPIKey())