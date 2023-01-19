//https://codepen.io/Hyperplexed/full/MWXBRBp
//https://www.youtube.com/watch?v=PkADl0HubMY
//https://camillemormal.com/

const track = document.getElementById("image-track");

const handleOnDown = e => track.dataset.mouseDownAt = e.clientX;

const handleOnUp = () => {
  track.dataset.mouseDownAt = "0";  
  track.dataset.prevPercentage = track.dataset.percentage;
}

const handleOnMove = e => {
  if(track.dataset.mouseDownAt === "0") return;
  
  const mouseDelta = parseFloat(track.dataset.mouseDownAt) - e.clientX,
  maxDelta = window.innerWidth / 2;
  
  const percentage = (mouseDelta / maxDelta) * -75,
  nextPercentageUnconstrained = parseFloat(track.dataset.prevPercentage) + percentage,
  nextPercentage = Math.max(Math.min(nextPercentageUnconstrained, 0), -75);
  
  track.dataset.percentage = nextPercentage;
  
  track.animate({
    transform: `translate(${nextPercentage}%, -0%)`
  }, { duration: 1200, fill: "forwards" });
  
  for(const image of track.getElementsByClassName("image")) {
    image.animate({
      objectPosition: `${Math.max(62.5 + nextPercentage/1.5, 12.5)}% center`
    }, { duration: 1200, fill: "forwards" });
  }
}

/* -- Had to add extra lines for touch events -- */

window.onmousedown = e => handleOnDown(e);

window.ontouchstart = e => handleOnDown(e.touches[0]);

window.onmouseup = e => handleOnUp(e);

window.ontouchend = e => handleOnUp(e.touches[0]);

window.onmousemove = e => handleOnMove(e);

window.ontouchmove = e => handleOnMove(e.touches[0]);