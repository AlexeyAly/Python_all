from random import *
def is_valid(b):
    return b.isdigit() and right_range>int(b)>0

def body_game(lasten):
    inp = -1
    count = 0
    n = randint(1, lasten)
    while inp!=n:
        inp=input()
        count+=1
        if is_valid(str(inp)):
            inp=int(inp)
            if inp == n:
                break
            elif inp>n:
                print("Слишком много, попробуйте еще раз")
            elif inp<n:
                print("Слишком мало, попробуйте еще раз")
        elif is_valid(str(inp)) == False:
            print('А может быть все-таки введем целое число от 1 до', lasten, '?')
    print('Победа!!! Вы угадали ответ за', count, 'попыток, поздравляем!')

while True:
    right_range=int(input("Введите правый диапазон: "))
    print('Добро пожаловать в числовую угадайку')
    body_game(right_range)
    check=int(input('Вы хотите сыгдать еще? (1 - Да, 2 - Нет): '))
    if check == 2:
        break
