def divider():
    a=int(input())
    b=int(input())
    if a>b:
        a,b=b,a
    k=0
    for i in range(a,0,-1):
        if a%i == 0:
            if b%i == 0:
                k=i
                break
    print(k)
divider()