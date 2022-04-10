a,b,c = float(input()), float(input()), float(input())
x=1
for x in range(-100,100):
    if a*x**2+b*x+c==0:
        print(x)


