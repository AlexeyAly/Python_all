import math
R=float(input())
V=4/3*math.pi*R**3
e=10.8321*10**11
if V<e:
    print("The Earth is in", round(e/V,3), "times bigger")
else:
    print("The Earth is in", round(V/ e, 3), "times smaller")























