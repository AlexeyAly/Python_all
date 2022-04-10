N=int(input("Please enter the students quantity: "))
g=0
a=0
b=0
for i in range (N):
    i=int(input("Enter grade:"))
    if i == 5:
        g+=1
    elif i == 4:
        a += 1
    elif i == 3:
        b += 1
if g>a:
    if g>b:
        print("Very good marks are the most numerous")
    else:
        print("Bad marks are the most numerous")
elif g<a>b:
    print("Good marks are the most numerous")
else:
    print("Bad marks are the most numerous")




