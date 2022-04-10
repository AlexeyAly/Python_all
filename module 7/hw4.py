o=0
i=0
for i in range (30, 35):
    print("enter quantity in sector", i, end=": ")
    s=int(input())
    if s>10:
        print("The quantity of people is more than should be")
        o+=1
    else:
        print("The quantity of people is fine")
print("Violations quantity is", o)