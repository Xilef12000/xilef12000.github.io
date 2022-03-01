function onload() {
	if(!(window.matchMedia('(prefers-color-scheme: dark)').matches)){
		document.body.classList.toggle("toggle-darklight");
		document.getElementById("icon").href = "../assets/favicon.svg"
	}
	else{
		document.getElementById("icon").href = "../assets/favicon_dark.svg"
	}
}
function toggledarklight() {
	document.body.classList.toggle("toggle-darklight");
	if (document.body.classList.contains("toggle-darklight")){
		document.getElementById("icon").href = "../assets/favicon.svg"
	}
	else{
		document.getElementById("icon").href = "../assets/favicon_dark.svg"
	}
}
function overlay_off() {
	document.getElementById("overlay").style.display = "none";
}