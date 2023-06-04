let gravConst, m1, m2

function setup() {
  createCanvas(400, 400);
  gravConst = 10
  m1 = 1
  m2 = 1
  p1 = createVector(100, 200)
  p2 = createVector(300, 200)
  v1 = createVector(0, -1)
  v2 = createVector(0, 1)
}

function draw() {
  background(0);
  if (dist(p1.x, p1.y, p2.x, p2.y) != 0) {
    a1 = createVector(p2.x - p1.x, p2.y - p1.y)
    a1.setMag(2 * gravConst * m2 / dist(p1.x, p1.y, p2.x, p2.y))
    a2 = createVector(p1.x - p2.x, p1.y - p2.y)
    a2.setMag(2 * gravConst * m1 / dist(p1.x, p1.y, p2.x, p2.y))
  }
  v1.add(a1)
  v2.add(a2)
  p1.add(v1)
  p2.add(v2)
  stroke(255)
  fill(255, 0, 0)
  circle(p1.x, p1.y, 20)
  fill(0, 0, 255)
  circle(p2.x, p2.y, 20)
  // v1.mult(0.999)
  // v2.mult(0.999)
}
