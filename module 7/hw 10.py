numb=0
N=int(input("please input N: "))
for i in range (1,N+1):
   numb=numb+i
sum=0
for k in range (1,N):
    b=int(input("please input the number: "))
    sum=b+sum
print("the missing number is:" numb-sum)
