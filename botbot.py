import pyowm
from pyowm.utils.config import get_default_config
import telebot

owm = pyowm.OWM('1f0e262e15c5790f98efecb2573b959c')
config_dict = get_default_config()
config_dict['language'] = 'ru'\

bot = telebot.TeleBot("5184523501:AAFRWgVHl21MfyLcfIT8V0TtSkvRJG5gSi8")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = (w.temperature('celsius')["temp"])

    answer = "Сейчас за окном " + w.detailed_status + ", температура около " + str(temp) + "\n"
    if temp < 10:
        answer += "а это ужасная дюдя, одевайся как капуста, ато простудишься!"
    elif temp < 12:
        answer += "а это прохладно, одень куртку и свитерок!"
    else:
        answer += "а это комфортная температура, одевайся как хочешь"
    bot.reply_to(message, answer)



bot.polling(none_stop=True)