import pygame as pg
from pygame.draw import *

pg.init()
FPS = 30

screen = pg.display.set_mode((400, 400))

rect(screen, (225, 225, 225), (0, 0, 400, 400))
circle(screen, (0, 0, 0), (200, 200), 102, 2)
circle(screen, (225, 225, 0), (200, 200), 100)
rect(screen, (0, 0, 0), (150, 240, 100, 20))
circle(screen, (225, 0, 0), (160, 170), 20)
circle(screen, (0, 0, 0), (160, 170), 21, 2)
circle(screen, (0 ,0, 0), (160, 170), 9)
circle(screen, (225, 0, 0), (240, 170), 20)
circle(screen, (0, 0, 0), (240, 170), 21, 2)
circle(screen, (0 ,0, 0), (240, 170), 9)
polygon(screen, (0, 0, 0), [(185, 160), (100, 120), (100, 115), (184, 154), (185, 160)])
polygon(screen, (0, 0, 0), [(215, 160), (300, 120), (300, 115), (216, 154), (215, 160)])

pg.display.update()
clock = pg.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

pg.quit()