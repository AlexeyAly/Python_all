q=int(input())
tsum=0
nu=0
k=0
for i in range(q):
    w=int(input())
    k=w
    sum=0
    while w:
        L=w%10
        sum+=L
        w=w//10
    if tsum<sum:
        tsum=sum
        nu=k
print(tsum)
print(nu)
