import numpy as np
import random as rn
import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

g = 3
#Ось вращения пушки
x_0 = 20
y_0 = 450
#Параметры пушки
h = 7
l_0 = 5
d = 3

class Ball:
    def __init__(self, screen: pygame.Surface):
        """
        Конструктор класса ball
        """
        self.screen = screen
        self.x = 0
        self.y = 0
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = rn.choice(GAME_COLORS)
        self.live = 150

    def move(self):
        """
        Переместить мяч
        """
        self.live -= 1
        self.x += self.vx
        self.y -= self.vy
        self.vy -= g
        if self.vy > 0 and self.y <= self.r:
            self.vy *= -0.8
        if self.vy < 0 and self.y >= HEIGHT - self.r:
            self.vy *= -0.8
        if self.vx < 0 and self.x <= self.r:
            self.vx *= -0.8
        if self.vx > 0 and self.x >= WIDTH - self.r:
            self.vx *= -0.8

    def draw(self):
        '''
        Рисует снаряд
        '''
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )
        pygame.draw.circle(
            self.screen,
            BLACK,
            (self.x, self.y),
            self.r, 1
        )
        

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (obj.x - self.x) ** 2 + (obj.y - self.y) ** 2 <= (obj.r + self.r) ** 2:
            return True
        else:
            return False

class Shot:
    def __init__(self, screen: pygame.Surface):
        """
        Конструктор класса ball
        """
        self.screen = screen
        self.x = 0
        self.y = 0
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.an = 0
        self.color = rn.choice(GAME_COLORS)
        self.live = 150
        
    def move(self):
        """
        Переместить мяч
        """
        self.live -= 1
        self.x += self.vx
        self.y -= self.vy
        #self.vy -= g
        if self.vy > 0 and self.y <= self.r:
            #self.vy *= -1
            self.live = 0
        if self.vy < 0 and self.y >= HEIGHT - self.r:
            #self.vy *= -1
            self.live = 0
        if self.vx < 0 and self.x <= self.r:
            #self.vx *= -1
            self.live = 0
        if self.vx > 0 and self.x >= WIDTH - self.r:
            #self.vx *= -1
            self.live = 0

    def draw(self):
        '''
        Рисует снаряд
        '''
        l = 5
        d = 1
        k = 2
        pygame.draw.polygon(self.screen, self.color,
        [
            (self.x - d * np.cos(self.an) - 0.5 * h * np.sin(self.an), self.y - d * np.sin(self.an) + 0.5 * h * np.cos(self.an)),
            (self.x - d * np.cos(self.an) + 0.5 * h * np.sin(self.an), self.y - d * np.sin(self.an) - 0.5 * h * np.cos(self.an)),
            (self.x + (l - d) * np.cos(self.an) + 0.5 * h * np.sin(self.an), self.y + (l - d) * np.sin(self.an) - 0.5 * h * np.cos(self.an)),
            (self.x + (l + k) * np.cos(self.an), self.y + (l + k) * np.sin(self.an)),
            (self.x + (l - d) * np.cos(self.an) - 0.5 * h * np.sin(self.an), self.y + (l - d) * np.sin(self.an) + 0.5 * h * np.cos(self.an))
        ])
        pygame.draw.aalines(self.screen, self.color, True,
        [
            (self.x - d * np.cos(self.an) - 0.5 * h * np.sin(self.an), self.y - d * np.sin(self.an) + 0.5 * h * np.cos(self.an)),
            (self.x - d * np.cos(self.an) + 0.5 * h * np.sin(self.an), self.y - d * np.sin(self.an) - 0.5 * h * np.cos(self.an)),
            (self.x + (l - d) * np.cos(self.an) + 0.5 * h * np.sin(self.an), self.y + (l - d) * np.sin(self.an) - 0.5 * h * np.cos(self.an)),
            (self.x + (l + k) * np.cos(self.an), self.y + (l + k) * np.sin(self.an)),
            (self.x + (l - d) * np.cos(self.an) - 0.5 * h * np.sin(self.an), self.y + (l - d) * np.sin(self.an) + 0.5 * h * np.cos(self.an))
        ])
        

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        l = 5
        k = 2
        if (obj.x - (self.x + (l + k) * np.cos(self.an))) ** 2 + (obj.y - (self.y + (l + k) * np.sin(self.an))) ** 2 <= obj.r ** 2:
            return True
        else:
            return False

