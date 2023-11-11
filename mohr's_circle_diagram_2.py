from built_modules import import_vectors as vect
from manim import *
import math, pygame, time

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

pygame.display.set_caption("Diagram 2")
scrn = pygame.display.set_mode((width, height))
# pp = pygame.image.load(r"C:/Users/vrdhn/Desktop/pp.png")
# pygame.display.set_icon(pp)

def drawArrow(scrn: pygame.Surface, label: str, colour, start_pos: vect.Vector, end_pos: vect.Vector, opp: bool = False):
	start_pos = centre + start_pos.rotate(-theta.val * DEGREES)
	end_pos = centre + end_pos.rotate(-theta.val * DEGREES)

	pygame.draw.line(scrn, colour, (start_pos.x, start_pos.y), (end_pos.x, end_pos.y), 5)
	if opp:
		pygame.draw.circle(scrn, colour, (start_pos.x, start_pos.y), 5)
	else:
		pygame.draw.circle(scrn, colour, (end_pos.x, end_pos.y), 5)
	# pygame.draw.line(scrn, colour, (end_pos.x, end_pos.y), (end_pos.x - 20, end_pos.y - 20), 10)
	# pygame.draw.line(scrn, colour, (end_pos.x, end_pos.y), (end_pos.x - 20, end_pos.y - 20), 10)

	scrn.blit(font.render(label, True, WHITE), (end_pos.x + 5, end_pos.y + 5))

theta = Slider("θ", vect.Vector(0, 0), 100, -90, 90)
sig_xx = Slider("σ_xx", vect.Vector(0, 0), 100, -100, 100)
tau_xy = Slider("τ_xy", vect.Vector(0, 0), 100, -100, 100)
sig_yy = Slider("σ_yy", vect.Vector(0, 0), 100, -100, 100)

while running:
	scrn.fill(BLACK)
	# scrn.fill(WHITE)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	try:
		fp = open("data.txt", 'r')
		str_read = fp.readline()
		fp.close()

		theta.val, sig_xx.val, tau_xy.val, sig_yy.val = eval(str_read)

		r = math.sqrt(((sig_xx.val - sig_yy.val) / 2) ** 2 + tau_xy.val ** 2)
		c = vect.Vector((sig_xx.val + sig_yy.val) / 2, 0)
		# theta_0 = math.atan2(tau_xy.val, sig_xx.val)
		sig_diff = (sig_xx.val - sig_yy.val) / 2

		new_sig_xx = c.x + sig_diff * math.cos(2 * theta.val * DEGREES) + tau_xy.val * math.sin(2 * theta.val * DEGREES)
		new_tau_xy = c.y - sig_diff * math.sin(2 * theta.val * DEGREES) + tau_xy.val * math.cos(2 * theta.val * DEGREES)
		new_sig_yy = c.x - sig_diff * math.cos(2 * theta.val * DEGREES) - tau_xy.val * math.sin(2 * theta.val * DEGREES)

		sig_xx.val = new_sig_xx
		tau_xy.val = new_tau_xy
		sig_yy.val = new_sig_yy

		top_left = centre + vect.Vector(-100, -100).rotate(-theta.val * DEGREES)
		top_right = centre + vect.Vector(100, -100).rotate(-theta.val * DEGREES)
		bottom_right = centre + vect.Vector(100, 100).rotate(-theta.val * DEGREES)
		bottom_left = centre + vect.Vector(-100, 100).rotate(-theta.val * DEGREES)
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

		scrn.blit(font.render(f"θ = {theta.val}", True, WHITE), (10, 10))
	except:
		print("Error: try failed.")

	pygame.display.update()
	time.sleep(0.05)

pygame.quit()