from flask import Flask, render_template, request, json, redirect
import requests
import geocoder

app = Flask(__name__)
  
@app.route('/')
def index():
    # url = "https://asos2.p.rapidapi.com/v2/auto-complete"
    
    # querystring = {"q":"bikini top","store":"US","country":"US","currency":"USD","sizeSchema":"US","lang":"en-US"}
    
    # headers = {
    # 	"X-RapidAPI-Key": "1c74124f6amshe4f133aae307c96p148d3djsn206071992808",
    # 	"X-RapidAPI-Host": "asos2.p.rapidapi.com"
    # }
    
    # response = requests.request("GET", url, headers=headers, params=querystring)
    
    # print(response.text)
    return render_template('index.html')

@app.route('/home')
def home():
  return render_template('index.html')        
@app.route('/men', methods=['GET','POST'])
def men():
  # if request.method == 'POST':
  #   output = request.get_json()
  #   if output != None:
  #     print(output) 
  #     print(type(output))
  #     result = json.loads(output)
  #     print(result)
  #     latitude = result["y"]
  #     longitude = result["z"]
  #     url = "https://api.weather.gov/points/{},{}".format(latitude, longitude)
  #     data = requests.get(url)
  #     list = data.json()
  #     print(list["properties"]["forecast"])
  #     url = list["properties"]["forecast"]
  #     data = requests.get(url)
  #     list = data.json()
  #     results = list["properties"]["periods"]
  #     print(type(results))
  #     yes = True
  #     return render_template("men.html", results = results)
  #   else:
  #     return render_template("men.html", yes = False)
  # else:
  return render_template("men.html", yes = False)
@app.route('/test')
def test():
      latitude = 37.731815
      longitude = -121.943672
      url = "https://api.weather.gov/points/{},{}".format(latitude, longitude)
      data = requests.get(url)
      list = data.json()
      print(list["properties"]["forecast"])
      url = list["properties"]["forecast"]
      data = requests.get(url)
      list = data.json()
      result = list["properties"]["periods"]
      print(type(result))
      return render_template("test.html", result=list, length=len(result), yes = True)

@app.route('/selection')
def selection():
  return render_template('gender-selector.html')

@app.route('/woman', methods=['GET','POST'])
def women():
  if request.method == 'POST':
    output = request.get_json()
    if output != None:
      print(output) 
  return render_template('woman.html')

@app.route('/about')
def about():
  return render_template('about.html')
  
@app.route('/contact')
def contact():
  return render_template('contact.html')

@app.route('/test1')
def test1():
  return render_template('test1.html')
  
@app.route('/other')
def other():
 return render_template('other.html')

app.run(host='0.0.0.0', port=81, debug=True, use_reloader = True)