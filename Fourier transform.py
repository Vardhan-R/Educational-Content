import math, pygame, random, time

pygame.init()

width = 1600
height = 1200
p = []
# for i in range(10):
    # p.append((random.randrange(100, 500), random.randrange(100, 500)))
# p = [(100, 10), (500, 400), (490, 310), (200, 190), (190, 240)]
# p = [(200, 300), (300, 400), (400, 300), (300, 200)]
# p = [(100, 500), (100, 300), (100, 100), (400, 300)]
# p = [(150, 446), (150, 446), (150, 446), (150, 446), (150, 446), (150, 446), (143, 400), (135, 328), (134, 284), (134, 262), (136, 237), (139, 217), (149, 181), (161, 159), (179, 139), (222, 103), (255, 87), (280, 81), (295, 80), (305, 83), (320, 91), (338, 104), (351, 121), (362, 143), (369, 169), (373, 189), (373, 210), (364, 232), (347, 254), (329, 268), (277, 289), (192, 312), (147, 320), (138, 320), (138, 320), (138, 320), (138, 320), (138, 320), (138, 320), (196, 323), (328, 345), (352, 357), (362, 370), (370, 386), (378, 413), (378, 429), (374, 443), (367, 455), (354, 466), (342, 473), (312, 483), (280, 491), (250, 496), (235, 498), (218, 498), (202, 497), (189, 494), (179, 491), (168, 488), (156, 483), (146, 480)] # B
# p = [(295, 112), (294, 112), (284, 112), (264, 114), (247, 120), (231, 129), (217, 142), (201, 162), (193, 186), (191, 219), (193, 244), (202, 268), (222, 299), (248, 320), (276, 339), (298, 352), (324, 369), (345, 386), (367, 407), (380, 425), (390, 441), (398, 457), (401, 473), (402, 486), (402, 494), (400, 498), (397, 501), (391, 505), (386, 509), (371, 512), (347, 515), (329, 516), (313, 516), (278, 513), (259, 509), (243, 504), (226, 500), (215, 493), (199, 478), (192, 468), (186, 456), (185, 450), (186, 442), (194, 429), (212, 408), (230, 389), (259, 363), (286, 341), (315, 309), (332, 278), (339, 259), (343, 246), (343, 237), (342, 225), (340, 217), (335, 206), (325, 188), (318, 175), (309, 163), (297, 151), (281, 143), (253, 137), (237, 136), (231, 136)] # 8
# p = [(341, 87), (341, 88), (340, 90), (328, 97), (300, 101), (266, 101), (239, 101), (208, 101), (197, 101), (192, 102), (195, 112), (201, 134), (204, 156), (204, 180), (206, 215), (211, 252), (214, 285), (214, 300), (214, 300), (214, 317), (215, 356), (216, 379), (217, 398), (216, 414), (216, 441), (217, 465), (208, 481), (195, 505), (193, 523), (193, 523), (191, 561), (191, 572), (200, 579), (227, 582), (244, 575), (262, 557), (278, 522), (291, 468), (296, 445), (295, 447), (287, 482), (287, 519), (295, 554), (313, 575), (340, 584), (363, 585), (376, 575), (387, 556), (389, 525), (370, 479), (359, 463), (355, 444), (355, 444), (355, 420), (355, 350), (352, 318), (352, 316), (352, 316), (347, 282), (345, 236), (344, 191), (344, 155), (344, 124), (343, 109), (343, 95), (341, 91), (332, 95), (308, 108), (284, 112), (241, 112), (205, 110), (196, 103), (193, 89), (201, 79), (212, 64), (215, 54), (215, 54), (215, 54), (219, 44), (228, 37), (238, 24), (244, 16), (251, 14), (260, 15), (263, 21), (263, 28), (263, 27), (263, 15), (264, 9), (273, 8), (289, 10), (302, 13), (313, 21), (326, 34), (339, 51), (343, 61), (344, 74), (344, 88)] # dick
# p = [] # eye
# p = [(270, 117), (270, 117), (270, 117), (270, 117), (271, 118), (273, 132), (273, 143), (270, 156), (266, 173), (260, 192), (256, 205), (253, 212), (246, 222), (239, 233), (230, 250), (223, 268), (216, 282), (212, 297), (212, 309), (214, 333), (216, 345), (217, 346), (217, 346), (217, 346), (217, 346), (219, 354), (228, 378), (234, 394), (239, 407), (247, 421), (254, 436), (261, 451), (267, 463), (270, 473), (273, 481), (274, 488), (274, 493), (274, 496), (274, 497), (274, 497), (274, 495), (275, 490), (277, 481), (280, 459), (285, 445), (288, 438), (295, 431), (306, 419), (317, 408), (326, 394), (332, 379), (335, 362), (338, 342), (338, 314), (336, 292), (336, 290), (336, 290), (336, 290), (336, 290), (334, 274), (330, 263), (321, 248), (314, 233), (306, 219), (299, 207), (292, 195), (288, 183), (284, 169), (279, 157), (276, 146), (275, 137), (272, 129), (270, 121), (269, 113), (269, 112)] # pussy
# for i in range(3):
    # p.append((width * i / 3, 300))
