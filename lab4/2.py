import pygame as pg
from pygame.draw import *

pg.init()
FPS = 30
alpha = 150
#Координаты верхнего левого угла машины
x = 135
y = 450

screen = pg.display.set_mode((350, 500))
surface1 = pg.Surface((550, 400), pg.SRCALPHA)
surface2 = pg.Surface((550, 400), pg.SRCALPHA)
surface3 = pg.Surface((550, 400), pg.SRCALPHA)
surface4 = pg.Surface((550, 600), pg.SRCALPHA)
surface5 = pg.Surface((550, 600), pg.SRCALPHA)

#Фон
rect(screen, (184, 197, 201), (0, 0, 350, 270))
rect(screen, (225, 225, 225), (0, 270, 350, 5))
rect(screen, (82, 108, 103), (0, 275, 350, 225))
#Дома и облака
##Справа
rect(screen, (220, 228, 227), (260, 10, 77, 275))
rect(screen, (111, 146, 139), (220, 60, 70, 275))
ellipse(surface1, (169, 187, 187, alpha), (-30, 3, 260, 80))
ellipse(surface1, (169, 187, 187, alpha), (150, -25, 260, 80))
screen.blit(surface1, (0, 0))
##Слева
rect(screen, (148, 168, 173), (7, 10, 77, 275))
rect(screen, (148, 173, 168), (100, 25, 77, 275))
ellipse(surface2, (169, 187, 187, alpha), (-50, 180, 260, 80))
screen.blit(surface2, (0 ,0))
rect(screen, (184, 201, 197), (70, 70, 77, 275))
##Середина
ellipse(surface3, (169, 187, 187, alpha), (90, 100, 300, 80))
screen.blit(surface3, (0, 0))
#Машина и дым от нее
ellipse(screen, (184, 201, 197), (-20, 400, 500, 150))
ellipse(screen, (0, 0, 0), (x - 12, y - 10, 15, 5))
polygon(screen, (0, 205, 255) ,[(x, y), (x, y - 30), (x + 30, y - 30), 
(x + 30, y - 50), (x + 95, y - 50), (x + 95, y - 30), (x + 145, y - 30), 
(x + 145, y), (x, y)])
circle(screen, (0, 0, 0), (x + 28, y), 14)
circle(screen, (0, 0, 0), (x + 117, y), 14)
rect(screen, (255, 255, 255), (x + 34, y - 47, 25, 17))
rect(screen, (255, 255, 255), (x + 66, y - 47, 25, 17))
ellipse(surface4, (108, 134, 129, alpha), (20, 415, 95, 30))
ellipse(surface4, (108, 134, 129, alpha), (15, 375, 95, 30))
ellipse(surface4, (108, 134, 129, alpha), (-40, 340, 95, 30))

screen.blit(surface4, (0, 0))
pg.display.update()
clock = pg.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

pg.quit()