function onload() {
	if(!(window.matchMedia('(prefers-color-scheme: dark)').matches)){
		var element = document.body;
		element.classList.toggle("toggle-darklight");
	}
}
function toggledarklight() {
	var element = document.body;
	element.classList.toggle("toggle-darklight");
}
function overlay_off() {
	document.getElementById("overlay").style.display = "none";
}