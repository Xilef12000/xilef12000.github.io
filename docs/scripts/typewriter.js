//http://jragon.herokuapp.com/
//https://jragon.pages.dev/

var i = 0;
var n = 0;
var txt = 'XILEF12000';
var last = 0;
var current = 0;
const speed = 100;
var cursor = true;
const speed_divisor = 4;
const text = ["XILEF12000", "ANIMATOR", "RENDERER", "PROGRAMMER", "DEVELOPER", "ARTIST", ""]


setInterval(typeWriter, speed);

function typeWriter() {
    if (i < txt.length && n == 20) {
        document.getElementById('cursor').style.opacity = 1;
        document.getElementById("typing").innerHTML += txt.charAt(i);
        i++;
    }
    else if ( n == 40){
        document.getElementById('cursor').style.opacity = 1;
        document.getElementById("typing").innerHTML = document.getElementById("typing").innerHTML.slice(0, -1);
        i--
        if (i <= 0) {
            n = 0;
            current = Math.floor(Math.random()* text.length)
            while (current == last){
                current = Math.floor(Math.random()* text.length)
            }
            txt = text[current];
            last = current;
        }
    }
    else {
        if (n % speed_divisor == 0 && cursor == true) {
            document.getElementById('cursor').style.opacity = 0;
            cursor = false;
        }
        else if (n % speed_divisor == 0 && cursor == false){
            document.getElementById('cursor').style.opacity = 1;
            cursor = true;
        }
        n++
    }
}