# p.pop(0)
# p.pop(-1)
# p = [(29, 502), (47, 499), (160, 504), (276, 503), (269, 470), (293, 459), (357, 470), (437, 481), (501, 478), (461, 492), (388, 492), (310, 493), (263, 466), (269, 440), (347, 434), (435, 432), (498, 436), (482, 448), (430, 447), (402, 430), (364, 401), (337, 367), (326, 341), (311, 280), (322, 239), (351, 215), (360, 212), (336, 189), (336, 174), (376, 193), (433, 199), (466, 186), (484, 180), (479, 220), (468, 220), (486, 259), (490, 314), (497, 337), (518, 387), (524, 408), (489, 393), (444, 358), (418, 329), (400, 297), (395, 260), (420, 242), (439, 256), (431, 288), (398, 284), (415, 275), (405, 292), (374, 298), (341, 289), (339, 259), (363, 242), (381, 266), (375, 287), (351, 276), (370, 273), (363, 297), (372, 330), (408, 306), (466, 295), (509, 312), (519, 338), (544, 407), (564, 453), (509, 433), (489, 445), (477, 460), (482, 481), (492, 488), (524, 501), (595, 499)] # owl
# p = [(1, 501), (42, 500), (155, 497), (190, 499), (175, 476), (168, 453), (181, 440), (190, 459), (224, 479), (280, 476), (334, 476), (401, 484), (401, 492), (359, 492), (311, 488), (256, 489), (186, 489), (164, 474), (162, 443), (196, 434), (263, 428), (297, 428), (328, 430), (371, 432), (396, 435), (403, 445), (363, 449), (323, 448), (315, 447), (287, 416), (257, 384), (234, 358), (217, 315), (214, 250), (223, 235), (233, 226), (255, 210), (252, 210), (238, 199), (237, 176), (245, 175), (261, 192), (291, 199), (313, 197), (336, 204), (354, 200), (373, 178), (383, 173), (387, 196), (379, 221), (363, 216), (366, 219), (380, 239), (390, 269), (392, 303), (392, 315), (397, 347), (417, 380), (427, 404), (418, 405), (377, 388), (344, 363), (317, 327), (302, 307), (291, 267), (302, 244), (324, 241), (335, 253), (336, 273), (324, 290), (306, 290), (295, 275), (307, 267), (315, 279), (306, 289), (287, 294), (261, 295), (234, 280), (240, 253), (265, 239), (284, 252), (283, 276), (275, 288), (255, 283), (256, 268), (267, 271), (269, 285), (260, 295), (267, 322), (275, 334), (290, 313), (334, 300), (374, 293), (396, 303), (407, 329), (421, 362), (438, 399), (455, 422), (463, 446), (454, 453), (430, 443), (409, 433), (398, 435), (387, 442), (378, 457), (379, 473), (398, 491), (450, 502), (499, 502), (549, 493), (577, 496), (599, 495)] # owl 2
# p = [(445, 191), (468, 185), (491, 172), (503, 138), (496, 92), (483, 53), (488, 19), (516, 23), (473, 38), (417, 40), (356, 37), (315, 29), (295, 12), (318, 18), (314, 55), (297, 88), (291, 131), (297, 156), (329, 196), (354, 235), (373, 265), (381, 311), (366, 359), (340, 393), (310, 422), (269, 458), (197, 500), (136, 521), (86, 531), (60, 532), (71, 508), (88, 462), (109, 419), (125, 391), (139, 368), (172, 315), (206, 268), (261, 230), (312, 195), (365, 194), (406, 205), (449, 230), (475, 290), (473, 344), (458, 369), (434, 415), (380, 451), (318, 478), (284, 500), (296, 533), (316, 566), (299, 593), (300, 570), (340, 556), (377, 574)] # owl 3
# p = [(471, 187), (501, 152), (498, 104), (486, 64), (487, 21), (510, 27), (468, 37), (424, 39), (375, 36), (329, 31), (294, 20), (312, 15), (309, 56), (288, 110), (302, 167), (331, 202), (364, 245), (383, 306), (363, 357), (332, 403), (295, 439), (251, 474), (203, 499), (156, 514), (108, 524), (59, 525), (79, 482), (95, 444), (116, 405), (140, 363), (170, 318), (203, 277), (245, 234), (282, 210), (319, 194), (367, 192), (410, 211), (446, 237), (470, 276), (473, 322), (458, 365), (435, 400), (408, 428), (378, 450), (347, 464), (317, 475), (291, 486), (286, 520), (304, 547), (317, 576), (293, 583), (311, 562), (339, 561), (368, 571), (384, 587)] # owl (p much evenly spaced out pts)
# p = [(297, 156), (303, 141), (311, 125), (318, 108), (325, 97), (333, 85), (341, 74), (350, 63), (360, 53), (371, 41), (382, 32), (395, 24), (408, 17), (419, 12), (434, 8), (452, 6), (469, 5), (484, 8), (499, 12), (511, 18), (524, 27), (535, 35), (545, 43), (553, 53), (560, 64), (566, 73), (572, 84), (577, 96), (581, 109), (585, 123), (588, 137), (590, 153), (591, 170), (591, 186), (590, 203), (588, 218), (586, 233), (582, 249), (579, 263), (575, 277), (570, 290), (565, 305), (560, 318), (554, 331), (548, 343), (541, 357), (534, 370), (527, 382), (520, 394), (513, 404), (505, 417), (495, 429), (485, 441), (476, 452), (465, 465), (453, 478), (442, 487), (433, 497), (423, 507), (409, 518), (397, 527), (386, 537), (374, 546), (363, 553), (353, 561), (342, 567), (329, 575), (319, 582), (308, 588), (298, 593), (287, 588), (273, 581), (261, 572), (249, 565), (235, 556), (221, 546), (208, 537), (195, 526), (183, 515), (171, 505), (161, 497), (151, 486), (141, 478), (131, 468), (122, 458), (114, 446), (104, 435), (93, 422), (84, 409), (76, 398), (67, 383), (59, 368), (50, 352), (42, 335), (35, 319), (28, 302), (22, 287), (17, 269), (13, 253), (8, 235), (6, 217), (5, 202), (3, 186), (3, 171), (4, 160), (5, 147), (7, 132), (10, 119), (13, 106), (17, 94), (24, 82), (30, 71), (37, 59), (46, 49), (55, 38), (66, 29), (79, 21), (91, 14), (104, 9), (120, 6), (135, 6), (150, 7), (163, 8), (176, 12), (188, 18), (199, 23), (212, 32), (222, 40), (230, 48), (239, 56), (247, 64), (254, 74), (263, 87), (270, 97), (276, 109), (284, 127), (291, 142)] # heart
# p = [(518, 58), (568, 63), (617, 81), (666, 104), (712, 134), (759, 170), (801, 209), (841, 250), (882, 293), (925, 339), (966, 387), (1003, 433), (1029, 483), (1050, 533), (1065, 583), (1070, 633), (1069, 683), (1066, 733), (1058, 783), (1043, 832), (1021, 881), (993, 929), (957, 972), (909, 1001), (859, 1010), (809, 1019), (759, 1019), (709, 1019), (659, 1015), (609, 1006), (559, 995), (509, 981), (459, 960), (410, 936), (361, 906), (315, 871), (274, 824), (244, 776), (218, 727), (201, 677), (191, 627), (187, 577), (188, 527), (194, 477), (205, 427), (217, 377), (235, 328), (257, 279), (283, 229), (317, 183), (357, 146), (400, 113), (449, 84), (497, 72)]
# p = [(578, 84), (747, 99), (919, 99), (1091, 105), (1263, 131), (1425, 252), (1490, 424), (1541, 596), (1555, 768), (1516, 941), (1386, 1085), (1214, 1117), (1042, 1138), (870, 1147), (697, 1138), (525, 1125), (353, 1100), (183, 1015), (99, 844), (177, 684), (349, 655), (521, 707), (692, 756), (791, 919), (963, 937), (1135, 939), (1306, 876), (1429, 716), (1432, 544), (1368, 372), (1239, 243), (1067, 218), (955, 296), (1127, 295), (1266, 385), (1292, 557), (1263, 730), (1137, 861), (965, 848), (855, 684), (840, 512), (824, 339), (689, 347), (621, 519), (500, 462), (398, 431), (299, 518), (327, 346), (420, 180), (578, 84)]
# p = [(56, 85), (56, 85), (79, 184), (107, 307), (112, 296), (142, 164), (156, 81), (160, 98), (175, 194), (253, 180), (270, 190), (230, 206), (196, 295), (247, 272), (265, 185), (284, 304), (392, 170), (352, 195), (496, 188), (495, 302), (659, 203), (664, 202), (605, 308), (679, 147), (671, 80), (686, 294), (751, 158), (739, 87), (755, 307), (772, 265), (808, 279), (829, 262), (914, 232), (913, 210), (875, 300), (930, 214), (966, 295), (1010, 203), (1022, 282), (1056, 207), (1102, 275)] # signature 1
# p = [(44, 78), (44, 78), (44, 89), (46, 130), (53, 162), (61, 189), (77, 241), (90, 274), (95, 287), (98, 294), (98, 294), (100, 290), (113, 253), (128, 193), (144, 123), (154, 86), (155, 82), (155, 82), (157, 97), (163, 134), (174, 146), (195, 165), (212, 167), (263, 168), (300, 182), (301, 183), (281, 186), (229, 197), (210, 241), (223, 285), (262, 262), (277, 219), (282, 180), (282, 229), (284, 266), (395, 277), (438, 220), (405, 140), (374, 146), (365, 156), (425, 163), (440, 163), (442, 185), (440, 236), (446, 245), (497, 205), (562, 174), (568, 174), (581, 176), (570, 175), (506, 243), (517, 282), (531, 279), (582, 181), (591, 65), (593, 55), (593, 55), (577, 176), (580, 289), (604, 276), (652, 202), (665, 80), (665, 84), (665, 232), (670, 259), (673, 252), (693, 212), (697, 214), (708, 236), (724, 259), (776, 206), (801, 196), (801, 196), (803, 191), (798, 181), (740, 276), (749, 297), (776, 276), (800, 212), (801, 245), (812, 278), (849, 241), (870, 181), (870, 213), (870, 282), (877, 260), (917, 162), (956, 250), (972, 283), (972, 283)] # signature 2
txt_file = open("python_files/signature.txt", 'r') # signature 3
p = txt_file.readlines()
for i in range(len(p)):
    temp = p[i].split(" ")
    p[i] = (int(temp[0]), int(temp[1]))
