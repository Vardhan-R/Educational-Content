let gravConst, m1, m2

function setup() {
  createCanvas(400, 400);
  gravConst = 1
  m1 = 1
  m2 = 10000
  m3 = 1
  p1 = createVector(200, 100)
  p2 = createVector(200, 200)
  p3 = createVector(200, 250)
  v1 = createVector(sqrt(gravConst * m2 / (dist(p1.x, p1.y, p2.x, p2.y))), 0)
  v2 = createVector(0, 0)
  v3 = createVector(sqrt(gravConst * m2 / (dist(p2.x, p2.y, p3.x, p3.y))), 0)
}

function draw() {
  background(0);
  if (dist(p1.x, p1.y, p2.x, p2.y) != 0) {
    a12 = createVector(p2.x - p1.x, p2.y - p1.y)
    a12.setMag(gravConst * m2 / ((dist(p1.x, p1.y, p2.x, p2.y)) ** 2))
    a21 = createVector(p1.x - p2.x, p1.y - p2.y)
    a21.setMag(gravConst * m1 / ((dist(p1.x, p1.y, p2.x, p2.y)) ** 2))
  }
  if (dist(p1.x, p1.y, p3.x, p3.y) != 0) {
    a13 = createVector(p3.x - p1.x, p3.y - p1.y)
    a13.setMag(gravConst * m3 / ((dist(p1.x, p1.y, p3.x, p3.y)) ** 2))
    a31 = createVector(p1.x - p2.x, p1.y - p2.y)
    a31.setMag(gravConst * m1 / ((dist(p1.x, p1.y, p3.x, p3.y)) ** 2))
  }
  if (dist(p2.x, p2.y, p3.x, p3.y) != 0) {
    a23 = createVector(p3.x - p2.x, p3.y - p2.y)
    a23.setMag(gravConst * m3 / ((dist(p2.x, p2.y, p3.x, p3.y)) ** 2))
    a32 = createVector(p2.x - p3.x, p2.y - p3.y)
    a32.setMag(gravConst * m2 / ((dist(p2.x, p2.y, p3.x, p3.y)) ** 2))
  }
  v1.add(a12)
  v1.add(a13)
  v2.add(a21)
  v2.add(a23)
  v3.add(a31)
  v3.add(a32)
  p1.add(v1)
  p2.add(v2)
  p3.add(v3)
  stroke(255)
  fill(255, 0, 0)
  circle(p1.x, p1.y, 20)
  fill(0, 255, 0)
  circle(p2.x, p2.y, 20)
  fill(0, 0, 255)
  circle(p3.x, p3.y, 20)
  // v1.mult(0.99)
  // v2.mult(0.99)
  // v3.mult(0.99)
}
