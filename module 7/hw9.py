count=0
o=0
for i in range(1,5):
    print("Please enter your salary for the", i, "month:", end=" " )
    i=int(input())
    if i>o:
        count+=1
        o=i
if count==4:
    print("all the selaries were rising")
else:
    print("not all the selaries were rising")


