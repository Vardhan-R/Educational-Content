import math, pygame, random, time
import import_vectors as vect

pygame.init()

width = 800
height = 600
black = (0, 0, 0)
dark_grey = (64, 64, 64)
grey = (128, 128, 128)
light_grey = (191, 191, 191)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
dark_green = (0, 128, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
violet = (255, 0, 255)
orange = (255, 128, 0)
running = True
g = 100
damping = 0
cor = 1
radius = 10
all_particles = []

scrn = pygame.display.set_mode((width, height))

class Particle:
    def __init__(self, m, p, v, clr):
        self.m = m
        self.pos = vect.Vector(p[0], p[1])
        self.vel = vect.Vector(v[0], v[1])
        self.acc = vect.Vector(0, 0)
        self.clr = clr

    def show(self):
        pygame.draw.circle(scrn, self.clr, (self.pos.x, self.pos.y), radius)

def update():
    global all_particles

    for m in range(len(all_particles)):
        for n in range(m, len(all_particles)):
            if m != n:
                r = vect.sub(all_particles[n].pos, all_particles[m].pos)
                try:
                    f = r.setMag(g * all_particles[m].m * all_particles[n].m / r.magSq())
                    all_particles[m].acc = vect.add(all_particles[m].acc, f.mult(1 / all_particles[m].m))
                    all_particles[n].acc = vect.add(all_particles[n].acc, f.mult(-1 / all_particles[n].m))
                except:
                    pass

    for m in all_particles:
        m.vel = vect.add(m.vel, m.acc).mult(1 - damping)
        m.pos = vect.add(m.pos, m.vel)
        m.acc = vect.Vector(0, 0)

def collision():
    global all_particles

    for i in range(len(all_particles)):
        for j in range(i, len(all_particles)):
            if i != j:
                a = all_particles[i]
                b = all_particles[j]
                if (vect.sub(b.pos, a.pos).mag() <= 2 * radius):
                    m1 = a.m
                    m2 = b.m
                    dist = vect.sub(b.pos, a.pos)
                    parallelCompA = dist.setMag(vect.dot(dist.normalise(), a.vel))
                    perpCompA = vect.sub(a.vel, parallelCompA)
                    parallelCompB = dist.setMag(vect.dot(dist.normalise(), b.vel))
                    perpCompB = vect.sub(b.vel, parallelCompB)
                    v1 = vect.add(parallelCompA.mult(m1 - cor * m2), parallelCompB.mult(m2 * (cor + 1))).mult(1 / (m1 + m2))
                    v2 = vect.add(parallelCompB.mult(m2 - cor * m1), parallelCompA.mult(m1 * (cor + 1))).mult(1 / (m1 + m2))
                    all_particles[i].vel = vect.add(perpCompA, v1)
                    all_particles[j].vel = vect.add(perpCompB, v2)

m_1 = 1
m_2 = 0.001
m_3 = 0.000001
r = 200
w = math.sqrt(g * m_1 / r ** 3)
x = r * (m_2 / (3 * m_1)) ** (1 / 3)

all_particles.append(Particle(m_1, (400, 300), (0, 0), red))
all_particles.append(Particle(m_2, (400 + r, 300), (0, w * r), green))
all_particles.append(Particle(m_3, (400 + r - x, 300), (0, w * (r - x)), blue))

while running:
    scrn.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # collision()
    update()
    # com = vect.Vector(0, 0)
    # for i in all_particles:
    #     com = vect.add(com, i.pos.mult(i.m))
    # print(com.x, com.y)

    for i in all_particles:
        i.show()

    pygame.display.update()

pygame.quit()