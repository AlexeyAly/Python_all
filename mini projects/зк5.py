from random import *

word_list=['год', 'человек', 'время', 'дело', ]

def get_word():
    return choice(word_list).upper()
word=get_word()

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play(word):
    print('Давайте играть в угадайку слов!')
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    print(display_hangman(tries))
    print(word_completion)
    print(f"У вас осталось {tries} попыток чтоб угадать слово, иначе вас повесят")
    while True:

        hang=0


        inp=input("Введите букву, несколько букв или слово целиком: ").upper()
        if inp == word:
            print(word)
            print("Вы угадали, вас, возможно, не повесят")
            break
        if inp in guessed_letters:
            print("Вы уже вводили эту букву(от Валерка!)")
            continue
        if inp.isalpha() == 0:
            print("вводите только буквы")
        else:
            l = [i if i not in guessed_letters else print("Вы уже вводиди эту букву") for i in inp  ]
            for i in inp:
                if i not in word:
                    tries-=1
                    hang+=1
            guessed_letters+=l
            if hang>0:
                print(f"У вас осталось {tries} попыток чтоб угадать слово, иначе вас повесят")
                print(display_hangman(tries))
            if tries < 1:
                print(f"К сожалению или счастью вас повесили, но знайте что слово было {word}")
                break


        #print(guessed_letters)
        W=""
        for i in range(len(word)):
            if word[i] in guessed_letters:
                W+=word[i]
            else: W+="_"
        print(W)
        if W == word:
            print("Вы угадали, вас, возможно, не повесят")
            break
    if int(input("Вы хотите сышрать еще (1 - да, 0 - нет: ")) == 1:
        word = get_word()
        play(word)

play(word)




