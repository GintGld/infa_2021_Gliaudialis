import pygame as pg
from pygame.draw import *

pg.init()
FPS = 30
alpha = 150

def car(x, y):
    ellipse(screen, (0, 0, 0), (x + 77, y - 6, 10, 4))
    polygon(screen, (36, 204, 242), 
    [
        (x, y), (x, y - 15), (x + 25, y - 15),
        (x + 25, y - 26), (x + 60, y - 26), (x + 60, y - 15),
        (x + 80, y - 15), (x + 80, y), (x, y)
    ])
    rect(screen, (255, 255, 255), (x + 29, y - 24, 12, 8))
    rect(screen, (255, 255, 255), (x + 46, y - 24, 12, 8))
    circle(screen, (0, 0, 0), (x + 18, y), 7)
    circle(screen, (0, 0, 0), (x + 62, y), 7)

def carh1(x, y):
    ellipse(screen, (0, 0, 0), (x - 12, y - 9, 18, 5))
    polygon(screen, (36, 204, 242), 
    [
        (x, y), (x, y - 40), (x + 40, y - 40), 
        (x + 40, y - 70), (x + 130, y - 70), (x + 130, y - 40), 
        (x + 185, y - 40), (x + 185, y), (x, y)
    ])
    rect(screen, (255, 255, 255), (x + 46, y - 65, 35, 25))
    rect(screen, (255, 255, 255), (x + 90, y - 65, 35, 25))
    circle(screen, (0, 0, 0), (x + 40, y), 18)
    circle(screen, (0, 0, 0), (x + 150, y), 18)

def carh2(x, y):
    ellipse(screen, (0, 0, 0), (x - 3, y - 9, 15, 5))
    polygon(screen, (36, 204, 242), 
    [
        (x, y), (x, y - 40), (x - 40, y - 40), 
        (x - 40, y - 70), (x - 130, y - 70), (x - 130, y - 40), 
        (x - 185, y - 40), (x - 185, y), (x, y)
    ])
    rect(screen, (255, 255, 255), (x - 80, y - 65, 35, 25))
    rect(screen, (255, 255, 255), (x - 124, y - 65, 35, 25))
    circle(screen, (0, 0, 0), (x - 40, y), 18)
    circle(screen, (0, 0, 0), (x - 150, y), 18)

screen = pg.display.set_mode((550, 700))
surface1 = pg.Surface((550, 400), pg.SRCALPHA)
surface2 = pg.Surface((550, 400), pg.SRCALPHA)
surface3 = pg.Surface((550, 400), pg.SRCALPHA)
surface4 = pg.Surface((550, 600), pg.SRCALPHA)
surface5 = pg.Surface((550, 600), pg.SRCALPHA)
surface6 = pg.Surface((550, 700), pg.SRCALPHA)
surface7 = pg.Surface((550, 700), pg.SRCALPHA)
surface8 = pg.Surface((550, 700), pg.SRCALPHA)

rect(screen, (85, 112, 106), (0, 300, 550, 600))

#Up
for i in range(140):
    rect(screen, (235 - i, 235 - i, 235 - i), (0, i, 413, 1))
    rect(screen, (i + 20, i + 20, i + 20), (413, i, 137, 1))
rect(surface1, (15, 15, 15), (530, 0, 20, 140))
rect(surface1, (20, 20, 20), (353, 0, 80, 140))
rect(surface1, (0, 0, 0, 100), (0, 0, 40, 140))
screen.blit(surface1, (0, 0))
rect(surface2, (0, 0, 0, 150), (313, 0, 80, 140))
rect(surface2, (0, 0, 0, 150), (223, 20, 80, 140))
rect(surface2, (0, 0, 0, 150), (0, 70, 70, 140))
screen.blit(surface2, (0, 0))
rect(surface3, (0, 0, 0, 150), (255, 60, 80, 140))
ellipse(surface3, (40, 40, 40, 100), (-30, -20, 300, 60))
screen.blit(surface3, (0, 0))
ellipse(surface4, (50, 50, 50, alpha - 100), (150, -30, 500, 90))
ellipse(surface4, (40, 40, 40, alpha), (490, 90, 200, 70))
ellipse(surface4, (20, 20, 20, 100), (-50, 110, 300, 60))
screen.blit(surface4, (0, 0))
ellipse(surface5, (20, 20, 20, alpha - 70), (100, 10, 450, 70))
screen.blit(surface5, (0, 0))
rect(screen, (255, 255, 255), (413, 0, 3, 140))

#Right
rect(screen, (255, 255, 255), (187, 127, 376, 356))
rect(screen, (183, 198, 200), (190, 130, 370, 350))
rect(screen, (148, 168, 173), (500, 140, 50, 337))
rect(screen, (148, 173, 168), (420, 155, 70, 328))
rect(screen, (112, 146, 139), (290, 195, 75, 335))
ellipse(surface6, (168, 186, 186, 150), (340, 150, 300, 55))
screen.blit(surface6, (0, 0))
rect(screen, (182, 199, 195), (450, 187, 75, 342))

#Left
rect(screen, (255, 255, 255), (0, 140, 328, 366))
rect(screen, (183, 198, 200), (0, 143, 325, 360))
rect(screen, (148, 168, 173), (0, 148, 10, 50))
rect(screen, (148, 173, 168), (20, 163, 70, 343))
rect(screen, (184, 201, 197), (0, 200, 70, 343))
rect(screen, (220, 228, 227), (220, 170, 80, 334))
rect(screen, (111, 146, 139), (180, 210, 80, 335))

#Down
car(40, 555)
car(210, 560)
car(335, 555)
car(440, 570)
carh1(60, 650)
carh2(490, 670)

#On the top
for i in range(200):
    circle(surface7, (255, 255, 255, 150 - 150 * i / 200), (260, 620), i, 2)
screen.blit(surface7, (0, 0))
for i in range(150):
    rect(surface8, (125, 156, 150, 150 - 150 * i / 150), (0, 310 - i, 550, 1))
    rect(surface8, (125, 156, 150, 150 - 150 * i / 150), (0, 310 + i, 550, 1))
screen.blit(surface8, (0, 0))

pg.display.update()
clock = pg.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

pg.quit()