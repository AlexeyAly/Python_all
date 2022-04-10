w=int(input("input width: "))
c=0
while w>12:
    w=w/2
    c+=2
print("You need to fold the letter", c, "times in order to fit the envelope")