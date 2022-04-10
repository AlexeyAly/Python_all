n=input()
l=0
L=int(len(n)-1)
for i in range(1,len(n)+1):
    if i%2 != 0:
        print(n[l], end="")
        l+=2
for i in range(1, len(n) + 1):
     if i%2 == 0:
         print(n[L], end="")
         L-=2
