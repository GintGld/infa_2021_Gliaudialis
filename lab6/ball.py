from os import X_OK
import pygame as pg
import numpy as np
from pygame.constants import BLEND_ALPHA_SDL2, K_SPACE, KEYDOWN
from pygame.draw import *
from random import randint
from random import random
pg.init()

FPS = 30
dt = 0.2
width = 900
height = 700
vmax = 20
points = 0
min_balls = 4
min_tr_s = 4
min_r = 20
max_r = 50
max_w = 1
k = 4

screen = pg.display.set_mode((width, height))

def start_menu():
    '''
    Вступительное меню
    '''
    font = pg.font.SysFont(None, 20)
    img = font.render('Нажмите в любом месте, чтобы начать', True, (255, 255, 255))
    screen.blit(img, (0.35 * width, 0.5 * height))

def finish_menu(a, b, c, d, e, p):
    '''
    Заключительное меню
    '''
    screen.fill((0, 0, 0))
    font = pg.font.SysFont(None, 20)
    img = font.render('Конец, нажмите в любом месте, чтобы выйти', True, (255, 255, 255))
    screen.blit(img, (0.35 * width, 0.05 * height))
    img = font.render('Ваш результат:', True, (255, 255, 255))
    screen.blit(img, (0.43 * width, 0.1 * height))
    img = font.render(str(p), True, (255, 255, 255))
    screen.blit(img, (0.55 * width, 0.1 * height))
    img = font.render('Лучшие результаты', True, (255, 255, 255))
    screen.blit(img, (0.43 * width, 0.15 * height))
    img = font.render(str(a), True, (255, 255, 255))
    screen.blit(img, (0.5 * width, 0.2 * height))
    img = font.render(str(b), True, (255, 255, 255))
    screen.blit(img, (0.5 * width, 0.25 * height))
    img = font.render(str(c), True, (255, 255, 255))
    screen.blit(img, (0.5 * width, 0.3 * height))
    img = font.render(str(d), True, (255, 255, 255))
    screen.blit(img, (0.5 * width, 0.35 * height))
    img = font.render(str(e), True, (255, 255, 255))
    screen.blit(img, (0.5 * width, 0.4 * height))
    
def counter(points):
    '''
    Счетчик
    '''
    font = pg.font.SysFont(None, 50)
    img = font.render(str(int(points)), True, (255, 255, 255))
    screen.blit(img, (0.6 * width, 0.05 * height))

def timer(time):
    '''
    Таймер
    '''
    font = pg.font.SysFont(None, 50)
    s = str(round(time, 3))
    while len(s) < 5: s += '0'
    img = font.render(s, True, (255, 255, 255))
    screen.blit(img, (0.35 * width, 0.05 * height))

def draw_backgrownd(time, points):
    '''
    Счетчик и таймер
    '''
    counter(points)
    timer(time)

def tr_decrease(tr):
    tr['r'] = tr['r0'] * (1 - tr['time'] / tr['time_of_life'])
    tr['w'] = tr['w0'] * (tr['r0'] / tr['r']) ** 2
    return tr

def create_ball():
    '''
    Рисует новый шарик
    '''
    r = randint(min_r, max_r)
    x = randint(r, width - r)
    y = randint(r, height - r)
    vx = randint(-vmax, vmax)
    vy = randint(-vmax, vmax)
    time_of_life = randint(50, 100)
    circle(screen,  (randint(0, 255), randint(0, 255), randint(0, 255)) , (x, y), r)
    ball = {
        'x' : x,
        'y' : y,
        'r' : r,
        'c' : (randint(0, 255), randint(0, 255), randint(0, 255)),
        'vx' : vx,
        'vy' : vy,
        'time' : 0,
        'time_of_life' : time_of_life
    }
    return ball

