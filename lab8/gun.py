import numpy as np
import random as rn
import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x234F1E
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600
Grass = 455

#Ускорение свободного падения
g = 3
#Параметры пушки
h = 7
l_0 = 6
d = 3

class Ball:
    def __init__(self, screen: pygame.Surface):
        """
        Конструктор класса ball
        """
        self.screen = screen
        self.x = 0
        self.y = 0
        self.r = 5
        self.vx = 0
        self.vy = 0
        self.color = rn.choice(GAME_COLORS)
        self.live = 50
        self.bottom = 0

    def move(self):
        """
        Переместить мяч
        """
        self.live -= 1
        self.x += self.vx
        self.y -= self.vy
        self.vy -= g
        if self.vy > 0 and self.y <= self.r:
            self.vy *= -0.6
        if self.vy < 0 and self.y >= self.bottom: #HEIGHT - self.r:
            self.vy *= -0.6
        if self.vx < 0 and self.x <= self.r:
            self.vx *= -0.6
        if self.vx > 0 and self.x >= WIDTH - self.r:
            self.vx *= -0.6

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
        if obj.type != 'air':
            if (obj.x - self.x) ** 2 + (obj.y - self.y) ** 2 <= (obj.r + self.r) ** 2:
                return True
            else:
                return False
        if obj.type == 'air':
            if (obj.x - obj.l - self.x) ** 2 + (obj.y - self.y) ** 2 <= self.r ** 2:
                return True
            elif (obj.x - obj.l1 - self.x) ** 2 + (obj.y - obj.d - self.y) ** 2 <= self.r ** 2:
                return True
            elif (obj.x + 2 * obj.q - self.x) ** 2 + (obj.y - obj.h - self.y) ** 2 <= self.r ** 2:
                return True
            elif (obj.x + obj.l2 + 3 * obj.q - self.x) ** 2 + (obj.y - obj.h1 - self.y) ** 2 <= self.r ** 2:
                return True
            elif (obj.x + obj.l2 - self.x) ** 2 + (obj.y + obj.d - self.y) ** 2 <= self.r ** 2:
                return True
            elif (obj.x - obj.q - self.x) ** 2 + (obj.y + obj.h - self.y) ** 2 <= self.r ** 2:
                return True
            elif (obj.x - obj.l1 - self.x) ** 2 + (obj.y + obj.d - self.y) ** 2 <= self.r ** 2:
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
        self.l = 5
        self.d = 1
        self.k = 2
        self.h = 7
        
    def move(self):
        """
        Переместить мяч
        """
        self.live -= 1
        self.x += self.vx
        self.y -= self.vy
        if self.vy > 0 and self.y <= self.r:
            self.live = 0
        if self.vy < 0 and self.y >= HEIGHT - self.r:
            self.live = 0
        if self.vx < 0 and self.x <= self.r:
            self.live = 0
        if self.vx > 0 and self.x >= WIDTH - self.r:
            self.live = 0

    def draw(self):
        '''
        Рисует снаряд
        '''
        pygame.draw.polygon(self.screen, self.color,
        [
            (self.x - self.d * np.cos(self.an) - 0.5 * self.h * np.sin(self.an), self.y - self.d * np.sin(self.an) + 0.5 * self.h * np.cos(self.an)),
            (self.x - self.d * np.cos(self.an) + 0.5 * self.h * np.sin(self.an), self.y - self.d * np.sin(self.an) - 0.5 * self.h * np.cos(self.an)),
            (self.x + (self.l - self.d) * np.cos(self.an) + 0.5 * self.h * np.sin(self.an), self.y + (self.l - self.d) * np.sin(self.an) - 0.5 * self.h * np.cos(self.an)),
            (self.x + (self.l + self.k) * np.cos(self.an), self.y + (self.l + self.k) * np.sin(self.an)),
            (self.x + (self.l - self.d) * np.cos(self.an) - 0.5 * self.h * np.sin(self.an), self.y + (self.l - self.d) * np.sin(self.an) + 0.5 * self.h * np.cos(self.an))
        ])
        pygame.draw.aalines(self.screen, self.color, True,
        [
            (self.x - self.d * np.cos(self.an) - 0.5 * self.h * np.sin(self.an), self.y - self.d * np.sin(self.an) + 0.5 * self.h * np.cos(self.an)),
            (self.x - self.d * np.cos(self.an) + 0.5 * self.h * np.sin(self.an), self.y - self.d * np.sin(self.an) - 0.5 * self.h * np.cos(self.an)),
            (self.x + (self.l - self.d) * np.cos(self.an) + 0.5 * self.h * np.sin(self.an), self.y + (self.l - self.d) * np.sin(self.an) - 0.5 * self.h * np.cos(self.an)),
            (self.x + (self.l + self.k) * np.cos(self.an), self.y + (self.l + self.k) * np.sin(self.an)),
            (self.x + (self.l - self.d) * np.cos(self.an) - 0.5 * self.h * np.sin(self.an), self.y + (self.l - self.d) * np.sin(self.an) + 0.5 * self.h * np.cos(self.an))
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
        if obj.type != 'air':
            if (obj.x - (self.x + (self.l + self.k) * np.cos(self.an))) ** 2 + (obj.y - (self.y + (self.l + self.k) * np.sin(self.an))) ** 2 <= obj.r ** 2:
                return True
            else:
                return False
        if obj.type == 'air':
            if (obj.x - obj.l - (self.x + (self.l + self.k) * np.cos(self.an))) ** 2 + (obj.y - (self.y + (self.l + self.k) * np.sin(self.an))) ** 2 <= self.r ** 2:
                return True
            elif (obj.x - obj.l1 - (self.x + (self.l + self.k) * np.cos(self.an))) ** 2 + (obj.y - obj.d - (self.y + (self.l + self.k) * np.sin(self.an))) ** 2 <= self.r ** 2:
                return True
            elif (obj.x + 2 * obj.q - (self.x + (self.l + self.k) * np.cos(self.an))) ** 2 + (obj.y - obj.h - (self.y + (self.l + self.k) * np.sin(self.an))) ** 2 <= self.r ** 2:
                return True
            elif (obj.x + obj.l2 + 3 * obj.q - (self.x + (self.l + self.k) * np.cos(self.an))) ** 2 + (obj.y - obj.h1 - (self.y + (self.l + self.k) * np.sin(self.an))) ** 2 <= self.r ** 2:
                return True
            elif (obj.x + obj.l2 - (self.x + (self.l + self.k) * np.cos(self.an))) ** 2 + (obj.y + obj.d - (self.y + (self.l + self.k) * np.sin(self.an))) ** 2 <= self.r ** 2:
                return True
            elif (obj.x - obj.q - (self.x + (self.l + self.k) * np.cos(self.an))) ** 2 + (obj.y + obj.h - (self.y + (self.l + self.k) * np.sin(self.an))) ** 2 <= self.r ** 2:
                return True
            elif (obj.x - obj.l1 - (self.x + (self.l + self.k) * np.cos(self.an))) ** 2 + (obj.y + obj.d - (self.y + (self.l + self.k) * np.sin(self.an))) ** 2 <= self.r ** 2:
                return True
            else:
                return False

class Bomb:
    def __init__(self, screen: pygame.Surface):
        """
        Конструктор класса bomb
        """
        self.screen = screen
        self.x = 0
        self.y = 0
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.an = 0
        self.color = BLACK
        self.live = 150
        self.l = 10
        self.d = 2
        self.k = 8
        self.h = 14
        
    def move(self):
        """
        Переместить мяч
        """
        #self.live -= 1
        self.vy -= 3
        self.x += self.vx
        self.y -= self.vy
        if self.vy > 0 and self.y <= self.r:
            self.live = 0
        if self.vy < 0 and self.y >= HEIGHT - self.r:
            self.live = 0
        #if self.vx < 0 and self.x <= self.r:
        #    self.live = 0
        #if self.vx > 0 and self.x >= WIDTH - self.r:
        #    self.live = 0

    def draw(self):
        '''
        Рисует снаряд
        '''
        if self.vy > 0 and self.vx > 0:
            self.an = np.arctan((self.vy) / (self.vx))
        if self.vy <= 0 and self.vx < 0:
            self.an = np.arctan((-self.vy) / (self.vx)) - np.pi
        if self.vy <= 0 and self.vx > 0:
            self.an = np.arctan((-self.vy) / (self.vx))

        pygame.draw.polygon(self.screen, self.color,
        [
            (self.x - self.d * np.cos(self.an) - 0.5 * self.h * np.sin(self.an), self.y - self.d * np.sin(self.an) + 0.5 * self.h * np.cos(self.an)),
            (self.x - self.d * np.cos(self.an) + 0.5 * self.h * np.sin(self.an), self.y - self.d * np.sin(self.an) - 0.5 * self.h * np.cos(self.an)),
            (self.x + (self.l - self.d) * np.cos(self.an) + 0.5 * self.h * np.sin(self.an), self.y + (self.l - self.d) * np.sin(self.an) - 0.5 * self.h * np.cos(self.an)),
            (self.x + (self.l + self.k) * np.cos(self.an), self.y + (self.l + self.k) * np.sin(self.an)),
            (self.x + (self.l - self.d) * np.cos(self.an) - 0.5 * self.h * np.sin(self.an), self.y + (self.l - self.d) * np.sin(self.an) + 0.5 * self.h * np.cos(self.an))
        ])
        pygame.draw.aalines(self.screen, self.color, True,
        [
            (self.x - self.d * np.cos(self.an) - 0.5 * self.h * np.sin(self.an), self.y - self.d * np.sin(self.an) + 0.5 * self.h * np.cos(self.an)),
            (self.x - self.d * np.cos(self.an) + 0.5 * self.h * np.sin(self.an), self.y - self.d * np.sin(self.an) - 0.5 * self.h * np.cos(self.an)),
            (self.x + (self.l - self.d) * np.cos(self.an) + 0.5 * self.h * np.sin(self.an), self.y + (self.l - self.d) * np.sin(self.an) - 0.5 * self.h * np.cos(self.an)),
            (self.x + (self.l + self.k) * np.cos(self.an), self.y + (self.l + self.k) * np.sin(self.an)),
            (self.x + (self.l - self.d) * np.cos(self.an) - 0.5 * self.h * np.sin(self.an), self.y + (self.l - self.d) * np.sin(self.an) + 0.5 * self.h * np.cos(self.an))
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
        if obj.type != 'air':
            if (obj.x - (self.x + (self.l + self.k) * np.cos(self.an))) ** 2 + (obj.y - (self.y + (self.l + self.k) * np.sin(self.an))) ** 2 <= obj.r ** 2:
                return True
            else:
                return False
        if obj.type == 'air':
            if (obj.x - obj.l - (self.x + (self.l + self.k) * np.cos(self.an))) ** 2 + (obj.y - (self.y + (self.l + self.k) * np.sin(self.an))) ** 2 <= self.r ** 2:
                return True
            elif (obj.x - obj.l1 - (self.x + (self.l + self.k) * np.cos(self.an))) ** 2 + (obj.y - obj.d - (self.y + (self.l + self.k) * np.sin(self.an))) ** 2 <= self.r ** 2:
                return True
            elif (obj.x + 2 * obj.q - (self.x + (self.l + self.k) * np.cos(self.an))) ** 2 + (obj.y - obj.h - (self.y + (self.l + self.k) * np.sin(self.an))) ** 2 <= self.r ** 2:
                return True
            elif (obj.x + obj.l2 + 3 * obj.q - (self.x + (self.l + self.k) * np.cos(self.an))) ** 2 + (obj.y - obj.h1 - (self.y + (self.l + self.k) * np.sin(self.an))) ** 2 <= self.r ** 2:
                return True
            elif (obj.x + obj.l2 - (self.x + (self.l + self.k) * np.cos(self.an))) ** 2 + (obj.y + obj.d - (self.y + (self.l + self.k) * np.sin(self.an))) ** 2 <= self.r ** 2:
                return True
            elif (obj.x - obj.q - (self.x + (self.l + self.k) * np.cos(self.an))) ** 2 + (obj.y + obj.h - (self.y + (self.l + self.k) * np.sin(self.an))) ** 2 <= self.r ** 2:
                return True
            elif (obj.x - obj.l1 - (self.x + (self.l + self.k) * np.cos(self.an))) ** 2 + (obj.y + obj.d - (self.y + (self.l + self.k) * np.sin(self.an))) ** 2 <= self.r ** 2:
                return True
            else:
                return False

class Target:
    def __init__(self):
        """ Инициализация новой цели. """
        self.type = 'targ'
        self.r = rn.randint(10, 40)
        self.x = rn.randint(0.5 * WIDTH, WIDTH - self.r)
        self.y = rn.randint(self.r, Grass - self.r)
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
        if self.y >= Grass - self.r and self.vy < 0:
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
        self.type = 'targ_sin'
        self.x = WIDTH
        self.y0 = rn.randint(0, 0.4 * HEIGHT)
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

class Airplane:
    def __init__(self):
        self.screen = screen
        self.type = 'air'
        self.vect = rn.choice([-1, 1])
        self.k = rn.randint(10, 20) * 0.1
        self.l = 24 * self.vect * self.k
        self.l1 = 17 * self.vect * self.k
        self.d = 5 * self.k #* self.vect
        self.q = 4 * self.vect * self.k
        self.h = 18 * self.k #* self.vect
        self.l2 = 24 * self.vect * self.k
        self.h1 = 18 * self.k #* self.vect
        self.color = 0xD21404
        if self.vect == 1:
            self.x0 = WIDTH + self.l
        if self.vect == -1:
            self.x0 = -self.l
        self.y0 = rn.random() * (0.5 * Grass - self.h) + (0.5 * Grass + self.h) / 2
        self.vx = rn.randint(5, 15) * self.vect
        self.x = self.x0
        self.y = self.y0
        self.live = 1
        self.time_to_bomb = 60

    def move(self):
        self.x -= self.vx
        self.time_to_bomb -= 1

    def draw(self):
        pygame.draw.polygon(self.screen, self.color, 
        [
            (self.x - self.l, self.y),
            (self.x - self.l1, self.y - self.d),
            (self.x - self.q, self.y - self.d),
            (self.x + 2 * self.q, self.y - self.h),
            (self.x + self.q, self.y - self.d),
            (self.x + self.l2, self.y - self.d),
            (self.x + self.l2 + 3 * self.q, self.y - self.h1),
            (self.x + self.l2, self.y + self.d),
            (self.x, self.y + self.d),
            (self.x - self.q, self.y + self.h),
            (self.x - 2 * self.q, self.y + self.d),
            (self.x - self.l1, self.y + self.d)
        ])
        pygame.draw.aalines(screen, self.color, True, 
        [
            (self.x - self.l, self.y),
            (self.x - self.l1, self.y - self.d),
            (self.x - self.q, self.y - self.d),
            (self.x + 2 * self.q, self.y - self.h),
            (self.x + self.q, self.y - self.d),
            (self.x + self.l2, self.y - self.d),
            (self.x + self.l2 + 3 * self.q, self.y - self.h1),
            (self.x + self.l2, self.y + self.d),
            (self.x, self.y + self.d),
            (self.x - self.q, self.y + self.h),
            (self.x - 2 * self.q, self.y + self.d),
            (self.x - self.l1, self.y + self.d),
            (self.x - self.l, self.y)
        ])

class Gun:
    def __init__(self, screen):
        '''
        Генерация пушки
        '''
        self.screen = screen
        self.type = 'gun'
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = BLACK
        self.act_col = rn.choice(GAME_COLORS)
        self.button = 0
        self.x0 = 80
        self.y0 = 450
        self.vx = 3
        self.vy = 3
        self.x = self.x0
        self.y = self.y0

    def move(self, v_v, v_h):
        '''
        Двигает пушку
        '''
        if self.x >= 6 * h and self.x <= WIDTH - 6 * h:
            self.x += v_h * self.vx
        elif self.x < 6 * h: self.x = 6 * h
        elif self.x > WIDTH - 6 * h: self.x = WIDTH - 6 * h
        if self.y >= Grass - 6 * d and self.y <= HEIGHT - 6 * d:
            self.y += v_v * self.vy
        elif self.y < Grass - 6 * d: self.y = Grass - 6 * d
        elif self.y > HEIGHT - 6 * d: self.y = HEIGHT - 6 * d

    def fire2_start(self):
        '''
        Индикатор начала накопления энергии пушки
        '''
        self.f2_on = 1
        self.act_col = rn.choice(GAME_COLORS)

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

        x, y = pygame.mouse.get_pos()
        if (x > self.x):
            self.an = np.arctan((y - self.y) / (x - self.x))
        elif x < self.x and y < self.y:
            self.an = np.arctan((y - self.y) / (x - self.x)) - np.pi
        elif x < self.x and y > self.y:
            self.an = np.arctan((y - self.y) / (x - self.x)) + np.pi

        l = l_0 #* self.f2_power
        new_ball.x = self.x + (l - d) * np.cos(self.an)
        new_ball.y = self.y + (l - d) * np.sin(self.an)
        new_ball.color = self.act_col
        self.an = np.arctan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * np.cos(self.an)
        new_ball.vy = -self.f2_power * np.sin(self.an)
        new_ball.bottom = self.y + 2 * d
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
        n = int(3 * (1 - np.exp(-3 * self.f2_power))) #int(self.f2_power * 0.1) 
        bullet += 1 + 2 * n
        x, y = pygame.mouse.get_pos()
        if (x > self.x):
            self.an = np.arctan((y - self.y) / (x - self.x))
        elif x < self.x and y < self.y:
            self.an = np.arctan((y - self.y) / (x - self.x)) - np.pi
        elif x < self.x and y > self.y:
            self.an = np.arctan((y - self.y) / (x - self.x)) + np.pi
        l = l_0 #* self.f2_power

        new_shot = Shot(screen)
        new_shot.an = self.an
        new_shot.x = self.x + (l + k - d) * np.cos(self.an)
        new_shot.y = self.y + (l + k - d) * np.sin(self.an)
        new_shot.color = self.act_col
        new_shot.vx = self.f2_power * np.cos(new_shot.an)
        new_shot.vy = -self.f2_power * np.sin(new_shot.an)
        Shots.append(new_shot)
        for i in range(1, n, 1):
            new_shot = Shot(screen)
            new_shot.an = self.an + np.pi / (6 * i)
            new_shot.x = self.x + (l + k - d) * np.cos(self.an)
            new_shot.y = self.y + (l + k - d) * np.sin(self.an)
            new_shot.color = self.act_col
            new_shot.vx = self.f2_power * np.cos(new_shot.an)
            new_shot.vy = -self.f2_power * np.sin(new_shot.an)
            Shots.append(new_shot)
            new_shot = Shot(screen)
            new_shot.an = self.an - np.pi / (6 * i)
            new_shot.x = self.x + (l + k - d) * np.cos(self.an)
            new_shot.y = self.y + (l + k - d) * np.sin(self.an)
            new_shot.color = self.act_col
            new_shot.vx = self.f2_power * np.cos(new_shot.an)
            new_shot.vy = -self.f2_power * np.sin(new_shot.an)
            Shots.append(new_shot)
        self.f2_on = 0
        self.f2_power = 10
        return bullet, shots

    def targetting(self):
        """
        Прицеливание. Зависит от положения мыши
        """
        x, y = pygame.mouse.get_pos()
        if (x != self.x):
            self.an = np.arctan((y - self.y) / (x - self.x))

    def draw(self):
        '''
        Рисует пушку
        '''
        pygame.draw.polygon(screen, 0x3B1E08,
        [
            (self.x - 4 * h, self.y + 2 * d),
            (self.x - 3 * h, self.y - 2 * d),
            (self.x + 3 * h, self.y - 2 * d),
            (self.x + 4 * h, self.y + 2 * d)
        ])
        pygame.draw.aalines(screen, BLACK, True,
        [
            (self.x - 4 * h, self.y + 2 * d),
            (self.x - 3 * h, self.y - 2 * d),
            (self.x + 3 * h, self.y - 2 * d),
            (self.x + 4 * h, self.y + 2 * d)
        ])
        pygame.draw.circle(screen, GREY, (self.x - 4 * h, self.y + 4 * d), 2 * d)
        pygame.draw.circle(screen, GREY, (self.x + 4 * h, self.y + 4 * d), 2 * d)
        pygame.draw.circle(screen, BLACK, (self.x - 4 * h, self.y + 4 * d), 2 * d, 2)
        pygame.draw.circle(screen, BLACK, (self.x + 4 * h, self.y + 4 * d), 2 * d, 2)
        pygame.draw.rect(screen, GREY, (self.x - 4 * h, self.y + 2 * d, 8 * h, 4 * d))
        pygame.draw.line(screen, BLACK, (self.x - 4 * h, self.y + 2 * d), (self.x + 4 * h, self.y + 2 * d))
        pygame.draw.line(screen, BLACK, (self.x - 4 * h, self.y + 6 * d), (self.x + 4 * h, self.y + 6 * d))


        x, y = pygame.mouse.get_pos()
        if (x > self.x):
            self.an = np.arctan((y - self.y) / (x - self.x))
        elif x < self.x and y < self.y:
            self.an = np.arctan((y - self.y) / (x - self.x)) - np.pi
        elif x < self.x and y > self.y:
            self.an = np.arctan((y - self.y) / (x - self.x)) + np.pi
        l = (l_0 + 10) * self.f2_power / 8
        pygame.draw.polygon(self.screen, self.color,
        [
            (self.x - d * np.cos(self.an) - 0.5 * h * np.sin(self.an), self.y - d * np.sin(self.an) + 0.5 * h * np.cos(self.an)),
            (self.x - d * np.cos(self.an) + 0.5 * h * np.sin(self.an), self.y - d * np.sin(self.an) - 0.5 * h * np.cos(self.an)),
            (self.x + (l - d) * np.cos(self.an) + 0.5 * h * np.sin(self.an), self.y + (l - d) * np.sin(self.an) - 0.5 * h * np.cos(self.an)),
            (self.x + (l - d) * np.cos(self.an) - 0.5 * h * np.sin(self.an), self.y + (l - d) * np.sin(self.an) + 0.5 * h * np.cos(self.an))
        ])
        pygame.draw.aalines(self.screen, self.color, True,
        [
            (self.x - d * np.cos(self.an) - 0.5 * h * np.sin(self.an), self.y - d * np.sin(self.an) + 0.5 * h * np.cos(self.an)),
            (self.x - d * np.cos(self.an) + 0.5 * h * np.sin(self.an), self.y - d * np.sin(self.an) - 0.5 * h * np.cos(self.an)),
            (self.x + (l - d) * np.cos(self.an) + 0.5 * h * np.sin(self.an), self.y + (l - d) * np.sin(self.an) - 0.5 * h * np.cos(self.an)),
            (self.x + (l - d) * np.cos(self.an) - 0.5 * h * np.sin(self.an), self.y + (l - d) * np.sin(self.an) + 0.5 * h * np.cos(self.an))
        ])

def counter(points):
    '''
    Счетчик очков
    '''
    font = pygame.font.SysFont(None, 30)
    img = font.render(str(points), True, (0, 0, 0))
    screen.blit(img, (0.05 * WIDTH, 0.05 * HEIGHT))

def cooldown(timer, cldn, time_cldn):
    '''
    Откат сильной атаки
    '''
    pygame.draw.rect(screen, BLACK, (0.02 * WIDTH, 0.97 * HEIGHT, 0.15 * WIDTH, 0.02 * HEIGHT), 2)
    pygame.draw.rect(screen, WHITE, (0.02 * WIDTH, 0.97 * HEIGHT, 0.15 * WIDTH, 0.02 * HEIGHT))
    pygame.draw.rect(screen, (173, 216, 230), (0.02 * WIDTH, 0.97 * HEIGHT, 0.15 * WIDTH * (timer - time_cldn) / timer, 0.02 * HEIGHT))
    if time_cldn <= 0: cldn = False
    if cldn: time_cldn -= 1
    return cldn, time_cldn

def draw_all(targets, targ_sin, airplanes, bombs, balls, shots, gun, cldn, time_cldn):
    '''
    Отрисовывание всего
    '''
    screen.fill(WHITE)
    pygame.draw.rect(screen, 0x74B72E, (0, Grass, WIDTH, HEIGHT - Grass))
    for t in targets:
        t.draw()
    for t_s in targ_sin:
        t_s.draw()
    for b in balls:
        b.draw()
    for sh in shots:
        sh.draw()
    for air in airplanes:
        air.draw()
    for bomb in bombs:
        bomb.draw()
    gun.draw()
    counter(points)
    cldn, time_cldn = cooldown(100, cldn, time_cldn)
    pygame.display.update()
    return cldn, time_cldn

def events(gun, v_w, v_s, v_a, v_d, balls, shots, bullet, finished, cldn, time_cldn):
    '''
    Считывание всех ивентов
    '''
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN and (event.button == 1 or (event.button == 3 and not cldn)):
            gun.fire2_start()
            gun.button = event.button
        elif event.type == pygame.MOUSEBUTTONUP and gun.button == 1:
            bullet, new_ball = gun.fire_ball_end(event, bullet)
            balls.append(new_ball)
            gun.button = 0
        elif event.type == pygame.MOUSEBUTTONUP and gun.button == 3 and time_cldn <= 0:
            bullet, shots = gun.fire_shot_end(event, bullet, shots)
            gun.button = 0
            cldn = True
            time_cldn = 100

        elif event.type == pygame.MOUSEMOTION:
            gun.targetting()
        if pygame.key.get_pressed()[pygame.K_w]: v_w = -1
        else: v_w = 0
        if pygame.key.get_pressed()[pygame.K_s]: v_s = 1
        else: v_s = 0
        if pygame.key.get_pressed()[pygame.K_a]: v_a = -1
        else: v_a = 0
        if pygame.key.get_pressed()[pygame.K_d]: v_d = 1
        else: v_d = 0
        #if not pygame.key.get_pressed()[pygame.K_w]: v_w = 0
        #if not pygame.key.get_pressed()[pygame.K_s]: v_s = 0
        #if not pygame.key.get_pressed()[pygame.K_a]: v_a = 0
        #if not pygame.key.get_pressed()[pygame.K_d]: v_d = 0
    return gun, v_w, v_s, v_a,  v_d, balls, shots, bullet, finished, cldn, time_cldn

def move_all(gun, v_w, v_s, v_a, v_d, balls, shots, targets, targ_sin, airplanes, bombs):
    '''
    Движение всего
    '''
    gun.move(v_w + v_s, v_a + v_d)
    ball_clone = []
    shots_clone = []
    target_clone = []
    targ_sin_clone = []
    airplanes_clone = []
    bombs_clone = []

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

    for air in airplanes:
        if air.x >= WIDTH * 1.5:
            air.live = 0
        if air.x <= -WIDTH * 0.5:
            air.live = 0
        if air.live == 1:
            airplanes_clone.append(air)
            rand = rn.random()
            if rand < 0.1 and air.time_to_bomb <= 0:
                new_bomb = Bomb(screen)
                new_bomb.x = air.x
                new_bomb.y = air.y
                new_bomb.vx = -air.vx
                new_bomb.an = 0.5 * np.pi - 0.5 * np.pi * air.vect
                bombs.append(new_bomb)
                air.time_to_bomb = 60
        air.move()
    airplanes = airplanes_clone

    for bomb in bombs:
        if bomb.live > 0:
            bomb.move()
            bombs_clone.append(bomb)
    bombs = bombs_clone

    return gun, balls, shots, targets, targ_sin, airplanes, bombs

def hits(balls, shots, targets, targ_sin, airplanes, points, again):
    '''
    Проверка на столкновения
    '''
    for b in balls:
        for t in targets:
            if b.hittest(t):
                points += 1
                t.live = 0
                again = True
                #i = 0
                #break
        for t_s in targ_sin:
            if b.hittest(t_s):
                points += 1
                t_s.live = 0
                again = True
                #i = 0
                #break
        for air in airplanes:
            if b.hittest(air):
                points += 1
                air.live = 0
                againt = True
    for sh in shots:
        for t in targets:
            if sh.hittest(t):
                points += 1
                t.live = 0
                sh.live = 0
                again = True
                #i = 0
                #break
        for t_s in targ_sin:
            if sh.hittest(t_s):
                points += 1
                t_s.live = 0
                sh.live = 0
                again = True
                #i = 0
                #break
        for air in airplanes:
            if sh.hittest(air):
                points += 1
                air.live = 0
                againt = True
    return points, again, 0

def more_targ(targets, targ_sin, airplanes):
    '''
    Добавляет нужные мишени
    '''
    if len(targets) < -1:
        targets.append(Target())
    if len(targ_sin) < -1:
        targ_sin.append(Targ_sin())
    rand = rn.random()
    if len(airplanes) < 6 and rand < 0.05:
        airplanes.append(Airplane())
    return targets, targ_sin, airplanes

def result(bullet, i, again, finished):
    '''
    Вывод результата игры
    экран с надписью 
    "вы уничтожили цель за n выстрелов"
    '''
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    screen.fill(WHITE)
    counter(points)
    font = pygame.font.SysFont(None, 40)
    if bullet % 10 == 1:
        img = font.render('Вы уничтожили цель за ' + str(bullet) + ' выстрел', True, (0, 0, 0))
    elif bullet % 10 > 1 and bullet % 10 < 5:
        img = font.render('Вы уничтожили цель за ' + str(bullet) + ' выстрела', True, (0, 0, 0))
    elif bullet % 10 > 4 or bullet % 10 == 0:
        img = font.render('Вы уничтожили цель за ' + str(bullet) + ' выстрелов', True, (0, 0, 0))
    screen.blit(img, (0.2 * WIDTH, 0.45 * HEIGHT))
    pygame.display.update()
    i += 1
    if i >= time_of_pause:
        again = False
        bullet = 0
    return bullet, i, again, finished

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
points = 0
time_of_pause = 60
#Флаги для движения пушки
v_w = 0
v_s = 0
v_a = 0
v_d = 0
balls = []
shots = []
targets = []
targ_sin = []
airplanes = []
bombs = []
i = 0
time_cldn = 0

clock = pygame.time.Clock()
gun = Gun(screen)
finished = False
again = False
cldn = False

while not finished:
    if not again:
        cldn, time_cldn = draw_all(targets, targ_sin, airplanes, bombs, balls, shots, gun, cldn, time_cldn)

        gun, v_w, v_s, v_a, v_d, balls, shots, bullet, finished, cldn, time_cldn = events(gun, v_w, v_s, v_a, v_d, balls, shots, bullet, finished, cldn, time_cldn)

        gun, balls, shots, targets, targ_sin, airplanes, bombs = move_all(gun, v_w, v_s, v_a, v_d, balls, shots, targets, targ_sin, airplanes, bombs)

        points, again, i = hits(balls, shots, targets, targ_sin, airplanes, points, again)

        targets, targ_sin, airplanes = more_targ(targets, targ_sin, airplanes)

        gun.power_up()

    again = False #отключение вывода результатов

    if again:
        balls = []
        shots = []
        targets = []
        targ_sin = []
        bullet, i, again, finished = result(bullet, i, again, finished)

pygame.quit()