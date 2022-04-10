import telebot
from random import *
from math import *
from telebot import types
bot = telebot.TeleBot("5230826014:AAHRZ2Jcs_x8d-JQ6bmksZ62zcxW1oR01SY")


def is_valid(b,right_range):
    return b.isdigit() and right_range>int(b)>0



@bot.message_handler(content_types=['text'])
def digit_starter(message):
    bot.send_message(message.chat.id, "Давай сыграем в угадай число")
    bot.send_message(message.chat.id, "Введите правый диапазон:")
    bot.register_next_step_handler(message, get_right)

def get_right(message):
    right_range=int(message.text)
    inp = -1
    count = 0
    print(right_range)
    n = randint(1, right_range)
    print(n)
    valera=ceil(log2(int(message.text)))

    bot.send_message(message.chat.id, f"Если ты не Валера то угадаешь менее чем за {valera} попыток")
    bot.send_message(message.chat.id, "Теперь угадывай число в заданном диапазоне")
    bot.register_next_step_handler(message, digit_game, right_range, inp, count,n,valera )




def digit_game(message, right_range, inp, count,n,valera):
    #if message.text == "Да":
        #bot.register_next_step_handler(message, guess_win)
    #elif message.text == "Нет":
        #bot.register_next_step_handler(message, guess_win)

    if inp!=n:
        inp=message.text
        count+=1
        if is_valid(str(inp),right_range):
            inp=int(inp)
            if inp == n:
                if count<valera+1:
                    bot.send_message(message.chat.id, f'Победа!!! Вы угадали ответ за {count} попыток, поздравляем, вероятнее всего вы не Валера!')
                else:
                    bot.send_message(message.chat.id, f'Победа!!! Валерка, ты угадал число аж за {count} попыток!')
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('Да')
                item2 = types.KeyboardButton('Нет')
                item3 = types.KeyboardButton('Не знаю')

                markup.add(item1, item2, item3)

                bot.send_message(message.chat.id, 'Хочешь сыграть еще?', reply_markup=markup)
                if message.text == "Да":
                    bot.register_next_step_handler(message, guess_win)
                elif message.text == "Нет":
                    bot.register_next_step_handler(message, guess_win)


            elif inp>n:
                bot.send_message(message.chat.id,"Слишком много, попробуйте еще раз")
            elif inp<n:
                bot.send_message(message.chat.id,"Слишком мало, попробуйте еще раз")

        elif is_valid(str(inp), right_range) == False:
            bot.send_message(message.chat.id,f'А может быть все-таки введем целое число от 1 до {right_range}?')
        bot.register_next_step_handler(message, digit_game, right_range, inp, count,n, valera)
    else:
        bot.register_next_step_handler(message, guess_winni)

    if message.text == "Да":
        bot.register_next_step_handler(message, guess_win)
    elif message.text == "Нет":
        bot.register_next_step_handler(message, guess_winno)

def guess_winni(message):
    bot.send_message(message.chat.id, f'наконец получилось')


def guess_win(message):
    bot.send_message(message.chat.id, f'Да')

def guess_winno(message):
    bot.send_message(message.chat.id, f'NO')


bot.polling( none_stop=True )
