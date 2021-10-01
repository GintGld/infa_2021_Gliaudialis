from random import *
import turtle as tl
tl.shape('classic')
tl.speed(0)
for i in range(100):
    tl.forward(random() * 50)
    tl.left(randint(0, 360))
tl.exitonclick()