def create_tr():
    '''
    Рисует новый трегульник Рело
    '''
    r = randint(1.5 * min_r, 1.5 * max_r)
    x = randint(r, width - r)
    y = randint(r, height - r)
    w = 2 * (random() - 0.5) * max_w
    phi = random() * 2 * np.pi / 3
    vx = randint(-vmax, vmax)
    vy = randint(-vmax, vmax)
    time_of_life = randint(50, 100)
    tr = {
        'x' : x,
        'y' : y,
        'r0' : r,
        'r' : r,
        'c' : (randint(0, 255), randint(0, 255), randint(0, 255)),
        'w0' : w,
        'w' : w,
        'phi' : phi,
        'vx' : vx,
        'vy' : vy,
        'time' : 0,
        'time_of_life' : time_of_life
    }
    draw_tr(tr)
    return tr

def draw_line_of_tr(tr):
    '''
    Рисует Треугольник Рело
    '''
    arc(screen, tr['c'], 
        (tr['x'] + tr['r'] * np.sin(tr['phi']) - tr['r'] * np.sqrt(3), tr['y'] - tr['r'] * np.cos(tr['phi']) - tr['r'] * np.sqrt(3),
        2 * tr['r'] * np.sqrt(3), 2 * tr['r'] * np.sqrt(3)), 
        -2 * np.pi / 3 - tr['phi'], - np.pi / 3 - tr['phi'], 3)
    arc(screen, tr['c'],
        (tr['x'] + tr['r'] * np.sin(tr['phi'] + 2 * np.pi / 3) - tr['r'] * np.sqrt(3), tr['y'] - tr['r'] * np.cos(tr['phi'] + 2 * np.pi / 3) - tr['r'] * np.sqrt(3), 
        2 * tr['r'] * np.sqrt(3), 2 * tr['r'] * np.sqrt(3)),
        2 * np.pi / 3 - tr['phi'], np.pi - tr['phi'], 3)
    arc(screen, tr['c'],
        (tr['x'] + tr['r'] * np.sin(tr['phi'] + 4 * np.pi / 3) - tr['r'] * np.sqrt(3), tr['y'] - tr['r'] * np.cos(tr['phi'] + 4 * np.pi / 3) - tr['r'] * np.sqrt(3),
        2 * tr['r'] * np.sqrt(3), 2 * tr['r'] * np.sqrt(3)),
        -tr['phi'], np.pi / 3 - tr['phi'], 3)

def draw_tr(tr):
    '''
    Рисует треугольник Рело.
    Изображая подобные концетричесакие треугольники Рело
    с разными радиусами закрашиваю его
    '''
    for i in range(0, int(k * tr['r']), 1):
        tr1 = {
            'x' : tr['x'],
            'y' : tr['y'],
            'r' : i / k,
            'c' : tr['c'],
            'w' : tr['w'],
            'phi' : tr['phi'],
        }
        draw_line_of_tr(tr1)

def strike_ball(ball):
    '''
    Отражение шарика
    '''
    if ball['x'] <= ball['r'] and ball['vx'] < 0:
        ball['vx'] *= -1
    if ball['x'] >= width - ball['r'] and ball['vx'] > 0:
        ball['vx'] *= -1
    if ball['y'] <= ball['r'] and ball['vy'] < 0:
        ball['vy'] *= -1
    if ball['y'] >= height - ball['r'] and ball['vy'] > 0:
        ball['vy'] *= -1
    return ball

def strike_tr(tr):
    '''
    Отражение треугольника
    При столкновении меняется не только линейная скорость,
    но и угловая на противоположную
    '''
    if tr['x'] <= tr['r'] and tr['vx'] < 0:
        tr['vx'] *= -1
        tr['w'] *= -1
    if tr['x'] >= width - tr['r'] and tr['vx'] > 0:
        tr['vx'] *= -1
        tr['w'] *= -1
    if tr['y'] <= tr['r'] and tr['vy'] < 0:
        tr['vy'] *= -1
        tr['w'] *= -1
    if tr['y'] >= height - tr['r'] and tr['vy'] > 0:
        tr['vy'] *= -1
        tr['w'] *= -1
    return tr

def move_ball(dt, ball):
    '''
    Двигает шарик за dt
    '''
    ball = strike_ball(ball)
    ball['x'] += dt * ball['vx']
    ball['y'] += dt * ball['vy']
    ball['time'] += 1
    return ball

