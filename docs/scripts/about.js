document.getElementById("currentYear").innerHTML = new Date().getFullYear();
if (document.cookie){
    document.getElementById("currentCookies").innerHTML = "Current Cookies: " + document.cookie;
}
else {
    document.getElementById("currentCookies").innerHTML = "no Cookies found";
}
function deleteAllCookies(){
    document.cookie.split(";").forEach(function(c) { document.cookie = c.replace(/^ +/, "").replace(/=.*/, "=;expires=" + new Date().toUTCString() + ";path=/"); });
    if (document.cookie){
        document.getElementById("currentCookies").innerHTML = "Current Cookies: " + document.cookie;
    }
    else {
        document.getElementById("currentCookies").innerHTML = "deleted all Cookies";
    }
}