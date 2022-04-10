raw=int(input("Введите кол-во рядов: "))
seats=int(input("Введите кол-во сидений ряду: "))
m=int(input("Введите кол-во метров между рядами: "))
for i in range (raw+1):
    print(seats*"=",m*"*",seats*"=")