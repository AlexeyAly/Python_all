from turtle import*
n=100
speed(3)

def sn(n):
    for i in range(4):
        forward(n)
        if i%2!=0:
            right(120)
        else:
            right(60)

for i in range(10):

    sn(100)
    right(45)
