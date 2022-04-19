athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
            ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]


def name(ath):
    return ath[0]


def age(ath):
    return ath[1]


def hight(ath):
    return ath[2]


def weight(ath):
    return ath[2]


dic = {1: name, 2: age, 3: hight, 4: weight}
i = int(input())

for p in sorted(athletes, key=dic[i]):
    print(*p)