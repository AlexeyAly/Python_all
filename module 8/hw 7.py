educational_grant = int(input("Schoolarship: "))
expenses = int(input("Expenses: "))
sum = 0
grantsum = 0
for i in range(10):
    sum += expenses
    expenses=expenses * 1.03
    grantsum+= educational_grant
    print(sum)
print("you will need to borrow at least", sum-grantsum, "from your parents")
