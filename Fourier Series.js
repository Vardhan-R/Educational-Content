let v = []
let f = []
let m = []
let d = []
let p = []
let px = []
let off

function setup() {
  createCanvas(600, 500);
  fourier(0, width / 4, PI)
  for (let i = 0; i < 100; i++) {
    fourier(2 * i + 1, 200 / (2 * i + 1), (-1) ** i * PI / 2)
  }

  off = 1

  for (let i = 0; i < f.length; i++) {
    v[i] = createVector(m[i] * cos(d[i]), m[i] * sin(d[i]))
  }
  noFill()
}

function draw() {
  background(220);
  translate(width / 2, height / 2)
  scale(1, -1)
  stroke(0)

  tempi = createVector()
  temp = createVector()

  arrow(0, 0, v[0].x, v[0].y)
  temp.add(v[0])
  for (let i = 0; i < v.length - 1; i++) {
    tempi.add(v[i])
    temp.add(v[i + 1])
    arrow(tempi.x, tempi.y, temp.x, temp.y)
  }
  px[px.length] = 0
  p[p.length] = temp.y

  stroke(255, 0, 0)
  beginShape()
  for (let i = 0; i < p.length; i++) {
    vertex(px[i], p[i])
    px[i] += off
  }
  endShape()

  for (let i = 0; i < v.length; i++) {
    v[i].rotate(f[i] * PI / 100)
  }
}

function fourier(freq, mag, dir) {
  f[f.length] = freq
  m[m.length] = mag
  d[d.length] = dir
}

function arrow(x1, y1, x2, y2) {
  push()
  fill(0)
  translate(x1, y1)
  line(0, 0, x2 - x1, y2 - y1)
  let dirOfArrow
  dirOfArrow = createVector(x2 - x1, y2 - y1)
  translate(x2 - x1, y2 - y1)
  rotate(dirOfArrow.heading())
  triangle(0, 0, -8, 4, -8, -4)
  pop()
}
