import telebot
from random import *

bot = telebot.TeleBot("5230826014:AAHRZ2Jcs_x8d-JQ6bmksZ62zcxW1oR01SY")

answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]



@bot.message_handler(content_types=['text'])
def ask_name(message):
    bot.send_message(message.chat.id, "Каково твое имя?: ")
    bot.register_next_step_handler(message, ask_name2)

def ask_name2(message):
    a=message.text
    bot.send_message(message.chat.id, f'сконцентрируйся и задай свой вопрос судьбе, {a}:')
    bot.register_next_step_handler(message, tell_prediction)


@bot.message_handler(content_types=['text'])
def tell_prediction(message):
    bot.send_message(message.chat.id, choice(answers))
    bot.register_next_step_handler(message, tell_prediction)
    #b=input("Вы хотите задать еще один вопрос? (1-Да, 0-Нет): ")
    #if b==str(0):
        #print('Возвращайся если возникнут вопросы!')

bot.polling( none_stop=True )