def reverter():
    while True:
        n = str(input())
        if n == str(0):
            print("Программа завершена!")
            break
        k = [(n[i]) for i in range(len(n) - 1, -1, -1)]
        print(int("".join(k)))

reverter()



