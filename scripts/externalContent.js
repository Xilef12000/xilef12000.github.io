function loadExternal(element){
    element.parentNode.outerHTML = element.parentNode.getAttribute("external");
}
function loadExternalAll(){
    document.querySelectorAll(".external_content").forEach(function(element) {
        element.outerHTML = element.getAttribute("external");
    });
}