//get tags.db
array = httpGet("/tags.db").split(";\n");
tags = [];
for (element of array) {
    tags.push(element.split(", "));
}
console.table(tags);
//get id.db
array = httpGet("/id.db").split(";\n");
ids = [];
for (element of array) {
    ids.push(element.split(", "));
}
console.table(ids);


function search(event) {
    var key = event.key;
    if (key == "Enter") {
        document.getElementById('results').innerHTML = ""
        var found = false;
        var search_input = document.getElementById('search_bar').value;
        var used = []
        for (word of search_input.split(" ")) {
            for (var i = 0; i < tags.length; i++) {
                if (tags[i][1].toLowerCase() === word.toLowerCase()) {
                    var tag = tags[i][0]
                    if (!used.includes(tag)){
                        for (id of ids) {
                            if (tag == id[0]) {
                                console.log(id[2])
                                if (id[1] == 'PROJECTS'){
                                    document.getElementById('results').innerHTML += '<p><a href="/project/' + tag +'/">' + id[2] + '</a></p>';
                                }
                                else if (id[1] == 'ART'){
                                    document.getElementById('results').innerHTML += '<p><a href="/gallery? ' + id[2] +'">' + id[2] + '</a></p>';
                                }
                                else {
                                    document.getElementById('results').innerHTML += '<p>' + id[2] + '</p>';
                                }
                            }
                        }
                    }
                    used.push(tag)
                    found = true;
                }
            }
        }
        if (!found) {
            console.log("No Result found")
            document.getElementById('results').innerHTML = "<p>No Result found</p>";
        }
    }
}


function httpGet(theUrl) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}