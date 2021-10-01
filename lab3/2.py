import turtle as tl
tl.shape('classic')
tl.speed(0)
index = [(45, 28.28, 225, 40, 180, 40, 135, 28.28, 135), 
(90, 20, 180, 20, 90, 20, 90, 20, 180, 40, 180, 20, 90, 20, 180), 
(45, 28.28, 225, 40, 180, 40, 135, 28.28, 135), 
(270, 20, 180, 20, 315, 28.28, 135, 20, 180, 20, 225, 28.28, 135),
(270, 20, 90, 20, 90, 40, 90, 20, 90, 20, 90),
(270, 20, 90, 20, 90, 40, 90, 20, 90, 20, 90)]
for i in index:
    for j in range(len(i)):
        if j % 2 == 0:
            tl.left(i[j])
        else:
            tl.forward(i[j])
    tl.penup()
    tl.forward(30)
    tl.pendown()
tl.exitonclick()