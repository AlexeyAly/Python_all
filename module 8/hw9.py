x=int(input("please input your x: "))
sum1=1
try:
    for i in range (1, 7):
        s=(x - ((2 ** i) - 1))/(x - 2 ** i)
        sum1=sum1*s
    print(sum1)
except:
    print("There is no solution with this x, please try another x")

