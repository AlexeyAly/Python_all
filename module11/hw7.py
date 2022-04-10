first_pointa=float(input())
first_pointb=float(input())
second_pointa=float(input())
second_pointb=float(input())

a1=int(first_pointa*10)
b1=int(first_pointb*10)
a2=int(second_pointa*10)
b2=int(second_pointb*10)



if a1>8 or a1<0 or b1>8 or b1<0 or a2>8 or a2<0 or b2>8 or b2<0:
    print("wrong input")
if (abs(a1-a2) == 1 and abs(b1-b2) == 2) or (abs(a1-a2) == 2 and abs(b1-b2) == 1):
    print("this step is possible")

else:
    print("horse is not able to moove like this")