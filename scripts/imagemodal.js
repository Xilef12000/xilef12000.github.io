//https://www.w3schools.com/howto/howto_css_modal_images.asp
const modal = document.getElementById("myModal");
const modalImg = document.getElementById("img01");
const captionText = document.getElementById("caption");
document.querySelectorAll(".modal-image").forEach(element => {
    element.addEventListener('click', function() {
        window.location.hash = this.id;
        modal.style.display = "block";
        modalImg.src = this.src;
        captionText.innerHTML = this.alt;
    });
});
const span = document.getElementsByClassName("close")[0];
span.onclick = function() {
    modal.style.display = "none";
}
document.addEventListener("keydown", (event) => {
    const keys = ['Escape', 'Space', 'Enter', 'Backspace', 'Delete', 'Home', 'End', 'KeyX', 'NumpadMultiply', 'PageUp', 'PageDown', 'ArrowUp', 'ArrowDown'];
    if (keys.includes(event.code)) {
        modal.style.display = "none";
    }
});