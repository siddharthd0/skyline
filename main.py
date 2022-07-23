from flask import Flask, render_template
import requests
import geocoder

app = Flask(__name__)

@app.route('/')
def index():
    url = "https://asos2.p.rapidapi.com/v2/auto-complete"
    
    querystring = {"q":"bikini top","store":"US","country":"US","currency":"USD","sizeSchema":"US","lang":"en-US"}
    
    headers = {
    	"X-RapidAPI-Key": "1c74124f6amshe4f133aae307c96p148d3djsn206071992808",
    	"X-RapidAPI-Host": "asos2.p.rapidapi.com"
    }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    
    print(response.text)
    return render_template('index.html')

@app.route('/home')
def home():
  return render_template('index.html')        
@app.route('/men')
def men():
  return render_template('men.html')

@app.route('/selection')
def selection():
  return render_template('gender-selector.html')

@app.route('/woman')
def women():
  return render_template('woman.html')

@app.route('/about')
def about():
  return render_template('about.html')
  
@app.route('/contact')
def contact():
  return render_template('contact.html')
  
@app.route('/other')
def other():
  return render_template('other.html')
  
app.run(host='0.0.0.0', port=81, debug=True)