def move_tr(dt, tr):
    '''
    Двигает треугольник за dt
    '''
    tr = strike_tr(tr)
    tr = tr_decrease(tr)
    tr['x'] += dt * tr['vx']
    tr['y'] += dt * tr['vy']
    tr['phi'] += dt * tr['w']
    tr['time'] += 1
    return tr

def click(event):
    '''
    Возврат координат клика
    '''
    (x, y) = event.pos
    return x, y

def is_point_in_tr(x, y, tr):
    counter = 0
    rho_1 = (tr['x'] + tr['r'] * np.sin(tr['phi']) - x) ** 2 + (tr['y'] - tr['r'] * np.cos(tr['phi']) - y) ** 2
    rho_2 =  (tr['x'] + tr['r'] * np.sin(tr['phi'] + 2 * np.pi / 3) - x) ** 2 + (tr['y'] - tr['r'] * np.cos(tr['phi'] + 2 * np.pi / 3) - y) ** 2
    rho_3 = (tr['x'] + tr['r'] * np.sin(tr['phi'] + 4 * np.pi / 3) - x) ** 2 + (tr['y'] - tr['r'] * np.cos(tr['phi'] + 4 * np.pi / 3) - y) ** 2
    if rho_1 <= 3 * tr['r'] ** 2:
        counter += 1
    if rho_2 <= 3 * tr['r'] ** 2:
        counter += 1
    if rho_3 <= 3 * tr['r'] ** 2:
        counter += 1
    if counter == 3:
        return True
    else:
        return False

#pg.display.update()
clock = pg.time.Clock()
finished = False
balls = []
tr_s = []
menu = False
time = 7
pause = False

while not menu:
    start_menu()
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        elif event.type == pg.MOUSEBUTTONDOWN:
            menu = True


while not finished and time > 0 :
    clock.tick(FPS)
    ball_to_del = []
    tr_to_del = []
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        elif event.type == KEYDOWN and event.key == K_SPACE:
            pause = not pause
        elif event.type == pg.MOUSEBUTTONDOWN:
            (cl_x, cl_y) = click(event)
            for ball in balls:
                if (cl_x - ball['x']) ** 2 + (cl_y - ball['y']) ** 2 <= ball['r'] ** 2:
                    points += 1
                    ball_to_del.append(ball)
            for tr in tr_s:
                if is_point_in_tr(cl_x, cl_y, tr) == True:
                    points += tr['r0'] / tr['r']
                    tr_to_del.append(tr)
    balls_clone = []
    tr_s_clone = []
    screen.fill((0, 0, 0))
    for ball in balls:
        if ball['time'] < ball['time_of_life'] and ball not in ball_to_del:
            if not pause:
                ball = move_ball(dt, ball)
            circle(screen, ball['c'], (ball['x'], ball['y']), ball['r'])
            balls_clone.append(ball)
    for tr in tr_s:
        if tr['time'] < tr['time_of_life'] and tr not in tr_to_del and tr['r'] > 10:
            if not pause:
                tr = move_tr(dt, tr)
            draw_tr(tr)
            tr_s_clone.append(tr)
    balls = balls_clone
    tr_s = tr_s_clone
    if len(balls) < min_balls:
        ball = create_ball()
        balls.append(ball)
    if len(tr_s) < min_tr_s:
        tr = create_tr()
        tr_s.append(tr)
    draw_backgrownd(time, points)
    time -= 1 / 30
    pg.display.update()

menu = False
inp = open(r'C:\Users\coolg\Desktop\top.txt', 'r')
s = inp.readlines()
a = []
for i in s:
    a.append(int(i.rstrip()))
a.append(int(points))
a.sort()
inp.close()
print(a)
out = open(r'C:\Users\coolg\Desktop\top.txt', 'w')
print(a[5], file=out)
print(a[4], file=out)
print(a[3], file=out)
print(a[2], file=out)
print(a[1], file=out)
out.close()
while not menu:
    finish_menu(a[5], a[4], a[3], a[2], a[1], int(points))
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            menu = True
        elif event.type == pg.MOUSEBUTTONDOWN:
            menu = True

pg.quit()