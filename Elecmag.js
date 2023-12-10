let gravConst, k, mu_naught, damping, p, B
let allParticles = []
let allUHS = []
let allUSS = []

function setup() {
  createCanvas(650, 500);

  gravConst = 1
  k = 1000
  mu_naught = 1000
  damping = 0
  B = createVector(0, 0, -0.1)
  p = 1

  allParticles.push(new Particle(1, 1, 0, 255, 0, 300, 250, 1, 0))
  // allParticles.push(new Particle(1, 2, 255, 0, 0, 100, 250, 0, 0))
  // allParticles.push(new Particle(1, 2, 0, 0, 255, 500, 250, 0, 0))
}

function draw() {
  background(0);
  showMagField()
  translate(width / 2, height / 2)
  scale(1, -1)
  translate(-width / 2, -height / 2)

  for (let i = 0; i < allParticles.length; i++) {
    if (p == 1) {
      allParticles[i].update()
      allParticles[i].magField()
    }
  }
  for (let i = 0; i < allParticles.length; i++) {
    if (p == 1) {
      allParticles[i].updatePos()
    }
    allParticles[i].show()
  }
}



class Particle {
  constructor(m, q, r, g, b, px, py, vx, vy) {
    this.mass = m
    this.charge = q
    this.clr = [r, g, b]
    this.pos = createVector(px, py)
    this.vel = createVector(vx, vy)
    this.acc = createVector()
  }

  update() {
    let tempAcc = createVector()
    let tempAccUHS = createVector()
    for (let n = 0; n < allParticles.length; n++) {
      if (this.pos != allParticles[n].pos) {
        let acc = k * this.charge * allParticles[n].charge / ((dist(this.pos.x, this.pos.y, allParticles[n].pos.x, allParticles[n].pos.y)) ** 3) / this.mass
        let dir = createVector(this.pos.x - allParticles[n].pos.x, this.pos.y - allParticles[n].pos.y)
        dir.mult(acc)
        tempAcc.add(dir)
      }
    }
    this.acc = tempAcc



//     for (let n = 0; n < allUHS.length; j++) {
//       if (dist(this.pos.x, this.pos.y, allUHS[n].px, allUHS[n].py) > allUHS[n].diameter / 2) {
//         acc = k * this.charge * allUHS[n].q / ((dist(this.pos.x, this.pos.y, allUHS[n].px, allUHS[n].py)) ** 3) / this.mass
//         dir = createVector(this.pos.x - allUHS[n].px, this.pos.y - allUHS[n].py)
//         dir.mult(acc)
//         tempAcc.add(dir)
//         dir.mult(this.mass / allUHS[n].m)
//         tempAccUHS.add(dir)
//         // still have not done acc, vel and mvmnt for UHS
//       }
//     }



//     // haven't done USS variable name correction
//     for (let j = 0; j < allUSS.length; j++) {
//       if (dist(allPos[i].x, allPos[i].y, allUSS[j].p.x, allUSS[j].p.y) > allUSS[j].diameter / 2) {
//         acc = k * allCharges[i] * allUSS[j].q / ((dist(allPos[i].x, allPos[i].y, allUSS[j].p.x, allUSS[j].p.y)) ** 3) / allMasses[i]
//         dir = createVector(allPos[i].x - allUSS[j].p.x, allPos[i].y - allUSS[j].p.y)
//         dir.mult(acc)
//         tempAcc.add(dir)
//       } else {
//         acc = 8 * k * allCharges[i] * allUSS[j].q / (allUSS[j].diameter ** 3) / allMasses[i]
//         dir = createVector(allPos[i].x - allUSS[j].p.x, allPos[i].y - allUSS[j].p.y)
//         dir.mult(acc)
//         tempAcc.add(dir)
//       }
//     }



    this.vel.add(tempAcc)
  }



  magField() {
    let accB = this.charge * B.z / this.mass // multiplying with vel in the next and next to next lines
    let dir_force_B = this.vel.copy()
    dir_force_B.rotate(-PI / 2)
    dir_force_B.mult(accB)
    this.vel.add(dir_force_B)
  }



  updatePos() {
    this.pos.add(this.vel)
  }



  show() {
    stroke(255)
    fill(this.clr[0], this.clr[1], this.clr[2])
    circle(this.pos.x, this.pos.y, 20)
  }
}

// function update() {
//   // vel and acc update for all the particles
//   for (let i = 0; i < allParticles.length; i++) {
//   }

//   // pos update for all particles
//   for (let i = 0; i < allMasses.length; i++) {
//     allPos[i].add(allVel[i])
//   }
// }



function damp() {
  for (let n = 0; i < allParticles.length; i++) {
    allParticles[i].vel.mult(1 - damping)
  }
}



class UHS {
  constructor(m, q, diameter, r, g, b, px, py, vx, vy) {
    this.m = m
    this.q = q
    this.diameter = diameter
    this.r = r
    this.g = g
    this.b = b
    this.px = px
    this.py = py
    this.vx = vx
    this.vy = vy
  }
  
  UHS_show() {
    push()
    noFill()
    stroke(this.r, this.g, this.b)
    circle(this.px, this.py, this.diameter)
    pop()
  }
}



class USS {
  constructor(m, q, diameter, r, g, b, a, px, py, vx, vy) {
    this.m = m
    this.q = q
    this.diameter = diameter
    this.r = r
    this.g = g
    this.b = b
    this.a = a
    this.p = createVector(px, py)
  }
  
  USS_show() {
    push()
    fill(this.r, this.g, this.b ,this.a)
    circle(this.p.x, this.p.y, this.diameter)
    pop()
  }
}



function showMagField() {
  noStroke()
  fill(0, 0, 255)
  if (B.z < 0) {
    for (let i = 0; i < 10; i++) {
      for (let j = 0; j < 10; j++) {
        text("x", width / 20 * (2 * i + 1), height / 20 * (2 * j + 1))
      }
    }
  }
  else if (B.z > 0) {
    for (let i = 0; i < 10; i++) {
      for (let j = 0; j < 10; j++) {
        text(".", width / 20 * (2 * i + 1), height / 20 * (2 * j + 1))
      }
    }
  }
}



function keyPressed() {
  if (keyCode === 32) {
    p *= -1
  }
}

// acc = F / m = q (v x B) / m = qvB / m
