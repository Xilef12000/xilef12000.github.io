//https://codepen.io/desandro/pen/LmWoWe
//https://3dtransforms.desandro.com/card-flip

document.querySelectorAll(".card__image").forEach(function(element) {
    element.addEventListener('load', function() {
        element.parentNode.parentNode.classList.add('is-flipped'); //for gallery
        element.parentNode.parentNode.parentNode.classList.add('is-flipped'); //for projects
    });
});
document.querySelectorAll(".card__image__instant").forEach(function(element) {
        element.parentNode.parentNode.classList.add('is-flipped'); //for gallery
        element.parentNode.parentNode.parentNode.classList.add('is-flipped'); //for projects
});

function loadExternal(element){
    element.parentNode.outerHTML = element.parentNode.getAttribute("external")
}
function loadExternalAll(){
    document.querySelectorAll(".external_content").forEach(function(element) {
        element.outerHTML = element.getAttribute("external")
    });
}