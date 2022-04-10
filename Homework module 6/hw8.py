X=int(input("Вклад в банке: "))
P=int(input("проценты: "))
Y=int(input("Желаемая сумма: "))
years=0
while X<Y:
    X=int(X+X*P/100)
    years+=1
print("ваш вклад достигнет желаемой суммы через", years, "лет")
print(X)
