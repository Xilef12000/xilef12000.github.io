//https://codepen.io/Hyperplexed/full/MWXBRBp
//https://www.youtube.com/watch?v=PkADl0HubMY
//https://camillemormal.com/

const track1 = document.getElementById("image-track1");
const track2 = document.getElementById("image-track2");

const handleOnDown1 = e => track1.dataset.mouseDownAt = e.clientX;
const handleOnDown2 = e => track2.dataset.mouseDownAt = e.clientX;

const handleOnUp1 = () => {
  track1.dataset.mouseDownAt = "0";  
  track1.dataset.prevPercentage = track1.dataset.percentage;
}
const handleOnUp2 = () => {
  track2.dataset.mouseDownAt = "0";  
  track2.dataset.prevPercentage = track2.dataset.percentage;
}

const handleOnMove1 = e => {
  if(track1.dataset.mouseDownAt === "0") return;
  
  const mouseDelta1 = parseFloat(track1.dataset.mouseDownAt) - e.clientX,
  maxDelta = window.innerWidth / 2;
  
  const percentage1 = (mouseDelta1 / maxDelta) * -75,
  nextPercentageUnconstrained = parseFloat(track1.dataset.prevPercentage) + percentage1,
  nextPercentage = Math.max(Math.min(nextPercentageUnconstrained, 0), -75);
  
  track1.dataset.percentage = nextPercentage;
  
  track1.animate({
    transform: `translate(${nextPercentage}%, -0%)`
  }, { duration: 1200, fill: "forwards" });
  
  for(const image of track1.getElementsByClassName("image")) {
    image.animate({
      objectPosition: `${Math.max(62.5 + nextPercentage/1.5, 12.5)}% center`
    }, { duration: 1200, fill: "forwards" });
  }
}

const handleOnMove2 = e => {
  if(track2.dataset.mouseDownAt === "0") return;
  
  const mouseDelta2 = parseFloat(track2.dataset.mouseDownAt) - e.clientX,
  maxDelta = window.innerWidth / 2;
  
  const percentage2 = (mouseDelta2 / maxDelta) * -75,
  nextPercentageUnconstrained = parseFloat(track2.dataset.prevPercentage) + percentage2,
  nextPercentage = Math.max(Math.min(nextPercentageUnconstrained, 0), -75);
  
  track2.dataset.percentage = nextPercentage;
  
  track2.animate({
    transform: `translate(${nextPercentage}%, -0%)`
  }, { duration: 1200, fill: "forwards" });
  
  for(const image of track2.getElementsByClassName("image")) {
    image.animate({
      objectPosition: `${Math.max(62.5 + nextPercentage/1.5, 12.5)}% center`
    }, { duration: 1200, fill: "forwards" });
  }
}

/* -- Had to add extra lines for touch events -- */

window.onmousedown = e => {
  handleOnDown1(e);
  handleOnDown2(e);
}
window.ontouchstart = e => {
  handleOnDown1(e.touches[0]);
  handleOnDown2(e.touches[0]);
}
window.onmouseup = e => {
  handleOnUp1(e);
  handleOnUp2(e);
}
window.ontouchend = e => {
  handleOnUp1(e.touches[0]);
  handleOnUp2(e.touches[0]);
}
window.onmousemove = e => {
  handleOnMove1(e);
  handleOnMove2(e);
}
window.ontouchmove = e => {
  handleOnMove1(e.touches[0]);
  handleOnMove2(e.touches[0]);
}