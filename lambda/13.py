
b=input().split()
k=int(input())
z=len(b)
g=0
for i in range(len(b)):
    g+=int(b[i])*k**(z-1)
    z-=1
print(g)


