function setup() {
  createCanvas(400, 400);
  a = 1
  console.log(a)

  // this is a comment

  if (2 > 5) {
    console.log("2 is greater than 5")
  }
  if (2 < 5) {
    console.log("2 is less than 5")
  }

  if (2 > 5) {
    console.log("2 is greater than 5")
  } else {
    console.log("2 is not greater than 5")
  }

  a = 1
  b = 2
  c = 4
  d = 4

  if (c == 4) {
    console.log("c is equal to 4")
  }

  if (c == d) {
    console.log("a is equal to b")
  } else if (a == 1) {
    console.log("a is equal to 1")
  } else {
    console.log("None of the above conditions were satisfied.")
  }

  if (1 <= 1) {
    console.log("1 is less than or equal to 1")
  }

  if (2 <= 3) {
    console.log("2 is less than or equal to 3")
  }

  x = 7
  y = 8

  if (x != y) {
    console.log(x, "does not equal", y)
  }
}

function draw() {
  background(220);
  random()
}
