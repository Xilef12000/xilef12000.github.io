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
	var iframe = "<iframe src=\"" + newurl + number + "\" width=100% id=\"iframe\"></iframe>"
	document.getElementById("frame").innerHTML = iframe;
	document.getElementById("framenr").innerHTML = "<p>Page: " + number + "</p>";
	var element = document.getElementById("iframe");
    element.style.height = element.contentWindow.document.body.scrollWidth*0.5625 + 'px';
}