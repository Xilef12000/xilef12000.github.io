function GO_en() {
	var bbburl = document.getElementById('bbb-url').value;
	var spliturl = bbburl.split("=");
	var token = spliturl[1]
	var spliturl = bbburl.split("/");
	var url
	for (i = 0; i < 3; i++) {
		url += spliturl[i] + "/";
	}
	url = url.slice(9, url.length);
	var padid = document.getElementById('notizen-id').value;
	var name = document.getElementById('name').value;
	splitname = name.split(" ");
	name = ""
	for (i = 0; i < splitname.length; i++) {
		name += splitname[i] + "%20";
	}
	name = name.slice(0, name.length - 3);
	var iframe = "<p>This tool has been disabled due to the risk of misuse and identity theft!</p>"
	document.getElementById("frame").innerHTML = iframe;
}