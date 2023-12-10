let xi, yi, t, a, b

function setup() {
  createCanvas(400, 400);
  background(0);
  stroke(255)
  xi = width / 2
  yi = height / 2
  t = 0
  a = 5
  b = 3
  frameRate(100)
}

function draw() {
  x = xi + 100 * cos(a * t)
  y = yi + 100 * sin(b * t)
  point(x, y)
  t = t + 0.01
}
