currentURL = window.location.href;
var parts = currentURL.split("gallery?%20");
if (parts.length > 1) {
    image = decodeURI(parts[parts.length -1]);
    console.log(image);
    document.addEventListener('DOMContentLoaded', (event) => {
        //page loaded
        document.getElementById(image).scrollIntoView()
        document.getElementById(image).focus()
    })
}