var number = 1
function pp() {
	number = number - 1
	if (number == 0){
		number = 1;
	}
	GO()
}
function np() {
	number = number + 1
	GO()
}
function GO() {
	var url = document.getElementById('bbb-url').value;
	var spliturl = url.split("/");
	var newurl
	for (i = 0; i < spliturl.length - 1; i++) {
		newurl += spliturl[i] + "/";
	}
	newurl = newurl.slice(9, newurl.length);
	var iframe = "<iframe src=\"" + newurl + number + "\" height=\"1080\" width=\"1920\"></iframe>"
	document.getElementById("frame").innerHTML = iframe;
	document.getElementById("framenr").innerHTML = "<p>Seite: " + number + "</p>";
}