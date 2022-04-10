n=10
for i in range (n+1):
    if i<5:
        print(" "*i+"^"+" "*(8-2*i)+"^"+" "*i)
    if i>5:
        i = n - i

        print(" " * i + "^" + " " * (8 - 2 * i) + "^" + " " * i)