class Target:
    def __init__(self):
        """ Инициализация новой цели. """
        self.r = rn.randint(10, 50)
        self.x = rn.randint(0.5 * WIDTH, WIDTH - self.r)
        self.y = rn.randint(self.r, HEIGHT - self.r)
        self.vx = rn.randint(0, 10)
        self.vy = rn.randint(0, 10)
        self.color = RED
        self.live = rn.randint(80, 200)

    def move(self):
        '''
        Движение мишени
        '''
        self.x += self.vx
        self.y -= self.vy
        if self.x <= self.r and self.vx < 0:
            self.vx *= -1
        if self.x >= WIDTH - self.r and self.vx > 0:
            self.vx *= -1
        if self.y <= self.r and self.vy > 0:
            self.vy *= -1
        if self.y >= HEIGHT - self.r and self.vy < 0:
            self.vy *= -1
        self.live -= 1

    def draw(self):
        '''
        Рисует мишень
        '''
        pygame.draw.circle(
            screen,
            self.color,
            (self.x, self.y),
            self.r)
        pygame.draw.circle(
            screen,
            BLACK,
            (self.x, self.y),
            self.r, 2)
        pygame.draw.circle(
            screen,
            BLACK,
            (self.x, self.y),
            3)      

class Targ_sin:
    def __init__(self):
        '''
        Конструктор новой мишени
        '''
        self.x = WIDTH
        self.y0 = rn.randint(0, 0.6 * HEIGHT)
        self.y = self.y0
        self.r = rn.randint(15, 30)
        self.phi = rn.randint(0, 360)
        self.phi *= np.pi / 180
        self.a = rn.randint(20, 100)
        if self.a + self.r > self.y0: self.a = 0.5 * (self.y0 - self.r)
        self.w = rn.random() * 0.5
        self.color = rn.choice(GAME_COLORS)
        self.time = rn.randint(50, 100)
        self.live = self.time
        self.vx = rn.randint(10, 30)
        self.vy = self.a * self.w * np.cos(self.w * (self.time - self.live) + self.phi)
    
    def move(self):
        '''
        Двигает мишень
        '''
        self.x -= self.vx
        self.y += self.vy#self.y0 + self.a * np.sin(self.w * self.x - self.phi)
        self.vy = self.a * self.w * np.cos(self.w * (self.time - self.live) + self.phi)
        self.live -= 1
        if self.x < 0: self.x = WIDTH

    def draw(self):
        '''
        Рисует мишень
        '''
        pygame.draw.circle(
            screen, (173, 216, 230), 
            (self.x, self.y), 
            self.r)
        pygame.draw.circle(
            screen, (250,250,210), 
            (self.x, self.y), 
            self.r, 1)

