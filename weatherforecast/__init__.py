from flask import Flask
import configparser

app = Flask(__name__)
config = configparser.ConfigParser()
config.read('weather.ini')
bing_api_key = config.get('DEFAULT', 'BING_API_KEY', fallback=None)

from weatherforecast import views