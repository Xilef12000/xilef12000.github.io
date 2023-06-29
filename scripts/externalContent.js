function loadExternal(element){
    element.parentNode.outerHTML = element.parentNode.getAttribute("external");
}
function loadExternalAll(){
    document.cookie = "loadExternal=true; path=/";
    document.querySelectorAll(".external_content").forEach(function(element) {
        element.outerHTML = element.getAttribute("external");
    });
}
window.onload = (event) => {
    if (document.cookie.match(new RegExp('(^| )' + "loadExternal" + '=([^;]+)'))[2] == "true"){
        loadExternalAll();
    }
};