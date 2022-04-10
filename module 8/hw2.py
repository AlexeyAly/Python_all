n=int(input("please input the debtors quantity: "))
sum=0
for i in range (0,n, 5):
    print ("Debtor #", i)
    s=int(input("how much do you owe: "))
    sum+=s
print("general amount is", sum)
