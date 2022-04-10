t1 = 1
t2 = 100
while True:
    x=(t1+t2)//2
    print('твое число больше, меньше или равно', x, '?')
    t=int(input('1 - Равно, 2 - Больше, 3 - Меньше: '))
    if t==1:
      print("Я угадал")
      break
    elif t==2:
        t1=x
    else: t2=x
