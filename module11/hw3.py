size=int(input())
speed=int(input())
sp=speed

sec=size//speed
for s in range(1,sec+2):
    print("Прошло", s, "сек. Скачано", speed, "из", size, "Мб", '(', round(100*speed/size),"%)")
    if speed+sp<size:
        speed+=sp
    else:
        speed=size