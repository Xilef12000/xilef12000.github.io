currentURL = window.location.href;
args = document.currentScript.getAttribute('args');
args = "?%20" + args;

if (currentURL.split('/').includes('project') && currentURL.split('/').slice(-1) != args){
    window.location.href = args;
}