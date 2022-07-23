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

app.route('/home')
def home():
  return render_template('index.html')
  
  
        
@app.route('/men')
def men():
  return render_template('men.html')

@app.route('/selection')
def selection():
  return render_template('gender-selector.html')

@app.route('/women')
def women():
  return render_template('woman.html')

@app.route('/about')
def about():
  return render_template('about.html')
  
@app.route('/contact')
def contact():
  return render_template('contact.html')


app.run(host='0.0.0.0', port=81, debug=True)