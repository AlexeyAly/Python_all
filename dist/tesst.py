
import pyowm
from pyowm.utils.config import get_default_config

import telebot

owm = pyowm.OWM('')
config_dict = get_default_config()
config_dict['language'] = 'ru'\

bot = telebot.TeleBot("5230826014:AAHRZ2Jcs_x8d-JQ6bmksZ62zcxW1oR01SY")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):

    bot.reply_to(message,"Напиши свое имя")

frozensmile = "\U0001F976"

@bot.message_handler(content_types=['text'])
def send_echo(message):
    bot.send_message(message.chat.id, "Привет, " + message.text + ".")
    if message.text=="Саша":
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place("Poltava")
        w = observation.weather
        temp = (w.temperature('celsius')["temp"])

        answer="Сейчас за окном " + w.detailed_status + ", температура около " + str(temp) + "\n"
        if temp < 10:
            answer+="а это ужасная дюдя, "+ frozensmile + "одевайся как капуста, ато простудишься!"
        elif temp < 12:
            answer+="а это прохладно, одень куртку и свитерок!"
        else:
            answer+="а это комфортная температура, одевайся как хочешь"
        bot.send_message(message.chat.id,"Я и так знаю что ты в Полтаве, но если хочешь напиши другой город. " + answer)

    elif message.text == "Алекс":
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place("Poltava")
        w = observation.weather
        temp = (w.temperature('celsius')["temp"])

        answer = "Сейчас за окном " + w.detailed_status + ", температура около " + str(temp) + "\n"
        if temp < 10:
            answer += "а это ужасная дюдя, одевайся как капуста, ато простудишься!"
        elif temp < 12:
            answer += "а это прохладно, одень куртку и свитерок!"
        else:
            answer += "а это комфортная температура, одевайся как хочешь"
        bot.send_message(message.chat.id,
                         "Я и так знаю что ты в Полтаве, но если хочешь напиши другой город. " + answer)

    elif message.text == "Нина":
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place("Bulancak")
        w = observation.weather
        temp = (w.temperature('celsius')["temp"])

        answer = "Сейчас за окном " + w.detailed_status + ", температура около " + str(temp) + "\n"
        if temp < 10:
            answer += "а это ужасная дюдя, одевайся как капуста, ато простудишься!"
        elif temp < 12:
            answer += "а это прохладно, одень куртку и свитерок!"
        else:
            answer += "а это комфортная температура, одевайся как хочешь"
        bot.send_message(message.chat.id,"Я и так знаю что ты в Гиресуне, если нет то напиши другой город. " + answer)
    else:
        bot.send_message(message.chat.id, "Напишите город в котором находишься")

        @bot.message_handler(content_types=['text'])
        def send_echo(message1):
            mgr = owm.weather_manager()
            observation = mgr.weather_at_place( message1.text )
            w = observation.weather
            temp = (w.temperature('celsius')["temp"])

            answer = "Сейчас за окном " + w.detailed_status + ", температура около " + str(temp) + "\n"
            if temp < 10:
                answer += "а это ужасная дюдя, одевайся как капуста, ато простудишься!"
            elif temp < 12:
                answer += "а это прохладно, одень куртку и свитерок!"
            else:
                answer += "а это комфортная температура, одевайся как хочешь"
            bot.send_message(message.chat.id, answer)



bot.polling( none_stop=True )