// https://usefulangle.com/post/113/javascript-detecting-irlE-visible-during-scroll
window.addEventListener('scroll', function() {
    check();
});
window.addEventListener('load', function() {
    check();
});
function check() {
    var irlE = document.querySelector('#irl');
    var irlP = irlE.getBoundingClientRect();
    var x12E = document.querySelector('#xilef12000');
    var x12P = x12E.getBoundingClientRect();
    if(irlP.top < window.innerHeight && irlP.bottom >= 0) {
        irl();
    }
    else if(x12P.top < window.innerHeight && x12P.bottom >= 0) {
        x12();
    }
}
var ppimg = document.getElementById("ppimg");
var pname = document.getElementById("pname");
function irl(){
    ppimg.src = "/assets/user.svg"
    pname.innerHTML = "Manuel König"
}
function x12(){
    ppimg.src = "/assets/art/4f35.png"
    pname.innerHTML = "Xilef12000"
}