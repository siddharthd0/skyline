window.onload = function getLocation() {
if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  }
}
function fetch2(url){
  fetch(url).then(function(response) {
    return response.json();
  }).then(function(data) {
    console.log(data);
    console.log(data["properties"]["periods"]);
    let arr = data["properties"]["periods"]
    console.log(arr[0].detailedForecast)
    for (let i = 0; i < arr.length; i++) {
      const node = document.createElement("li");
      const textnode = document.createTextNode(arr[i].name + ': '+arr[i].detailedForecast);
      var regex = /\d+/g;
      var string = arr[i].detailedForecast;
      var matches = string.match(regex);  // creates array from matches
      // console.log(matches);
      let num = parseInt(matches[0])
      console.log(num)
      node.appendChild(textnode);
      document.getElementById("myList").appendChild(node);
    }
  }).catch(function() {
    console.log("Booo");
  });
}
function showPosition(position) {
  let x = document.getElementById('location');
  x.innerHTML = position.coords.latitude + ', '+position.coords.longitude;
  let y = position.coords.latitude
  let z = position.coords.longitude
  const dict_values = {y, z} //Pass the javascript variables to a dictionary.
  const s = JSON.stringify(dict_values); // Stringify converts a JavaScript object or value to a JSON string
  console.log(s); // Prints the variables to console window, which are in the JSON format
  fetch('https://api.weather.gov/points/'+y+','+z).then(function(response) {
    return response.json();
  }).then(function(data) {
    console.log(data["properties"]["forecast"]);
    fetch2(data["properties"]["forecast"])
  }).catch(function() {
    console.log("Booo");
  });
}