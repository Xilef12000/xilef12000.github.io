function onloadabout() {
	onload();
	document.getElementById("currentYearEN").innerHTML = new Date().getFullYear();
	document.getElementById("currentYearDE").innerHTML = new Date().getFullYear();
}