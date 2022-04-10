N=int(input("seconds left till the BOOM: "))
boom=True
for i in range (N,-1,-1):
    L=int(input("Do you want to defuse the bomb? (1 - yes, 2 - no): "))
    if L == 1:
        print("the bomb was defused successfully, there was still", i, "seconds till the explosion")
        break
    else:
        print("there are still", i, "seconds till the explosion")
print("BOOM")