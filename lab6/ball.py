from os import X_OK
import pygame as pg
import numpy as np
from pygame.constants import BLEND_ALPHA_SDL2, K_SPACE, KEYDOWN
from pygame.draw import *
from random import randint
from random import random
pg.init()

'''
Константы
'''
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

clock = pg.time.Clock()
menu = False
time = 1
pause = False
end = False
rate = False

screen = pg.display.set_mode((width, height))
surface1 = pg.Surface((0.107 * width, 0.048 * height), pg.SRCALPHA)
surface2 = pg.Surface((0.17 * width, 0.096 * height), pg.SRCALPHA)
surface3 = pg.Surface((0.134 * width, 0.048 * height), pg.SRCALPHA)
surface4 = pg.Surface((0.134 * width, 0.048 * height), pg.SRCALPHA)

def is_mouse_in_start_box(x, y):
    '''
    Находится ли мышь на кнопке старт
    '''
    if (x - 0.45 * width) * (x - 0.557 * width) <= 0 and (y - 0.405 * height) * (y - 0.453 * height) <= 0:
        return True
    else:
        return False

def is_mouse_in_rate_box(x, y):
    if (x - 0.418 * width) * (x - 0.588 * width) <= 0 and (y - 0.48 * height) * (y - 0.576 * height) <= 0:
        return True
    else:
        return False

def is_mouse_in_out_box(x, y):
    '''
    Находится ли мышь на кнопке выход/меню
    '''
    if (x - 0.437 * width) * (x - 0.571 * width) <= 0 and (y - 0.6 * height) * (y - 0.648 * height) <= 0:
        return True
    else:
        return False
    
def game_menu(rate, a, points):
    '''
    Меню
    '''
    x, y = pg.mouse.get_pos()
    if not rate:
        screen.fill((0, 0, 0))
        font = pg.font.SysFont(None, 70)

        img_name = font.render('Лучшая игра', True, (255, 255, 255))
        screen.blit(img_name, (0.33 * width, 0.2 * height))

        font = pg.font.SysFont(None, 50)
        if is_mouse_in_start_box(x, y):
            surface1.fill((205, 115, 0))
        else:
            surface1.fill((255, 165, 0))
        if is_mouse_in_rate_box(x, y):
            surface2.fill((205, 115, 0))
        else:
            surface2.fill((255, 165, 0))
        if is_mouse_in_out_box(x, y):
            surface3.fill((205, 115, 0))
        else:
            surface3.fill((255, 165, 0))
        img = font.render('Старт', True, (255, 255, 255))
        screen.blit(surface1, (0.45 * width, 0.405 * height))
        screen.blit(img, (0.45 * width, 0.4 * height))

        img1 = font.render('Таблица', True, (255, 255, 255))
        img11 = font.render('лидеров', True, (255, 255, 255))
        screen.blit(surface2, (0.418 * width, 0.48 * height))
        screen.blit(img1, (0.425 * width, 0.48 * height))
        screen.blit(img11, (0.42 * width, 0.52 * height))

        img2 = font.render('Выход', True, (255, 255, 255))
        screen.blit(surface3, (0.437 * width, 0.6 * height))
        screen.blit(img2, (0.437 * width, 0.6 * height))
    else:
        screen.fill((0, 0, 0))
        font = pg.font.SysFont(None, 50)

        if points >= 0:
            img_my_res = font.render('Ваш результат: ' + str(points), True, (255, 255, 255))
            screen.blit(img_my_res, (0.35 * width, 0.05 * height))
        
        img = font.render('Лучшие результаты', True, (255, 255, 255))
        screen.blit(img, (0.33 * width, 0.15 * height))

        img = font.render(str(a[5]), True, (255, 255, 255))
        screen.blit(img, (0.48 * width, 0.24 * height))

        img = font.render(str(a[4]), True, (255, 255, 255))
        screen.blit(img, (0.48 * width, 0.31 * height))

        img = font.render(str(a[3]), True, (255, 255, 255))
        screen.blit(img, (0.48 * width, 0.38 * height))

        img = font.render(str(a[2]), True, (255, 255, 255))
        screen.blit(img, (0.48 * width, 0.45 * height))

        img = font.render(str(a[1]), True, (255, 255, 255))
        screen.blit(img, (0.48 * width, 0.52 * height))

        img3 = font.render('Меню', True, (255, 255, 255))
        if is_mouse_in_out_box(x, y):
            surface4.fill((205, 115, 0))
        else:
            surface4.fill((255, 165, 0))
        screen.blit(surface4, (0.437 * width, 0.6 * height))
        screen.blit(img3, (0.45 * width, 0.6 * height))

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

