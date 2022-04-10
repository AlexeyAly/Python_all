from turtle import*

def hexagon(side):
    speed(3)
    for i in range(6):
        forward(side)
        right(60)

for i in range(7):
    hexagon(50)
    right(120)
    forward(50)
    left(60)

