while True:
    p=input("Введите строку: ")
    count=0
    c1=0
    for letter in p:
        if letter != " ":
            count+=1
            if c1<count:
                c1=count
        if letter ==" ":
            count=0
    print("длинна самого длинного слова", c1)



