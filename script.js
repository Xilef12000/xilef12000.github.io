function onload() {
	if(!(window.matchMedia('(prefers-color-scheme: dark)').matches)){
		document.body.classList.toggle("toggle-darklight");
		document.getElementById("icon").href = "../assets/favicon.svg"
	}
}
function toggledarklight() {
	document.body.classList.toggle("toggle-darklight");
}
function overlay_off() {
	document.getElementById("overlay").style.display = "none";
}