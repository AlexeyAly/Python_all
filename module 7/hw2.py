
count=0
s=0
while count<10:
    i=int(input("enter the number: "))
    count+=1
    if i%2==0 and i>0:
        s+=1

print(s)