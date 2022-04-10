beg=int(input("beg "))
end=int(input("end "))
step=int(input("step "))

for x in range (beg,end-1,step):

    y = x ** 3 + 2*x ** 2 - 4*x + 1
    print("in the point", x, "function equals", y)


