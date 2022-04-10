X=int(input("Boys X: "))
Y=int(input("Girls Y: "))

if X>=Y:
    if Y-(X-Y)<0:
        print("There is no solution")
    else:
        p="BG"
        p1 = "BGB"
        print(p*(Y-(X-Y)),p1*(X-Y),sep="")
else:
    if X-(Y-X)<0:
        print("There is no solution")
    else:
        p="GB"
        p1 = "GBG"
        print(p*(X-(Y-X)),p1*(Y-X),sep="")





