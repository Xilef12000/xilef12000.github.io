function redirect(page){
	if (navigator.language.includes("de")){
		window.location.replace("de/" + page);
	}
	else
		window.location.replace("en/" + page);
}
function redirectde(page){
	window.location.replace("../de/" + page);
}
function redirecten(page){
	window.location.replace("../en/" + page);
}