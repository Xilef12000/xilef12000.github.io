
var i = 0;
var n = 0;
var txt = 'XILEF12000';
const speed = 100;
var cursor = true;
const speed_divisor = 4;
const teyt = []


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