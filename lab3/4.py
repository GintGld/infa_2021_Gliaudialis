import turtle as tl
tl.shape('circle')
tl.speed(0)
tl.hideturtle()
tl.setup(1000, 500)
g = 10
s = -480
alpha = 0.8
tl.goto(500, 0)
tl.goto(-500, 0)
tl. goto(s, 0)
for i in range(12):
    k = 0
    Vx = 25 * alpha ** i
    Vy = 60 * alpha ** i
    t = 0
    while t <= 2 * Vy / g:
        tl.goto(Vx * t + s, Vy * t - 0.5 * g * t ** 2)
        k = Vx * t
        t += 0.1
    s = s + k
tl.exitonclick()