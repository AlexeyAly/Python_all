import telebot
bot = telebot.TeleBot("5230826014:AAHRZ2Jcs_x8d-JQ6bmksZ62zcxW1oR01SY")



@bot.message_handler(content_types=['text'])
def send_echo(message):
	if message.text=="Алекс":
		bot.reply_to(message, "Я тебя знаю")

	else:
		bot.reply_to(message, "Я хз кто ты")



bot.polling(none_stop=True)