import telebot
from telebot import types
import logging

bot = telebot.TeleBot("5230826014:AAHRZ2Jcs_x8d-JQ6bmksZ62zcxW1oR01SY")
frozensmile = "\U0001F976"


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
--------
|       |
|       O
|      \\|/
|        |
|      / \\
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




@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):

    bot.send_message(message.chat.id,"Напиши свое имя", reply_markup=get_keyboard())

def get_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    button = telebot.types.InlineKeyboardButton('Установить', callback_data='set timer')
    button = telebot.types.InlineKeyboardButton('Игра', callback_data='set timer')
    keyboard.add(button)
    return keyboard

@bot.message_handler(content_types=['text'])

def send_echo1(message0):
    attempt=0
    bot.send_message(message0.chat.id, display_hangman(attempt))










def send_echo2(message1):

    bot.send_message(message1.chat.id, "Какой у тебя рост?")
    if message1.text == "р":
        bot.send_message(message1.chat.id, "Круто!")
    else:
        bot.send_message(message1.chat.id, "не круто!")








bot.polling( none_stop=True )