from flask import Flask
import configparser
import logging

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('weather.ini')
bing_api_key = config.get('DEFAULT', 'BING_API_KEY', fallback=None)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
fh = logging.FileHandler('weatherstation.log')
fh.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s;%(module)s;%(funcName)s;%(levelname)s;%(message)s")
ch.setFormatter(formatter)
fh.setFormatter(formatter)
logger.propagate = False
logger.addHandler(ch)
logger.addHandler(fh)

from weatherforecast import views