import pygame as pg
import numpy as np
from pygame.draw import *

pg.init()

FPS = 0.5
screen = pg.display.set_mode((700, 850))
# закрашиваем фон
screen.fill((230, 230, 230))
rect(screen, (250, 250, 250), (0, 400, 700, 500))

def igl(x, y, width, height):
    for i in range(width): 
        arc(screen, (231, 231, 231), (x + i, y + 0.5 * i * height / width, width - 2 * i, height - i * height / width), 0, np.pi, 4)
    arc(screen, (0, 0, 0), (x, y, width, height), 0, np.pi, 2)
    line(screen, (0, 0, 0), [x, y + height / 2], [x + width, y + height / 2], 2)
    line(screen, (0, 0, 0), [x + 0.03 * width, y + height / 2 - 0.15 * height], [x + width - 0.03 * width, y + height / 2 - 0.15 * height], 2)
    line(screen, (0, 0, 0), [x + 0.1 * width, y + height / 2 - 0.3 * height], [x + width - 0.1 * width, y + height / 2 - 0.3 * height], 2)
    line(screen, (0, 0, 0), [x + 0.23 * width, y + height / 2 - 0.42 * height], [x + width - 0.23 * width, y + height / 2 - 0.42 * height], 2)
    aaline(screen, (0, 0, 0), [x + width / 2, y], [x + 0.52 * width, y + height / 2 - 0.42 * height], 3)
    aaline(screen, (0, 0, 0), [x + 0.33 * width, y + height / 2 - 0.42 * height], [x + 0.3 * width, y + height / 2 - 0.3 * height], 3)
    aaline(screen, (0, 0, 0), [x + 0.6 * width, y + height / 2 - 0.42 * height], [x + 0.63 * width, y + height / 2 - 0.3 * height], 3)
    aaline(screen, (0, 0, 0), [x + 0.7 * width, y + height / 2 - 0.42 * height], [x + 0.72 * width, y + height / 2 - 0.3 * height], 3)
    aaline(screen, (0, 0, 0), [x + 0.28 * width, y + height / 2 - 0.3 * height], [x + 0.26 * width, y + height / 2 - 0.15 * height], 3)
    aaline(screen, (0, 0, 0), [x + 0.35 * width, y + height / 2 - 0.3 * height], [x + 0.37 * width, y + height / 2 - 0.15 * height], 3)
    aaline(screen, (0, 0, 0), [x + 0.6 * width, y + height / 2 - 0.3 * height], [x + 0.64 * width, y + height / 2 - 0.15 * height], 3)
    aaline(screen, (0, 0, 0), [x + 0.8 * width, y + height / 2 - 0.3 * height], [x + 0.78 * width, y + height / 2 - 0.15 * height], 3)
    aaline(screen, (0, 0, 0), [x + 0.18 * width, y + height / 2 - 0.15 * height], [x + 0.16 * width, y + height / 2], 3)
    aaline(screen, (0, 0, 0), [x + 0.22 * width, y + height / 2 - 0.15 * height], [x + 0.24 * width, y + height / 2], 3)
    aaline(screen, (0, 0, 0), [x + 0.4 * width, y + height / 2 - 0.15 * height], [x + 0.42 * width, y + height / 2], 3)
    aaline(screen, (0, 0, 0), [x + 0.56 * width, y + height / 2 - 0.15 * height], [x + 0.54 * width, y + height / 2], 3)
    aaline(screen, (0, 0, 0), [x + 0.68 * width, y + height / 2 - 0.15 * height], [x + 0.7 * width, y + height / 2], 3)
    aaline(screen, (0, 0, 0), [x + 0.85 * width, y + height / 2 - 0.15 * height], [x + 0.82 * width, y + height / 2], 3)

def man(x, y, width, height):
    circle(screen, (228, 223, 220), (x + 0.51 * width, y + 0.15 * height), 0.15 * height)
    ellipse(screen, (146, 125, 112), (x + 0.17 * width, y + 0.2 * height, 0.7 * width, 1.2 * height))
    rect(screen, (250, 250, 250), (x + 0.17 * width, y + 0.8 * height, 0.7 * width, 0.6 * height))
    ellipse(screen, (146, 125, 112), (x + 0.26 * width, y + 0.67 * height, 0.2 * width, 0.3 * height))
    ellipse(screen, (146, 125, 112), (x + 0.58 * width, y + 0.67 * height, 0.2 * width, 0.3 * height))
    ellipse(screen, (146, 125, 112), (x + 0.12 * width, y + 0.87 * height, 0.3 * width, 0.13 * height))
    ellipse(screen, (146, 125, 112), (x + 0.62 * width, y + 0.87 * height, 0.3 * width, 0.13 * height))
    ellipse(screen, (146, 125, 112), (x + 0.02 * width, y + 0.45 * height, 0.35 * width, 0.1 * height))
    ellipse(screen, (146, 125, 112), (x + 0.64 * width, y + 0.45 * height, 0.35 * width, 0.1 * height))
    rect(screen, (108, 93, 82), (x + 0.17 * width, y + 0.7 * height, 0.7 * width, 0.1 * height))
    rect(screen, (108, 93, 82), (x + 0.44 * width, y + 0.25 * height, 0.14 * width, 0.45 * height))
    circle(screen, (173, 158, 148), (x + 0.51 * width, y + 0.17 * height), 0.12 * height)
    circle(screen, (228, 223, 220), (x + 0.51 * width, y + 0.19 * height), 0.09 * height)
    aaline(screen, (0, 0, 0), [x + 0.42 * width, y + 0.18 * height], [x + 0.46 * width, y + 0.2 * height], 3)
    aaline(screen, (0, 0, 0), [x + 0.58 * width, y + 0.18 * height], [x + 0.54 * width, y + 0.2 * height], 3)
    arc(screen, (0, 0, 0), (x + 0.4 * width, y + 0.23 * height, 0.2 * width, 0.1 * height), 0, np.pi, 2)
    aaline(screen, (0, 0, 0), [x + 0.1 * width, y + 0.4 * width], [x + 0.12 * width, y + 0.91 * width], 2)

