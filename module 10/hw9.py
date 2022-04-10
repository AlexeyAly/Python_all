n=5
k=1
for i in range(1,n+1):
    print('\t' * (n - i), end="")
    for j in range(i):
        print(k,end="")
        k+=2
        print('\t'*2,end='')
    print()