def draw_pause():
    '''
    Рисует паузу
    '''
    font = pg.font.SysFont(None, 20)
    img = font.render('Пауза. Нажмите пробел, чтобы продолжить', True, (255, 255, 255))
    screen.blit(img, (0.35 * width, 0.5 * height))

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
    '''
    Проверка того, находится ли 
    место клика в треугольнике
    '''
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

def start(menu, rate, finished):
    '''
    Начало игры
    меню и таюлица лидеров
    '''
    while not menu:
        clock.tick(FPS)
        if not rate:
            a = [0] * 6
        game_menu(rate, a, -1)
        pg.display.update()
        '''
        Кнопки
        '''
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                (cl_x, cl_y) = click(event)
                if is_mouse_in_start_box(cl_x, cl_y):
                    menu = True
                if is_mouse_in_rate_box(cl_x, cl_y):
                    rate = True
                    inp = open(r'C:\Users\coolg\infa_2021_Gliaudialis\lab6\top.txt', 'r')
                    s = inp.readlines()
                    a = []
                    for i in s:
                        a.append(int(i.rstrip()))
                    a.append(0)
                    a.sort()
                    inp.close()
                if is_mouse_in_out_box(cl_x, cl_y) and not rate:
                    finished = True
                    menu = True
                if is_mouse_in_out_box(cl_x, cl_y) and rate:
                    rate = False
    return menu, rate, finished

def game(finished, time, points, balls, tr_s):
    '''
    Тело игры
    тут проходит сама игра
    '''
    pause = False
    while not finished and time > 0:
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
                    if (cl_x - ball['x']) ** 2 + (cl_y - ball['y']) ** 2 <= ball['r'] ** 2 and not pause:
                        points += 1
                        ball_to_del.append(ball)
                for tr in tr_s:
                    if is_point_in_tr(cl_x, cl_y, tr) == True and not pause:
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
        if not pause:
            draw_backgrownd(time, points)
        else:
            draw_pause()
        if not pause:
            time -= 1 / FPS
        pg.display.update()
    return finished, points, time

def endgame(finished, points, menu):
    '''
    Конец игры
    Результат игры и таблица лидеров
    '''
    while not finished and not menu:
        clock.tick(FPS)
        #finish_menu(a[5], a[4], a[3], a[2], a[1], int(points))
        fin = points
        rate = True
        game_menu(rate, a, fin)
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                menu = True
            elif event.type == pg.MOUSEBUTTONDOWN:
                (cl_x, cl_y) = click(event)
                if is_mouse_in_out_box(cl_x, cl_y) and rate:
                    rate = False
                    menu = True

fin = False
men = False
while not fin:
    '''
    Основной цикл
    '''
    men, rate, fin = start(menu = men, rate = False, finished = fin)
    fin, points, time = game(finished = fin, time = 1, points = 0, balls = [], tr_s = [])
    if time <= 0: #Костыль для выходного меню
        fin = False
        men = False
    inp = open(r'C:\Users\coolg\infa_2021_Gliaudialis\lab6\top.txt', 'r')
    s = inp.readlines()
    a = []
    for i in s:
        a.append(int(i.rstrip()))
    a.append(int(points))
    a.sort()
    inp.close()
    out = open(r'C:\Users\coolg\infa_2021_Gliaudialis\lab6\top.txt', 'w')
    print(a[5], file=out)
    print(a[4], file=out)
    print(a[3], file=out)
    print(a[2], file=out)
    print(a[1], file=out)
    out.close()
    endgame(fin, points, men)

pg.quit()