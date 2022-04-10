h=0
s=0
w=0
while h<3:
    h=h+1
    print(h, "hour")
    s=s+int(input("how many tasks: "))
    w=w+int(input("PIck up the phone? (1-yes, 0-no): "))
print(s)
if w>0:
    print("Нужно зайти в магазин")

