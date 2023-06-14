from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__)
api_key = 'ee7e9698cc898d0021e975781ad4cc4c'

@app.route('/find-weather', methods=["post"])
def weather():
    global api_key
    global browser
    city_name = request.form['city_name']
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=imperial')
    data = response.json()
    if city_name != data:
        print('No weather data. Try again!')

    return render_template('index.html', data=data)

@app.route('/')
def index():

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')