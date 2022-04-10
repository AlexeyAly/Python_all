def summa_n(n):
    z=0
    for i in range(1,n+1):
        z+=i
    print("Я знаю, что сумма чисел от 1 до", n, "равна",z)
k=int(input())
summa_n(k)
