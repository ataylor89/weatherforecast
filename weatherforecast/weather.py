from weatherforecast import bing_api_key
import requests
import geocoder

def get_forecast(latitude, longitude):
    url1 = f"https://api.weather.gov/points/{latitude},{longitude}"
    resp1 = requests.get(url1)
    url2 = resp1.json()['properties']['forecast']
    resp2 = requests.get(url2)
    data = resp2.json()['properties']
    forecast = format_json(data)
    return forecast

def format_json(data):
    forecast = {}
    forecast['elevation'] = f'{0} m'.format(data['elevation']['value'])
    forecast['generatedAt'] = data['generatedAt']
    forecast['units'] = data['units']
    forecast['periods'] = []
    for s in data['periods']:
        d = {}
        d['name'] = s['name']
        d['temperature'] = str(s['temperature']) + ' ' + s['temperatureUnit']
        d['relativeHumidity'] = str(s['relativeHumidity']['value']) + '%'
        if s['probabilityOfPrecipitation']['value'] is None:
            d['probabilityOfPrecipitation'] = 'N/A'
        else:
            d['probabilityOfPrecipitation'] = str(s['probabilityOfPrecipitation']['value']) + '%'
        if s['dewpoint']['unitCode'] == 'wmoUnit:degC':
            d['dewpoint'] = str(int(celsius_to_fahrenheit(s['dewpoint']['value']))) + ' F'
        d['windDirection'] = s['windDirection']
        d['windSpeed'] = s['windSpeed']
        d['shortForecast'] = s['shortForecast']
        d['detailedForecast'] = s['detailedForecast']
        d['icon'] = s['icon']
        forecast['periods'].append(d)
    return forecast

def geocode(city):
    g = geocoder.bing(city, key=bing_api_key)
    return g.latlng

def rev_geocode(latitude, longitude):
    g = geocoder.bing([latitude, longitude], method='reverse', key=bing_api_key)
    return g.json['city']

def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32