txt_file.close()

# t < 2 * math.pi * (nN - 2) / (nN - 1) ==> non-cyclic

pts = []
all_pts = []
nN = len(p)
freqs = []
coeffs = []
coeffs_mag = []
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
running = True

scrn = pygame.display.set_mode((width, height))

def write(re, im): return str(re) + " + " + str(im) + "i"

class Comp:
    def __init__(self, r, i):
        self.r = r
        self.i = i
        self.z = str(r) + " + " + str(i) + "i"

    def copy(self): return Comp(self.r, self.i)

    def mag(self): return math.sqrt(self.r ** 2 + self.i ** 2)

    def magSq(self): return self.r ** 2 + self.i ** 2

    def normalise(self): return self.write(self.r / self.mag(), self.i / self.mag())

    def setMag(self, m):
        try:
            old_mag = self.mag()
            self.r = m * self.r / old_mag
            self.i = m * self.i / old_mag
        except: pass

    def angle(self):
        if math.atan2(self.i, self.r) < 0: return 2 * math.pi + math.atan2(self.i, self.r)
        else: return math.atan2(self.i, self.r)

    # def plot(self, clr):
    #     pygame.draw.circle(scrn, clr, (width * (xl - self.r) / (xl - xr), height * (yu - self.i) / (yu - yd)), 4)

