# -*- conding:utf-8 -*-
import requests
history = []

def fetchweather(location):
    url = "https://api.seniverse.com/v3/weather/now.json"

    params = {
        "key": "6kdw2auoyzhisehb",
        "location": location,
        "language": "zh-Hans",
        "unit": 'c'
        }

    result = requests.get(url, params, timeout=20).json()
    #print(result)
    city = result['results'][0]['location']['name']
    temperature = result['results'][0]['now']['temperature']
    weather_info = result['results'][0]['now']['text']
    time = result['results'][0]['last_update']
    time_ed = time[:10] + ' ' + time[11:19]

    return city, temperature, weather_info, time_ed
