a=int(input("a "))
b=int(input("b "))
c=int(input("c "))
num=0
count=0
for i in range (a,b+1):
    if i%c == 0:
        num=i+num
        count+=1
print(int(num/count))
print(int(count))

