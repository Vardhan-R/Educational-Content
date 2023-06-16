from manim import *
import pygame, sys

sys.path.insert(0, "C:/Users/vrdhn/Desktop/CS/GitHub/Python-Modules")

import import_vectors as vect

pygame.init()

width = 600
height = 600
running = True
dt = 10 ** (-3)

class Particle:
    def __init__(self, pos: vect.Vector, vel: vect.Vector):
        self.pos = pos
        self.vel = vel
        self.acc = vect.Vector(0, 0)

    def show(self):
        pygame.draw.circle(scrn, RED, (self.pos.x, self.pos.y), 5)

    def update(self):
        self.acc = vect.Vector(2 * ((self.pos.y - height / 2) / 50) ** 3, 3 * ((self.pos.x - width / 2) / 50) ** 2)
        self.vel = vect.add(self.vel, self.acc.mult(dt))
        self.pos = vect.add(self.pos, self.vel.mult(dt))

scrn = pygame.display.set_mode((width, height))

a = Particle(vect.Vector(width / 2, height / 2 + 100), vect.Vector(0, 0))

while running:
    scrn.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(20):
        pygame.draw.circle(scrn, GREEN, (width / 2, height / 2), i * width / 40, 1)

    a.update()
    a.show()

    pygame.display.update()

pygame.quit()