currentURL = window.location.href;
var parts = currentURL.split("gallery?%20");
if (parts.length > 1) {
    image = decodeURI(parts[parts.length -1]);
    console.log(image);
    document.addEventListener('DOMContentLoaded', (event) => {
        //the event occurred
        document.getElementById(image).focus()
        console.log(document.getElementById(image).outerHTML)
        console.log("focus");
    })
}