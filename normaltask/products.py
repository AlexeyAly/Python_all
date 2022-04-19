def print_products(*args):
    j = [i for i in args if len(str(i)) > 0 and type(i) is str]
    if len(j) > 0:
        n = 1
        for i in j:
            print(str(n) + ") " + i)
            n += 1
    else:
        print("Нет продуктов")

print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)