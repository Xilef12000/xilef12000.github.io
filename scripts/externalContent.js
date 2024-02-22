function loadExternal(element){
    element.parentNode.outerHTML = element.parentNode.getAttribute("external");
}
function loadExternalAll(){
    document.cookie = "loadExternal=true; path=/";
    document.querySelectorAll(".toggle_href").forEach(function(element) {
        element = element.parentNode.parentNode.parentNode;
        setTimeout(() => {
            element.setAttribute("href", element.getAttribute("href_alt"));
        }, 0) // after delay of 0ms
    });
    document.querySelectorAll(".external_content").forEach(function(element) {
        element.outerHTML = element.getAttribute("external");
    });
}
window.onload = (event) => {
    if (document.cookie.match(new RegExp('(^| )' + "loadExternal" + '=([^;]+)'))[2] == "true"){
        loadExternalAll();
    }
};
function disable_href(element){
    element.parentNode.parentNode.parentNode.setAttribute("href", "javascript: void(0)");
    console.log("enable")
}
function enable_href(element){
    element.parentNode.parentNode.parentNode.setAttribute("href", element.parentNode.parentNode.parentNode.getAttribute("href_alt"));
    console.log("disable")
}