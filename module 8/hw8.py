N=int(input("Please input N: "))
s=1
for i in range (1,N+1):
    S=(-1)**i*1/2**i
    s=s+S
    print(s)
print("Row sum equals: ",s)



