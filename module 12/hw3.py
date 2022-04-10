while True:
    def results():
        n=int(input("enter the number:" ))
        k=int(input("enter the action:1-sum, 2-max, 3-min "))
        if k == 1:
            sum(n)
        elif k == 2:
            max(n)
        elif k == 3:
            min(n)

    def sum(n):
        new=0
        sum=0
        while n:
          new=n%10
          sum+=new
          n//=10
        print(sum)

    def max(n):
        new = 0
        max = 0
        while n:
            new = n % 10
            if new>max:
                max = new
            n //= 10
        print(max)
    def min(n):
        new = 0
        min = 9
        while n:
            new = n % 10
            if new<min:
                min = new
            n //= 10
        print(min)

    results()
