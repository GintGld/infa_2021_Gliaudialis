import math
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
        
    def hit(self, points):
        """Попадание шарика в цель."""
        self.points += points
        return points

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
    
    def fire2_end(self, event, bullet):
        """
        Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan((event.pos[1] - y_0) / (event.pos[0] - x_0))
        l = l_0 * self.f2_power
        new_ball.x = x_0 + (l - d) * math.cos(self.an)
        new_ball.y = y_0 + (l - d) * math.sin(self.an)
        new_ball.color = self.act_col
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = -self.f2_power * math.sin(self.an)
        self.f2_on = 0
        self.f2_power = 10
        return bullet, new_ball

    def targetting(self):
        """Прицеливание. Зависит от положения мыши."""
        x, y = pygame.mouse.get_pos()
        self.an = math.atan((y - y_0) / (x - x_0))

    def draw(self):
        '''
        Рисует пушку
        '''
        x, y = pygame.mouse.get_pos()
        self.an = math.atan((y - y_0) / (x - x_0))
        l = (l_0 + 10) * self.f2_power / 8
        pygame.draw.polygon(self.screen, self.color,
        [
            (x_0 - d * math.cos(self.an) - 0.5 * h * math.sin(self.an), y_0 - d * math.sin(self.an) + 0.5 * h * math.cos(self.an)),
            (x_0 - d * math.cos(self.an) + 0.5 * h * math.sin(self.an), y_0 - d * math.sin(self.an) - 0.5 * h * math.cos(self.an)),
            (x_0 + (l - d) * math.cos(self.an) + 0.5 * h * math.sin(self.an), y_0 + (l - d) * math.sin(self.an) - 0.5 * h * math.cos(self.an)),
            (x_0 + (l - d) * math.cos(self.an) - 0.5 * h * math.sin(self.an), y_0 + (l - d) * math.sin(self.an) + 0.5 * h * math.cos(self.an))
        ])
        pygame.draw.aalines(self.screen, self.color, True,
        [
            (x_0 - d * math.cos(self.an) - 0.5 * h * math.sin(self.an), y_0 - d * math.sin(self.an) + 0.5 * h * math.cos(self.an)),
            (x_0 - d * math.cos(self.an) + 0.5 * h * math.sin(self.an), y_0 - d * math.sin(self.an) - 0.5 * h * math.cos(self.an)),
            (x_0 + (l - d) * math.cos(self.an) + 0.5 * h * math.sin(self.an), y_0 + (l - d) * math.sin(self.an) - 0.5 * h * math.cos(self.an)),
            (x_0 + (l - d) * math.cos(self.an) - 0.5 * h * math.sin(self.an), y_0 + (l - d) * math.sin(self.an) + 0.5 * h * math.cos(self.an))
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
targets = []

clock = pygame.time.Clock()
gun = Gun(screen)
finished = False
again = False

while not finished:
    if not again:
        screen.fill(WHITE)
        counter(points)
        gun.draw()
        for t in targets:
            t.draw()
        for b in balls:
            b.draw()
        pygame.display.update()

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                gun.fire2_start(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                bullet, new_balls = gun.fire2_end(event, bullet)
                balls.append(new_balls)
            elif event.type == pygame.MOUSEMOTION:
                gun.targetting()

        ball_clone = []
        target_clone = []

        for b in balls:
            if b.live > 0:
                b.move()
                ball_clone.append(b)
        balls = ball_clone
        for t in targets:
            if t.live > 0:
                t.move()
                target_clone.append(t)
        targets = target_clone
        for b in balls:
            for t in targets:
                if b.hittest(t):
                    points += 1
                    again = True
                    i = 0
                    break
        if len(targets) < 2:
            targets.append(Target())
        gun.power_up()
    
    if again:
        balls = []
        targets = []
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
