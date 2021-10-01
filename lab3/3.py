import turtle as tl
tl.shape('classic')
tl.speed(0)
inp = open(r'C:\Users\coolg\Desktop\input.txt', 'r')
a = []
for j in range(6):
    s = inp.readline()
    a = list(map(float, s.split(' ')))
    for i in range(len(a)):
        if i % 2 == 0:
            tl.left(a[i])
        else:
            tl.forward(a[i])
    tl.penup()
    tl.forward(30)
    tl.pendown()
inp.close()
tl.exitonclick()