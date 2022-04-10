s=int(input())
f=int(input())
count=0

for num in range(s, f+1):
    if num == 1:
        continue
    flag=False
    for div in range (2,num):
        if num%div==0:
            flag=True
    if flag==False:
            count+=1
print(count)




