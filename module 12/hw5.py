def calc():
    n=input()
    countn=0
    countl=0
    numb=input("Какую цифру ищем?:" )
    l=input("Какую букву ищем?:")
    for i in n:
        if i == numb:
            countn+=1
        if i == l:
            countl+=1
    print("Количество цифр", numb, countn)
    print("Количество букв", l, countl)
calc()
