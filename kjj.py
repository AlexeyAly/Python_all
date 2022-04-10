
import pyowm
from pyowm.utils.config import get_default_config

import telebot

owm = pyowm.OWM('1f0e262e15c5790f98efecb2573b959c')
config_dict = get_default_config()
config_dict['language'] = 'ru'\

bot = telebot.TeleBot("5230826014:AAHRZ2Jcs_x8d-JQ6bmksZ62zcxW1oR01SY")
frozensmile = "\U0001F976"

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):

    bot.send_message(message.chat.id,"Напиши свое имя")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    try:
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place( message.text )
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
    except:

            if message.text == "Галя":
                mgr = owm.weather_manager()
                observation = mgr.weather_at_place("Poltava")
                w = observation.weather
                temp = (w.temperature('celsius')["temp"])

                answer = "Та я и так знаю что ты в Полтаве, сейчас за окном " + w.detailed_status + ", температура около " + str(temp) + "\n"
                if temp < 10:
                    answer += "а это ужасная дюдя, " + frozensmile + "одевайся как капуста, ато простудишься!"
                elif temp < 12:
                    answer += "а это прохладно, одень куртку и свитерок!"
                else:
                    answer += "а это комфортная температура, одевайся как хочешь"
                bot.send_message(message.chat.id,
                                 "Я и так знаю что ты в Полтаве, но если хочешь напиши другой город. " + answer)

            elif message.text == "Алекс":
                mgr = owm.weather_manager()
                observation = mgr.weather_at_place("Poltava")
                w = observation.weather
                temp = (w.temperature('celsius')["temp"])

                answer = "Сейчас за окном " + w.detailed_status + ", температура около " + str(temp) + "\n"
                if temp < 10:
                    answer += "а это ужасная дюдя, " + frozensmile + "одевайся как капуста, ато простудишься!"
                elif temp < 12:
                    answer += "а это прохладно, одень куртку и свитерок!"
                else:
                    answer += "а это комфортная температура, одевайся как хочешь"
                bot.send_message(message.chat.id,
                                 "Я и так знаю что ты в Полтаве, но если хочешь напиши другой город. " + answer)

            elif message.text == "Нинна":
                mgr = owm.weather_manager()
                observation = mgr.weather_at_place("Bulancak")
                w = observation.weather
                temp = (w.temperature('celsius')["temp"])

                answer = "Сейчас за окном " + w.detailed_status + ", температура около " + str(temp) + "\n"
                if temp < 10:
                    answer += "а это ужасная дюдя, " + frozensmile + "одевайся как капуста, ато простудишься!"
                elif temp < 12:
                    answer += "а это прохладно, одень куртку и свитерок!"
                else:
                    answer += "а это комфортная температура, одевайся как хочешь"
                bot.send_message(message.chat.id,
                                 "Я и так знаю что ты в Гиресуне, если нет то напиши другой город. " + answer)
            else:
                bot.send_message(message.chat.id, "Привет, " + message.text + ".")
                bot.send_message(message.chat.id, "Напиши город в котором находишься")


bot.polling( none_stop=True )