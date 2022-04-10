while True:
    n1=input("enter 6 digits ticket nr: ")
    n=int(n1)
    if(len(n1))==6:
        if n // 100000 % 10+n // 10000 % 10+n // 1000 % 10==n // 100 % 10+n//10 %10+n%10:
            print("lucky")
        else:
            print("unlucky")
    else:
        print("please correct your number!")