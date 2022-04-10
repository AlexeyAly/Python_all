X,Y=15,20
XS=8
YS=10
print("Current robot position is:", XS,YS)
while 0<XS<X+1 and 0<YS<Y+1:
    inX = input(' введите команду: ')
    if inX == 'a':
        XS=XS-1
        if 2>XS:
            XS=1
    elif inX =='d':
        XS=XS+1
        if 14<XS:
            XS=15
    elif inX =='w':
        YS+=1
        if 19<YS:
            YS=20
    elif inX =='s':
        YS-=1
        if 2>YS:
            YS=1
    print("Current robot position is:",XS,YS)

