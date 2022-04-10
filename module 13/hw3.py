n=int(input())
k=int(input())

def reverse(a):
    b=""
    for i in range (len(str(a))-1,-1,-1):
        b+=str(a)[i]
    return int(b)

print(reverse(n))
print(reverse(k))