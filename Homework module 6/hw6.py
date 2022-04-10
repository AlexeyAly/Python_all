i=0
b=0
while True:
    z = int(input("enter the number: "))
    if z>0:
        i=i+1
    elif z<0:
        b=b+1
    elif z==0:
        break
print("Количество положительных чисел: ", i)
print("Количество отрицательных чисел: ", b)
