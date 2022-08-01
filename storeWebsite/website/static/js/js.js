

//makes menu appear when click on meu image
var ulAlign = document.getElementById("ulAlign");

function openMenu(){
    ulAlign.style.left = "0px";

};

function closeMenu(){
    ulAlign.style.left = "-200px";
};


// scrolling with mouse enabled

const storeItemBlock = document.querySelector('.scroll-item-block');

let mouseDown= false;
let StartX, scrollLeft;

let startDragging = function(e){
    mouseDown=true;
    startX = e.pageX - storeItemBlock.offsetLeft;
    scrollLeft = storeItemBlock.scrollLeft;
};

let stopDragging = function (event) {
    mouseDown = false;
};


storeItemBlock.addEventListener('mousemove', (e) => {
  e.preventDefault();
  if(!mouseDown) { return; }
  const x = e.pageX - storeItemBlock.offsetLeft;
  const scroll = x - startX;
  storeItemBlock.scrollLeft = scrollLeft - scroll;
});


recipeBlock.addEventListener('mousedown', startDragging, false);
recipeBlock.addEventListener('mouseup', stopDragging, false);
recipeBlock.addEventListener('mouseleave', stopDragging, false);

recipeBlock.addEventListener('mousemove', (e) => {
  e.preventDefault();
  if(!mouseDown) { return; }
  const x = e.pageX - recipeBlock.offsetLeft;
  const scroll = x - startX;
  recipeBlock.scrollLeft = scrollLeft - scroll;
});

storeItemBlock.addEventListener('mousedown', startDragging, false);
storeItemBlock.addEventListener('mouseup', stopDragging, false);
storeItemBlock.addEventListener('mouseleave', stopDragging, false);

