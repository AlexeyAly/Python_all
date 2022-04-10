

z=float(input())
count=0
while z>9 or z<1:
    if z>9:
        z=z/10
        count+=1
    elif z<1:
        z*=10
        count-=1
print(z,"*",10,"**",count,end="")
