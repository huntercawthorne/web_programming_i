/*
 * @name Animation
 * @description The circle moves.
 */
let x, y;
let x2, y2;
let x3, y3;
let x4, y4;
let x5, y5;
let x6, y6;
let x7, y7;
let x8, y8;
let x9, y9;
let randomColor, randomColor2;
let interval = 6.7;

function setup() {
  createCanvas(400, 400);
  // Starts in the middle
  x = width / 2;
  y = height / 2;
  x2 = x;
  y2 = y;
  x3 = x;
  y3 = y;
  x4 = x;
  y4 = y;
  x5 = x;
  y5 = y;
  x6 = x;
  y6 = y;
  x7 = x;
  y7 = y;
  x8 = x;
  y8 = y;
  x9 = x;
  y9 = x;
}

function draw() {
  //background(200);

  //Selects random colors
  randomColor = color(random(0,255), random(0,255), random(0,255));
  randomColor2 = color(random(0,255), random(0,255), random(0,255));

  //Changes the background color every few seconds
  if (frameCount % (interval *30) == 0) {
    background(randomColor2);
  }

  //Changes circle colors every few seconds
  if (frameCount % (interval * 30) == 0) {
    stroke(randomColor);
    fill(randomColor, 175);
  }


  //To add the jiggle effect
  x = x + random(-1, 1);
  x2 = x2 + random(-1, 1);
  x3 = x3 + random(-1, 1);
  x4 = x4 + random(-1, 1);
  x5 = x5 + random(-1, 1);
  x6 = x6 + random(-1, 1);
  x7 = x7 + random(-1, 1);
  x8 = x8 + random(-1, 1);

  y = y + random(-1, 1);
  y2 = y2 + random(-1, 1);
  y3 = y3 + random(-1, 1);
  y4 = y4 + random(-1, 1);
  y5 = y5 + random(-1, 1);
  y6 = y6 + random(-1, 1);
  y7 = y7 + random(-1, 1);
  y8 = y8 + random(-1, 1);



  //Creates circles
  ellipse(x, y, 24, 24);
  ellipse(x2, y2, 24, 24);
  ellipse(x3, y3, 24, 24);
  ellipse(x4, y4, 24, 24);
  ellipse(x5, y5, 24, 24);
  ellipse(x6, y6, 24, 24);
  ellipse(x7, y7, 24, 24);
  ellipse(x8, y8, 24, 24);
  ellipse(x9, y9, 24, 24);

  // Moves circles at constant speeds
  y = y - 1;
  x2 = x2 - 1;
  x3 = x3 - 1;
  y3 = y3 - 1;
  x4 = x4 + 1;
  y4 = y4 - 1;
  x5 = x5 + 1;
  x6 = x6 + 1;
  y6 = y6 + 1;
  x7 = x7 - 1;
  y7 = y7 + 1;
  y8 = y8 + 1;

  //Resets positions to opposite where they were
  if (y < 0) {
    y = height;
  }

  if (x2 < 0) {
    x2 = width;
  }

  if (x3 < 0 && y3 < 0) {
    x3 = width;
    y3 = height;
  }

  if (x4 > width && y4 < 0) {
    x4 = 0;
    y4 = height;
  }

  if (x5 > width) {
    x5 = 0;
  }

  if (x6 > width && y6 > height) {
    x6 = 0;
    y6 = 0;
  }

  if (x7 < 0 && y7 > height) {
    x7 = width;
    y7 = 0;
  }

  if (y8 > height) {
    y8 = 0;
  }
}