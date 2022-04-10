a=int(input("Please enter a: "))
b=int(input("PLease enter b: "))
o=0
p=0
for i in range (a,b+1):
    print(i)
    if i%3 ==0:
        o=o+i
        p+=1
print ("average of all numbers divisible by 3 is:", int(o/p))