def add(z1, z2): return Comp(z1.r + z2.r, z1.i + z2.i)
def sub(z1, z2): return Comp(z1.r - z2.r, z1.i - z2.i)
def mult(z1, z2): return Comp(z1.r * z2.r - z1.i * z2.i, z1.r * z2.i + z1.i * z2.r)
def root(n, z):
    roots = []
    for k in range(n): roots.append(Comp((z.mag() ** (1 / n)) * math.cos((z.angle() + 2 * math.pi * k) / n), (z.mag() ** (1 / n)) * math.sin((z.angle() + 2 * math.pi * k) / n)))
    return roots
def compPolar(r, t):
    return Comp(r * math.cos(t), r * math.sin(t))
def compExp(r, t):
    return Comp(r * math.cos(t), r * math.sin(t))

def sortCheck(l):
    for m in range(len(l) - 1):
        if l[m] < l[m + 1]:
            return False
    return True

for i in p:
    pts.append(Comp(i[0], i[1]))

for i in range(round(-(nN - 1) / 2), round((nN + 1) / 2)):
    freqs.append(i)

for i in freqs:
    c = Comp(0, 0)
    for j in range(nN):
        c = add(c, mult(pts[j], Comp(math.cos(2 * math.pi * i * j / nN), -math.sin(2 * math.pi * i * j / nN))))
    coeffs.append(c)

