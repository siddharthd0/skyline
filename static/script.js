window.onload = function getLocation() {
if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  }
}

function showPosition(position) {
  let x = document.getElementById('location');
  x.innerHTML = position.coords.latitude + ', '+position.coords.longitude;
  console.log(position.coords.latitude)
  console.log(position.coords.longitude);
  const dict_values = {position.coords.latitude, position.coords.longitude} //Pass the javascript variables to a dictionary.
  const s = JSON.stringify(dict_values); // Stringify converts a JavaScript object or value to a JSON string
  console.log(s); // Prints the variables to console window, which are in the JSON format
  window.alert(s)
  $.ajax({
    url:"/men",
    type:"POST",
    contentType: "application/json",
    data: JSON.stringify(s)});
}