def oval(x, y, width, height):
    for j in range(int(500 * width)):
        i = j / 1000
        ellipse(screen, (205, 205, 205), (x + i, y + i * height / width, width - 2 * i, height - 2 * i * height / width), 2)

def cat(x, y, width):
    oval(x + 0.15 * width, y + 0.35 * width, 0.7 * width, 0.3 * width)
    oval(x, y + 0.45 * width, 0.2 * width, 0.1 * width)
    oval(x + 0.2 * width, y + 0.5 * width, 0.1 * width, 0.3 * width)
    oval(x + 0.35 * width, y + 0.5 * width, 0.1 * width, 0.3 * width)
    oval(x + 0.55 * width, y + 0.5 * width, 0.1 * width, 0.3 * width)
    oval(x + 0.7 * width, y + 0.5 * width, 0.1 * width, 0.3 * width)
    circle(screen, (205, 205, 205), (x + 0.81 * width, y + 0.32 * width), 0.04 * width)
    circle(screen, (205, 205, 205), (x + 0.93 * width, y + 0.32 * width), 0.04 * width)
    circle(screen, (205, 205, 205), (x + 0.87 * width, y + 0.42 * width), 0.115 * width)
    circle(screen, (0, 0, 0), (x + 0.84 * width, y + 0.4 * width), 0.015 * width)
    circle(screen, (0, 0, 0), (x + 0.9 * width, y + 0.4 * width),  0.015 * width)
    aaline(screen, (0, 0, 0), [x + 0.83 * width, y + 0.45 * width], [x + 0.91 * width, y + 0.45 * width], 2)

def fish(color, x, y, width, height):
    ellipse(screen, color, (x, y, 0.8 * width, height))
    polygon(screen, color, [(x + 0.8 * width, y + height / 2), (x + width, y), (x + width, y + height), (x + 0.8 * width, y + height / 2)])
    circle(screen, (0, 0, 0), (x + 0.2 * width, y + 0.4 * height), 0.05 * width)

def draw_village():
    screen.fill((230, 230, 230))
    rect(screen, (250, 250, 250), (0, 400, 700, 500))
    igl(30, 380, 150, 125)
    igl(280, 410, 150, 125)
    igl(60, 400, 300, 250)
    igl(30, 500, 200, 166.67)
    igl(170, 540, 200, 166.67)
    man(550, 360, 75, 100)
    man(480, 400, 75, 100)
    man(590, 440, 75, 100)
    man(460, 470, 75, 100)
    man(510, 530, 150, 200)
    cat(220, 600, 200)
    cat(50, 690, 150)
    cat(30, 600, 150)
    fish((0, 0, 255), 550, 730, 100, 30)
    fish((255, 0, 0), 590, 765, 100, 30)
    fish((0, 255, 0), 480, 755, 100, 30)

def t_l(x, y, width, height):
    ellipse(screen, (250, 250, 250), (x, y, width, height))
    ellipse(screen, (0, 0, 0), (x, y, width, height), 2)
    ellipse(screen, (250, 250, 250), (x, y + 0.95 * height, 0.05 * width, 0.05 * height), 2)
    ellipse(screen, (0, 0, 0), (x, y + 0.83 * height, 0.17 * width, 0.17 * height), 2)

def t_r(x, y, width, height):
    ellipse(screen, (250, 250, 250), (x, y, width, height))
    ellipse(screen, (0, 0, 0), (x, y, width, height), 2)
    ellipse(screen, (250, 250, 250), (x + 0.83 * width, y + 0.95 * height, 0.05 * width, 0.05 * height), 2)
    ellipse(screen, (0, 0, 0), (x + 0.83 * width, y + 0.83 * height, 0.17 * width, 0.17 * height), 2)

def t1():
    t_l(420, 600, 210, 70)
    font = pg.font.SysFont(None, 24)
    img = font.render('Вы продоёте рыбов?', True, (0,0,0))
    screen.blit(img, (440, 625))

def t2():
    t_r(350, 520, 210, 60)
    font = pg.font.SysFont(None, 24)
    img = font.render('Нет, только показываем', True, (0,0,0))
    screen.blit(img, (357, 543))

def t3():
    t_l(420, 630, 100, 50)
    font = pg.font.SysFont(None, 24)
    img = font.render('Красивое', True, (0,0,0))
    screen.blit(img, (433, 646))

clock = pg.time.Clock()
finished = False

k = 0
while not finished:
    clock.tick(FPS)
    k = k % 3
    draw_village()
    if k % 3 == 0: 
        t1()
    elif k % 3 == 1:
        t2()
    else:
        t3()
    pg.display.update()
    k += 1
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

pg.quit()