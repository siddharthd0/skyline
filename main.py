from flask import Flask, render_template
import requests
import geocoder

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get(' https://api.weather.gov/alerts/active?area=KS')
    data = response.json()
    g = geocoder.ip('me')
    print(g.latlng)
    return render_template('index.html', data=data, coords=g.latlng)
        
app.run(host='0.0.0.0', port=81, debug=True)

@app.route('/men')
def men():
  return render_template('men.html')

@app.route('/selection')
def men():
  return render_template('gender-selector.html')

@app.route('/women')
def women():
  return render_template('women.html')