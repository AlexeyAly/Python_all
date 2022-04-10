n=5

for i in range(n):
    for j in range(n,n-1-i,-1):
        print(j,end="")
    print("." * (n-1 - i) * 2,end="")
    for j in range(n-i,n+1):
        print(j,end="")
    print()