for i in coeffs:
    coeffs_mag.append(i.mag())

while not(sortCheck(coeffs_mag)):
    for i in range(len(coeffs_mag) - 1):
        if coeffs_mag[i] < coeffs_mag[i + 1]:
            temp = coeffs_mag[i]
            coeffs_mag[i] = coeffs_mag[i + 1]
            coeffs_mag[i + 1] = temp

            temp = coeffs[i]
            coeffs[i] = coeffs[i + 1]
            coeffs[i + 1] = temp

            temp = freqs[i]
            freqs[i] = freqs[i + 1]
            freqs[i + 1] = temp

t = 0

while running:
    scrn.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if t < 2 * math.pi * (nN - 2) / (nN - 1):
    # if t < 2 * math.pi:
        pt = Comp(0, 0)
        for i in range(len(freqs)):
            temp_pt = mult(coeffs[i], compExp(1, freqs[i] * t))
            pygame.draw.circle(scrn, white, (p[i][0], p[i][1]), 2)
            pygame.draw.circle(scrn, green, (pt.r / nN, pt.i / nN), coeffs[i].mag() / nN, width = 1)
            pygame.draw.line(scrn, green, (pt.r / nN, pt.i / nN), (add(pt, temp_pt).r / nN, add(pt, temp_pt).i / nN))
            pt = add(pt, temp_pt)
        pt.setMag(pt.mag() / nN)
        pygame.draw.circle(scrn, red, (pt.r, pt.i), 2)
        all_pts.append(pt)
        t += math.pi / 5000
    else:
        break

    pygame.display.update()

# for i in p:
#     pygame.draw.circle(scrn, white, (i[0], i[1]), 2)
for i in all_pts:
    pygame.draw.circle(scrn, red, (i.r, i.i), 1)

pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()