class Gun:
    def __init__(self, screen):
        '''
        Генерация пушки
        '''
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = BLACK
        self.act_col = rn.choice(GAME_COLORS)
        self.button = 0

    def fire2_start(self, event):
        '''
        Индикатор начала накопления энергии пушки
        '''
        self.f2_on = 1

    def power_up(self):
        '''
        Зарядка энергией
        '''
        if self.f2_on:
            if self.f2_power < 60:
                self.f2_power += 0.5
            self.color = self.act_col
        else:
            self.color = BLACK
    
    def fire_ball_end(self, event, bullet):
        """
        Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = np.arctan((event.pos[1] - y_0) / (event.pos[0] - x_0))
        l = l_0 * self.f2_power
        new_ball.x = x_0 + (l - d) * np.cos(self.an)
        new_ball.y = y_0 + (l - d) * np.sin(self.an)
        new_ball.color = self.act_col
        self.an = np.arctan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * np.cos(self.an)
        new_ball.vy = -self.f2_power * np.sin(self.an)
        self.f2_on = 0
        self.f2_power = 10
        return bullet, new_ball

    def fire_shot_end(self, event, bullet, Shots):
        '''
        Выстрел дробью
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        '''
        l = 5
        d = 1
        k = 2
        self.an = np.arctan((event.pos[1] - y_0) / (event.pos[0] - x_0))
        n = int(3 * (1 - np.exp(-3 * self.f2_power))) #int(self.f2_power * 0.1) 
        bullet += 1 + 2 * n
        self.an = np.arctan((event.pos[1] - y_0) / (event.pos[0] - x_0))
        l = l_0 * self.f2_power

        new_shot = Shot(screen)
        new_shot.an = self.an
        new_shot.x = x_0 + (l + k - d) * np.cos(self.an)
        new_shot.y = y_0 + (l + k - d) * np.sin(self.an)
        new_shot.color = self.act_col
        new_shot.vx = self.f2_power * np.cos(new_shot.an)
        new_shot.vy = -self.f2_power * np.sin(new_shot.an)
        Shots.append(new_shot)
        for i in range(1, n, 1):
            new_shot = Shot(screen)
            new_shot.an = self.an + np.pi / (6 * i)
            new_shot.x = x_0 + (l + k - d) * np.cos(self.an)
            new_shot.y = y_0 + (l + k - d) * np.sin(self.an)
            new_shot.color = self.act_col
            new_shot.vx = self.f2_power * np.cos(new_shot.an)
            new_shot.vy = -self.f2_power * np.sin(new_shot.an)
            Shots.append(new_shot)
            new_shot = Shot(screen)
            new_shot.an = self.an - np.pi / (6 * i)
            new_shot.x = x_0 + (l + k - d) * np.cos(self.an)
            new_shot.y = y_0 + (l + k - d) * np.sin(self.an)
            new_shot.color = self.act_col
            new_shot.vx = self.f2_power * np.cos(new_shot.an)
            new_shot.vy = -self.f2_power * np.sin(new_shot.an)
            Shots.append(new_shot)
        self.f2_on = 0
        self.f2_power = 10
        return bullet, shots

    def targetting(self):
        """Прицеливание. Зависит от положения мыши."""
        x, y = pygame.mouse.get_pos()
        self.an = np.arctan((y - y_0) / (x - x_0))

    def draw(self):
        '''
        Рисует пушку
        '''
        x, y = pygame.mouse.get_pos()
        self.an = np.arctan((y - y_0) / (x - x_0))
        l = (l_0 + 10) * self.f2_power / 8
        pygame.draw.polygon(self.screen, self.color,
        [
            (x_0 - d * np.cos(self.an) - 0.5 * h * np.sin(self.an), y_0 - d * np.sin(self.an) + 0.5 * h * np.cos(self.an)),
            (x_0 - d * np.cos(self.an) + 0.5 * h * np.sin(self.an), y_0 - d * np.sin(self.an) - 0.5 * h * np.cos(self.an)),
            (x_0 + (l - d) * np.cos(self.an) + 0.5 * h * np.sin(self.an), y_0 + (l - d) * np.sin(self.an) - 0.5 * h * np.cos(self.an)),
            (x_0 + (l - d) * np.cos(self.an) - 0.5 * h * np.sin(self.an), y_0 + (l - d) * np.sin(self.an) + 0.5 * h * np.cos(self.an))
        ])
        pygame.draw.aalines(self.screen, self.color, True,
        [
            (x_0 - d * np.cos(self.an) - 0.5 * h * np.sin(self.an), y_0 - d * np.sin(self.an) + 0.5 * h * np.cos(self.an)),
            (x_0 - d * np.cos(self.an) + 0.5 * h * np.sin(self.an), y_0 - d * np.sin(self.an) - 0.5 * h * np.cos(self.an)),
            (x_0 + (l - d) * np.cos(self.an) + 0.5 * h * np.sin(self.an), y_0 + (l - d) * np.sin(self.an) - 0.5 * h * np.cos(self.an)),
            (x_0 + (l - d) * np.cos(self.an) - 0.5 * h * np.sin(self.an), y_0 + (l - d) * np.sin(self.an) + 0.5 * h * np.cos(self.an))
        ])

def counter(points):
    '''
    Счетчик очков
    '''
    font = pygame.font.SysFont(None, 30)
    img = font.render(str(points), True, (0, 0, 0))
    screen.blit(img, (0.05 * WIDTH, 0.05 * HEIGHT))

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
points = 0
time_of_pause = 60
balls = []
shots = []
targets = []
targ_sin = []

clock = pygame.time.Clock()
gun = Gun(screen)
finished = False
again = False

while not finished:
    if not again:
        '''
                Отрисовывание всего
        '''
        screen.fill(WHITE)
        counter(points)
        for t in targets:
            t.draw()
        for t_s in targ_sin:
            t_s.draw()
        for b in balls:
            b.draw()
        for sh in shots:
            sh.draw()
        gun.draw()
        pygame.display.update()

        '''
                Анализ действий
        '''
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN and (event.button == 1 or event.button == 3):
                gun.fire2_start(event)
                gun.button = event.button
            elif event.type == pygame.MOUSEBUTTONUP and gun.button == 1:
                bullet, new_ball = gun.fire_ball_end(event, bullet)
                balls.append(new_ball)
                gun.button = 0
            elif event.type == pygame.MOUSEBUTTONUP and gun.button == 3:
                bullet, shots = gun.fire_shot_end(event, bullet, shots)
                gun.button = 0
            elif event.type == pygame.MOUSEMOTION:
                gun.targetting()

        '''
                Движение снарядов и мишеней, удаление лишнего
        '''
        ball_clone = []
        shots_clone = []
        target_clone = []
        targ_sin_clone = []

        for b in balls:
            if b.live > 0:
                b.move()
                ball_clone.append(b)
        balls = ball_clone
        for sh in shots:
            if sh.live > 0:
                sh.move()
                shots_clone.append(sh)
        shots = shots_clone
        for t in targets:
            if t.live > 0:
                t.move()
                target_clone.append(t)
        targets = target_clone
        for t_s in targ_sin:
            if t_s.live > 0:
                t_s.move()
                targ_sin_clone.append(t_s)
        targ_sin = targ_sin_clone


        '''
                Проверка столкновений
        '''
        for b in balls:
            for t in targets:
                if b.hittest(t):
                    points += 1
                    again = True
                    i = 0
                    break
            for t_s in targ_sin:
                if b.hittest(t_s):
                    points += 1
                    again = True
                    i = 0
                    break
        for sh in shots:
            for t in targets:
                if sh.hittest(t):
                    points += 1
                    again = True
                    i = 0
                    break
            for t_s in targ_sin:
                if sh.hittest(t_s):
                    points += 1
                    again = True
                    i = 0
                    break

        '''
                Добавление нужных мишеней
        '''
        if len(targets) < 2:
            targets.append(Target())
        if len(targ_sin) < 2:
            targ_sin.append(Targ_sin())
        gun.power_up()
    
    if again:
        '''
                Всплывашка с результатом игры
        '''
        balls = []
        shots = []
        targets = []
        targ_sin = []
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
        screen.fill(WHITE)
        counter(points)
        font = pygame.font.SysFont(None, 40)
        if bullet % 10 == 1:
            img = font.render('Вы уничтожили цель за ' + str(bullet) + ' выстрел', True, (0, 0, 0))
        elif bullet % 10 > 1 and points % 10 < 5:
            img = font.render('Вы уничтожили цель за ' + str(bullet) + ' выстрела', True, (0, 0, 0))
        elif bullet % 10 > 4 or bullet % 10 == 0:
            img = font.render('Вы уничтожили цель за ' + str(bullet) + ' выстрелов', True, (0, 0, 0))
        screen.blit(img, (0.2 * WIDTH, 0.45 * HEIGHT))
        pygame.display.update()
        i += 1
        if i >= time_of_pause:
            again = False
            bullet = 0

pygame.quit()
