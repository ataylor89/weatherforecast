from flask import request, render_template, jsonify
from weatherforecast import app, weather

@app.route('/', methods=['GET'])
def home():
    return render_template('weather.html')

@app.route('/forecast', methods=['POST'])
def forecast():
    city = request.form['city']
    if city:
        latitude, longitude = weather.geocode(city)
    else:
        latitude = request.form['latitude']
        longitude = request.form['longitude']
    forecast = weather.get_forecast(latitude, longitude)
    return jsonify(forecast)