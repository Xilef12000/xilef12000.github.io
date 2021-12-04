function onload404() {
	document.getElementById("Url").innerHTML = "Requested Url: " + window.location.href;
	document.getElementById("Time").innerHTML = "Time of Request: " + Date();
	onload();
}