import turtle as tl
import numpy as np
from random import *
tl.setup(800, 800)

number_of_turtles = 30
T = 500
alpha = 30 #Коэффициент пропорциональности
q = 2 #Степень пропорциональности
V_max = 35
dt = 0.05
wall = 200
delta = 0.2 * V_max
d = 0.5 #Диаметр шарика
beta = 15 #Коэффициент дальности силы

X = [0] * number_of_turtles 
Y = [0] * number_of_turtles
Vx = [0] * number_of_turtles
Vy = [0] * number_of_turtles
Ax = [0] * number_of_turtles
Ay = [0] * number_of_turtles

#Генерация
pool = [tl.Turtle(shape='circle') for i in range(number_of_turtles)]
nt = 0
for unit in pool:
    unit.penup()
    unit.speed(0)
    unit.shapesize(d)
    X[nt] = (random() - 0.5) * 2 * wall
    Y[nt] = (random() - 0.5) * 2 * wall
    Vx[nt] = (random() - 0.5) * 2 * V_max
    Vy[nt] = (random() - 0.5) * 2 * V_max
    unit.goto(X[nt], Y[nt])
    nt += 1

#Расчет движения
for i in range(T):
    #Рачет ускорения
    nt = 0
    for unit in pool:
        a_nt = 0
        Ax[nt] = 0
        Ay[nt] = 0
        for another_unit in pool:
            if nt != a_nt:
                if X[nt] - X[a_nt] <= beta * d and X[nt] > X[a_nt]:
                    Ax[nt] += alpha * float(beta * d + X[a_nt] - X[nt]) ** q
                if X[a_nt] - X[nt] <= beta * d and X[a_nt] > X[nt]:
                    Ax[nt] += - alpha * float(beta * d + X[nt] - X[a_nt]) ** q
                if Y[nt] - Y[a_nt] <= beta * d and Y[nt] > Y[a_nt]:
                    Ay[nt] += alpha * float(beta * d + Y[a_nt] - Y[nt]) ** q
                if Y[a_nt] - Y[nt] <= beta * d and Y[a_nt] > Y[nt]:
                    Ay[nt] += - alpha * float(beta * d + Y[nt] - Y[a_nt]) ** q
            a_nt += 1
        nt += 1
    #Расчет скорости
    nt = 0
    for unit in pool:
        if X[nt] >= wall - delta and Vx[nt] > 0:
            Vx[nt] *= -1
        if X[nt] <= -wall + delta and Vx[nt] < 0:
            Vx[nt] *= -1
        if Y[nt] >= wall - delta and Vy[nt] > 0:
            Vy[nt] *= -1
        if Y[nt] <= -wall + delta and Vy[nt] < 0:
            Vy[nt] *= -1
        Vx[nt] += Ax[nt] * dt
        Vy[nt] += Ay[nt] * dt
        nt += 1
    #Расчет координаты
    nt = 0
    for unit in pool:
        unit.goto(float(X[nt] + Vx[nt] * dt), float(Y[nt] + Vy[nt] * dt))
        X[nt] += Vx[nt] * dt
        Y[nt] += Vy[nt] * dt
        nt += 1
tl.exitonclick()