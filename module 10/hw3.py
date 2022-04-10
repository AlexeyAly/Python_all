h=int(input())
w=int(input())
print("-"*w)
for i in range(h-1):
    print("|"+" "*(w-2)+"|")
print("|"+"-"*(w-2)+"|")


