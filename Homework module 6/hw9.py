i=3938
k=0
b=0
while b!=i:
    b=int(input("guess: "))
    if b<i:
        print("The number you entered is smaller, try again")
    elif b>i:
        print("The number you entered is bigger, try again")
    k+=1

print("This is the right number, you have used", k, "tries")

