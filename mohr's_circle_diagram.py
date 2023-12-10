from built_modules import import_vectors as vect
from manim import *
import pygame

pygame.init()

width = 800
height = 600
centre = vect.Vector(width / 2, height / 2)
running = True
font = pygame.font.Font("freesansbold.ttf", 24)

class Slider:
	def __init__(self, label: str, pos: vect.Vector, length: float | int, min_val: float | int, max_val: float | int):
		self.label = label
		self.pos = pos
		self.length = length
		self.min_val = min_val
		self.max_val = max_val
		self.val = (max_val + min_val) / 2
		self.font = pygame.font.Font("freesansbold.ttf", 12)

	def show(self, scrn: pygame.Surface):
		pygame.draw.line(scrn, (255, 255, 0), (self.pos.x, self.pos.y), (self.pos.x + self.length, self.pos.y), 2)
		pygame.draw.circle(scrn, (255, 0, 0), (self.pos.x + self.length * (self.val - self.min_val) / (self.max_val - self.min_val), self.pos.y), 3)
		scrn.blit(self.font.render(self.label, True, WHITE), (self.pos.x + self.length + 5, self.pos.y))
		scrn.blit(self.font.render(f"{self.val:.2f}", True, WHITE), (self.pos.x + self.length * (self.val - self.min_val) / (self.max_val - self.min_val) - 5, self.pos.y + 3))

	def update(self, mouse_button_left: bool, mx: int, my: int):
		if (mouse_button_left and self.pos.x <= mx <= self.pos.x + self.length and abs(my - self.pos.y) <= 6):
			self.val = self.min_val + (mx - self.pos.x) * (self.max_val - self.min_val) / self.length

pygame.display.set_caption("Diagram")
scrn = pygame.display.set_mode((width, height))
# pp = pygame.image.load(r"C:/Users/vrdhn/Desktop/pp.png")
# pygame.display.set_icon(pp)

def drawArrow(scrn: pygame.Surface, label: str, colour, start_pos: vect.Vector, end_pos: vect.Vector, opp: bool = False):
	start_pos = centre + start_pos.rotate(-0 * DEGREES)
	end_pos = centre + end_pos.rotate(-0 * DEGREES)

	pygame.draw.line(scrn, colour, (start_pos.x, start_pos.y), (end_pos.x, end_pos.y), 5)
	if opp:
		pygame.draw.circle(scrn, colour, (start_pos.x, start_pos.y), 5)
	else:
		pygame.draw.circle(scrn, colour, (end_pos.x, end_pos.y), 5)
	# pygame.draw.line(scrn, colour, (end_pos.x, end_pos.y), (end_pos.x - 20, end_pos.y - 20), 10)
	# pygame.draw.line(scrn, colour, (end_pos.x, end_pos.y), (end_pos.x - 20, end_pos.y - 20), 10)

	scrn.blit(font.render(label, True, WHITE), (end_pos.x + 5, end_pos.y + 5))

theta = Slider("θ", vect.Vector(20, height - 200), 100, -90, 90)
sig_xx = Slider("σ_xx", vect.Vector(20, height - 150), 100, -100, 100)
tau_xy = Slider("τ_xy", vect.Vector(20, height - 100), 100, -100, 100)
sig_yy = Slider("σ_yy", vect.Vector(20, height - 50), 100, -100, 100)

lst_to_write = [theta.val, sig_xx.val, tau_xy.val, sig_yy.val]

while running:
	scrn.fill(BLACK)
	# scrn.fill(WHITE)

	prev_lst_to_write = lst_to_write

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		mouse_button_left = pygame.mouse.get_pressed()[0]
		mx, my = pygame.mouse.get_pos()
		theta.update(mouse_button_left, mx, my)
		sig_xx.update(mouse_button_left, mx, my)
		tau_xy.update(mouse_button_left, mx, my)
		sig_yy.update(mouse_button_left, mx, my)

	theta.show(scrn)
	sig_xx.show(scrn)
	tau_xy.show(scrn)
	sig_yy.show(scrn)

	top_left = centre + vect.Vector(-100, -100).rotate(-0 * DEGREES)
	top_right = centre + vect.Vector(100, -100).rotate(-0 * DEGREES)
	bottom_right = centre + vect.Vector(100, 100).rotate(-0 * DEGREES)
	bottom_left = centre + vect.Vector(-100, 100).rotate(-0 * DEGREES)
	pygame.draw.line(scrn, (255, 128, 0), (top_left.x, top_left.y), (top_right.x, top_right.y), 5)
	pygame.draw.line(scrn, (255, 128, 0), (top_right.x, top_right.y), (bottom_right.x, bottom_right.y), 5)
	pygame.draw.line(scrn, (255, 128, 0), (bottom_right.x, bottom_right.y), (bottom_left.x, bottom_left.y), 5)
	pygame.draw.line(scrn, (255, 128, 0), (bottom_left.x, bottom_left.y), (top_left.x, top_left.y), 5)

	if (abs(sig_xx.val) >= 0.01):
		drawArrow(scrn, f"σ_xx = {sig_xx.val:.2f}", RED, vect.Vector(100, 0), vect.Vector(200, 0), bool(sig_xx.val < 0))
		drawArrow(scrn, "", RED, vect.Vector(-100, 0), vect.Vector(-200, 0), bool(sig_xx.val < 0))

	if (abs(tau_xy.val) >= 0.01):
		drawArrow(scrn, "", GREEN, vect.Vector(-80, -120), vect.Vector(80, -120), bool(tau_xy.val < 0))
		drawArrow(scrn, f"τ_xy = {tau_xy.val:.2f}", GREEN, vect.Vector(120, 80), vect.Vector(120, -80), bool(tau_xy.val < 0))
		drawArrow(scrn, "", GREEN, vect.Vector(80, 120), vect.Vector(-80, 120), bool(tau_xy.val < 0))
		drawArrow(scrn, "", GREEN, vect.Vector(-120, -80), vect.Vector(-120, 80), bool(tau_xy.val < 0))

	if (abs(sig_yy.val) >= 0.01):
		drawArrow(scrn, f"σ_yy = {sig_yy.val:.2f}", BLUE, vect.Vector(0, 100), vect.Vector(0, 200), bool(sig_yy.val < 0))
		drawArrow(scrn, "", BLUE, vect.Vector(0, -100), vect.Vector(0, -200), bool(sig_yy.val < 0))

	lst_to_write = [theta.val, sig_xx.val, tau_xy.val, sig_yy.val]

	if prev_lst_to_write != lst_to_write:
		fp = open("data.txt", 'w')
		fp.write(str(lst_to_write))
		fp.close()

	pygame.display.update()

pygame.quit()