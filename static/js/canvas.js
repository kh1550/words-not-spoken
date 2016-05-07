var width, height;
var bg;

function setup() {
    width = window.innerWidth;
    height = window.innerHeight;
    createCanvas(width,height);
    bg = loadImage("static/img/classroom.png");
}

function draw() {
    image(bg,0,0,width,height);
}