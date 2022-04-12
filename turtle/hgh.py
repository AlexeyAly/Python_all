import turtle as t
import random

t.Screen().setup(640, 480)
t.shape('triangle')
t.Screen().bgcolor('black')
t.speed(1000)
t.pensize(3)
t.penup()
s = 40
for _ in range(600):
    t.pencolor(('blue', 'DarkOrchid', 'DeepSkyBlue', 'goldenrod', 'PaleGreen')[random.randint(0, 4)])
    t.stamp()
    t.right(152)
    t.forward(s)
    s += 0.5