//https://codepen.io/desandro/pen/LmWoWe
//https://3dtransforms.desandro.com/card-flip

document.querySelectorAll(".card__image").forEach(function(element) {
    element.addEventListener('load', function() {
        console.log("loaded");
        element.parentNode.parentNode.classList.add('is-flipped'); //for gallery
        element.parentNode.parentNode.parentNode.classList.add('is-flipped'); //for projects
    });
    element.addEventListener('click', function() {
        console.log("clicked");
    });
});