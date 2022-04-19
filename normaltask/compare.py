def compare(n):
    return sum([int(i) for i in str(n)])

b=input().split()

print(*sorted(b,key=compare))