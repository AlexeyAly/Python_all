import telebot
from telebot import types
from random import *
from math import *


bot = telebot.TeleBot("5230826014:AAHRZ2Jcs_x8d-JQ6bmksZ62zcxW1oR01SY")

@bot.message_handler(  commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Games 🎮')
    #item2 = types.KeyboardButton('ПогоYes')
    item3 = types.KeyboardButton('Stickers 😛')


    markup.add(item1,item3)

    bot.send_message(message.chat.id, "Hi, {0.first_name}!". format(message.from_user), reply_markup= markup)
    print("Hi, {0.first_name}!". format(message.from_user))

@bot.message_handler(content_types=['text'])
def bot_mesasge(message):
    if message.chat.type == 'private':
        if message.text == "Stickers 😛":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Кубик')
            item2 = types.KeyboardButton('Баскетбол')
            item3 = types.KeyboardButton('Кегли')
            item4 = types.KeyboardButton('Yesртс')
            item5 = types.KeyboardButton('Казино')
            item6 = types.KeyboardButton('Go back')


            markup.add(item1, item2, item3, item4, item5, item6)
            bot.send_message(message.chat.id, "Другое", reply_markup=markup)

        elif message.text == "Кубик":
            bot.send_dice(message.chat.id, '🎲')
        elif message.text == "Баскетбол":
            bot.send_dice(message.chat.id, '🏀')
        elif message.text == "Кегли":
            bot.send_dice(message.chat.id, '🎳')
        elif message.text == "Yesртс":
            bot.send_dice(message.chat.id, '🎯')
        elif message.text == "Казино":
            bot.send_dice(message.chat.id, '🎰')

        elif message.text == "Go back":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Games 🎮')
            #item2 = types.KeyboardButton('ПогоYes')
            item3 = types.KeyboardButton('Stickers 😛')

            markup.add(item1, item3)

            bot.send_message(message.chat.id, "Go back", reply_markup=markup)

        elif message.text == "Games 🎮":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Hangman ☠')
            item2 = types.KeyboardButton('Guess the number')
            item3 = types.KeyboardButton('Черный шар судьбы')
            item4 = types.KeyboardButton('Go back')

            markup.add(item1, item2, item3, item4)

            bot.send_message(message.chat.id, "Games 🎮", reply_markup=markup)
        elif message.text == "Guess the number":
            bot.send_message(message.chat.id, "Lets play Guess the number")
            bot.send_message(message.chat.id, "Enter the last number in the guessing range:")
            bot.register_next_step_handler(message, get_right)
        elif message.text == "Черный шар судьбы":
            bot.send_message(message.chat.id, 'Cконцентрируйся и задай свой вопрос судьбе, {0.first_name}!'. format(message.from_user))
            bot.register_next_step_handler(message, tell_prediction)
        elif message.text == "Hangman ☠":
            bot.send_message(message.chat.id, "Now I will try to hang you, are you ready to resist?")
            bot.register_next_step_handler(message, send_echo)
        elif message.text == "ПогоYes":
            bot.send_message(message.chat.id, "Напиши свое имя")
            bot.register_next_step_handler(message, send_weather)





# угаYesйка чисел
def is_valid(b,right_range):
    return b.isdigit() and right_range>int(b)>0

def get_right(message):



    if message.text.isdigit():
        right_range=int(message.text)
        inp = -1
        count = 0
        print(right_range)
        n = randint(1, right_range)
        print(n)
        valera=ceil(log2(int(message.text)))

        bot.send_message(message.chat.id, f"If you are smart enough, you will be able to guess in {valera} tries")
        bot.send_message(message.chat.id, "Now you have to guess a number inside the range")
        bot.register_next_step_handler(message, digit_game, right_range, inp, count,n,valera )
    else:
        if message.text == "Yes":
            bot.register_next_step_handler(message, guess_win)
        elif message.text == "No":
            bot.register_next_step_handler(message, guess_win)
        else:
            bot.send_message(message.chat.id, "You have to enter only numbers, try again")
            bot.register_next_step_handler(message, bot_mesasge)

def digit_game(message, right_range, inp, count,n,valera):
    if inp!=n:
        inp=message.text
        count+=1
        if is_valid(str(inp),right_range):
            inp=int(inp)
            if inp == n:
                if count<valera+1:
                    bot.send_message(message.chat.id, f'Congats! you have guessed the number in  {count} tries, you are either smart or lucky')
                else:
                    bot.send_message(message.chat.id, f'Congratulations!!! you have guessed the number in {count} tries, probably you are not that smart!')

                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('Yes')
                item2 = types.KeyboardButton('No')
                item3 = types.KeyboardButton('I dunno')


                markup.add(item1, item2, item3)

                bot.send_message(message.chat.id, 'Do you wanna play once again?', reply_markup=markup)



            elif inp>n:
                bot.send_message(message.chat.id,"Too much, try again")
            elif inp<n:
                bot.send_message(message.chat.id,"Way to less, try again")

        elif is_valid(str(inp), right_range) == False:
            bot.send_message(message.chat.id,f'But maybe you will enter a number from 0 till {right_range}?')
        bot.register_next_step_handler(message, digit_game, right_range, inp, count,n, valera)
    else:
        if message.text == "Yes" or message.text == "I dunno":
            bot.send_message(message.chat.id, "Enter the range:")
            bot.register_next_step_handler(message, get_right)

        elif message.text == "No":

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Games 🎮')
            item2 = types.KeyboardButton('ПогоYes')
            item3 = types.KeyboardButton('Stickers 😛')

            markup.add(item1, item3)

            bot.send_message(message.chat.id, "No", reply_markup=markup)
            bot.register_next_step_handler(message, bot_mesasge)

# виселица
word_list=['knee', 'knife', 'knock', 'adapt', 'know', 'affect', 'land', 'afford', 'lap', 'large', 'last', 'borrow', 'map', 'margin', 'budget', 'mark', 'market', 'campus', 'nerve', 'civil', 'oppose', 'deal', 'porch', 'port', 'pose', 'quit', 'elite', 'quote', 'recipe', 'email', 'emerge', 'refuse', 'regard', 'scope', 'score', 'fiber', 'scream', 'screen', 'field', 'script', 'tactic', 'forest', 'tail', 'forget', 'form', 'talent', 'formal', 'uncle', 'gear', 'gender', 'gene', 'video', 'view', 'viewer', 'holy', 'weapon', 'home', 'wear', 'image', 'week', 'impact', 'year', 'income', 'yell', 'yellow', 'joy', 'judge', 'equal', 'lord', 'king', 'france', 'cousin', 'will', 'move', 'speedy', 'friend', 'seem', 'make', 'denial', 'love', 'wisdom', 'answer', 'mean', 'freely', 'leave', 'stand', 'part', 'well', 'serve', 'gentry', 'sick', 'enter', 'count', 'good', 'young', 'youth', 'bear', 'father', 'face', 'frank', 'nature', 'haste', 'moral', 'paris', 'duty', 'look', 'time', 'long', 'steal', 'talk', 'return', 'hide', 'honour', 'like', 'pride', 'clock', 'true', 'minute', 'speak', 'tongue', 'obey', 'hand', 'place', 'proud', 'poor', 'praise', 'copy', 'follow', 'rich', 'royal', 'speech', 'always', 'say', 'hear', 'word', 'ear', 'grow', 'live', 'begin', 'heel', 'flame', 'lack', 'snuff', 'sense', 'expire', 'wish', 'honey', 'bring', 'home', 'hive', 'give', 'room', 'lend', 'fill', 'know', 'month', 'rest', 'debate', 'stock', 'exchange', 'note', 'sell', 'equity', 'large', 'liquid', 'attractive', 'guarantor', 'settlement', 'counter', 'dealer', 'different', 'attract', 'cover', 'interest', 'frequently', 'likely', 'trade', 'transfer', 'money', 'security', 'seller', 'buyer', 'agree', 'price', 'ownership', 'particular', 'company', 'market', 'range', 'small', 'individual', 'larger', 'world', 'include', 'insurance', 'pension', 'hedge', 'trader', 'physical', 'floor', 'method', 'known', 'open', 'offer', 'type', 'network', 'example', 'potential', 'specific', 'accept', 'match', 'sale', 'place', 'multiple', 'purpose', 'facilitate', 'provide', 'real', 'discovery', 'hybrid', 'location', 'flow', 'broker', 'order', 'post', 'maintain', 'spread', 'case', 'close', 'difference', 'tape', 'brokerage', 'firm', 'investor', 'play', 'important', 'role', 'program', 'electronic', 'computer', 'similar', 'purchase', 'drive', 'late', 'system']

def get_word():
    return choice(word_list).upper()

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
|       |
|     / 
-
''',
# голова, торс, обе руки
'''
--------
|      |
|      O
|     \\|/
|       |
|      
-
''',
# голова, торс и одна рука
'''
--------
|      |
|      O
|     \\|
|       |
|     
-
''',
# голова и торс
'''
--------
|      |
|      O
|      |
|       |
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



def send_echo(uiper):
    word = get_word()
    bot.send_message(uiper.chat.id, "It doesn't matter though, let's play a word guessing game!")

    word_completion = '-' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    bot.send_message(uiper.chat.id,display_hangman(tries))
    bot.send_message(uiper.chat.id,f"{word_completion} {len(word)} letters")
    bot.send_message(uiper.chat.id,f"You still have {tries} tries to guess the word, othervise you will be hanged")
    bot.send_message(uiper.chat.id, "Enter the letter, a few letters or a word: ")
    #bot.send_message(uiper.chat.id, word)
    bot.register_next_step_handler(uiper, check_word,tries, guessed_letters, word)


def check_word(message, tries, guessed_letters, word):
    hang = 0
    W = ""
    inp = message.text.upper()
    if inp in guessed_letters:
        bot.send_message(message.chat.id, "Вы уже вводили эту букву(от Валерка!)")
        print(guessed_letters)
    else:
        if inp.isalpha() == 0:
            bot.send_message(message.chat.id, "вводите только буквы")
        else:
            l = [i  for i in inp if i not in guessed_letters]
            for i in inp:
                if i not in word:
                    tries -= 1
                    hang += 1
            guessed_letters += l
            if hang > 0:
                bot.send_message(message.chat.id,f"You still have {tries} tries to guess the word, othervise you will be hanged")
                bot.send_message(message.chat.id, display_hangman(tries))
            if tries < 1:
                bot.send_message(message.chat.id,f"Unfortunately or fortunately, you were hanged, but the the word was {word}")
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('Yes')
                item2 = types.KeyboardButton('No')
                item3 = types.KeyboardButton('I dunno')

                markup.add(item1, item2, item3)

                bot.send_message(message.chat.id, 'Do you wanna play once again?', reply_markup=markup)
                bot.register_next_step_handler(message, check_da)
            else:
                for i in range(len(word)):
                    if word[i] in guessed_letters:
                        W += word[i]
                    else:
                        W += "-"
                bot.send_message(message.chat.id, W)
    if W == word:
        bot.send_message(message.chat.id, "You guessed it, you might not be hanged")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Yes')
        item2 = types.KeyboardButton('No')
        item3 = types.KeyboardButton('I dunno')

        markup.add(item1, item2, item3)

        bot.send_message(message.chat.id, 'Wanna play once again?', reply_markup=markup)
        bot.register_next_step_handler(message, check_da)

    else:
        if tries>0:
            bot.register_next_step_handler(message, check_word, tries, guessed_letters,word)



def check_da(message):
    if message.text == "Yes" or message.text == "I dunno":
        bot.send_message(message.chat.id, "We will hang you again! Ready?")
        bot.register_next_step_handler(message, send_echo)
    elif message.text == "No":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Games 🎮')
        item2 = types.KeyboardButton('ПогоYes')
        item3 = types.KeyboardButton('Stickers 😛')

        markup.add(item1, item3)

        bot.send_message(message.chat.id, "No", reply_markup=markup)
        bot.register_next_step_handler(message, bot_mesasge)

#шар

answers = ["Бесспорно", "Мне кажется - Yes", "Пока неясно, попробуй снова", "Yesже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - No",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим Yesнным - No",
           "Можешь быть уверен в этом", "Yes", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

def tell_prediction(message):
    print(message.text)
    choi=choice(answers)
    bot.send_message(message.chat.id, choi)
    print(choi)


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Yes')
    item2 = types.KeyboardButton('No')
    item3 = types.KeyboardButton('I dunno')

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, 'Хочешь еще один вопрос?', reply_markup=markup)
    bot.register_next_step_handler(message, check_dashar)
def check_dashar(message):
    if message.text == "Yes" or message.text == "I dunno":

        bot.send_message(message.chat.id, "Еще раз натужся и сформулируй вопрос:")
        bot.register_next_step_handler(message, tell_prediction)
    if message.text == "No":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Games 🎮')
        item2 = types.KeyboardButton('ПогоYes')
        item3 = types.KeyboardButton('Stickers 😛')

        markup.add(item1, item3)

        bot.send_message(message.chat.id, "Возвращайся если возникнут вопросы!", reply_markup=markup)
        bot.register_next_step_handler(message, bot_mesasge)

#ПогоYes

def send_weather(message):
    import pyowm
    from pyowm.utils.config import get_default_config
    owm = pyowm.OWM('1f0e262e15c5790f98efecb2573b959c')
    config_dict = get_default_config()
    config_dict['language'] = 'ru' \


    if message.text == "Рома":
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place("Poznan")
        w = observation.weather
        temp = (w.temperature('celsius')["temp"])

        answer = "Сейчас за окном " + w.detailed_status + ", температура около " + str(temp) + "\n"
        if temp < 10:
            answer += "а это ужасная дюдя, " + frozensmile + "одевайся как капуста, ато простудишься!"
        elif temp < 12:
            answer += "а это прохладно, одень куртку и свитерок!"
        elif temp<22:
            answer += "а это комфортная температура, одевайся как хочешь"
        else: answer += "а это страшная жара, срочно снимай одежду и окунайся куYes-то, или ищи кондиционер"
        bot.send_message(message.chat.id,
                         "Я и так знаю что ты в Познани, если No то напиши другой город. " + answer)
    elif message.text == "Нина":
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place("Bulancak")
        w = observation.weather
        temp = (w.temperature('celsius')["temp"])

        answer = "Сейчас за окном " + w.detailed_status + ", температура около " + str(temp) + "\n"
        if temp < 10:
            answer += "а это ужасная дюдя, " + frozensmile + "одевайся как капуста, ато простудишься!"
        elif temp < 12:
            answer += "а это прохладно, одень куртку и свитерок!"
        elif temp<22:
            answer += "а это комфортная температура, одевайся как хочешь"
        else: answer += "а это страшная жара, срочно снимай одежду и окунайся куYes-то, или ищи кондиционер"
        bot.send_message(message.chat.id,
                         "Я и так знаю что ты в Гиресуне, если No то напиши другой город. " + answer)
    elif message.text == "Таня":
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place("Bulancak")
        w = observation.weather
        temp = (w.temperature('celsius')["temp"])

        answer = "Сейчас за окном " + w.detailed_status + ", температура около " + str(temp) + "\n"
        if temp < 10:
            answer += "а это ужасная дюдя, " + frozensmile + "одевайся как капуста, ато простудишься!"
        elif temp < 12:
            answer += "а это прохладно, одень куртку и свитерок!"
        elif temp<22:
            answer += "а это комфортная температура, одевайся как хочешь"
        else: answer += "а это страшная жара, срочно снимай одежду и окунайся куYes-то, или ищи кондиционер"
        bot.send_message(message.chat.id,
                         "Я и так знаю что ты в Гиресуне, если No то напиши другой город. " + answer)
    elif message.text == "Татьяна":
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place("Калининград")
        w = observation.weather
        temp = (w.temperature('celsius')["temp"])

        answer = "Сейчас за окном " + w.detailed_status + ", температура около " + str(temp) + "\n"
        if temp < 10:
            answer += "а это ужасная дюдя, " + frozensmile + "одевайся как капуста, ато простудишься! И возьми на всякий случай зонтик, ато у вас все время дождь!"
        elif temp < 12:
            answer += "а это прохладно, одень куртку и свитерок! И возьми на всякий случай зонтик, ато у вас все время дождь!"
        elif temp < 22:
            answer += "а это комфортная температура, одевайся как хочешь И возьми на всякий случай зонтик, ато у вас все время дождь!"
        else:
            answer += "а это страшная жара, срочно снимай одежду и окунайся куYes-то, или ищи кондиционер"
        bot.send_message(message.chat.id,
                         "Я и так знаю что ты в Калининграде, если No то напиши другой город. " + answer)
    elif message.text == "Тимур":
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place("Bulancak")
        w = observation.weather
        temp = (w.temperature('celsius')["temp"])

        answer = "Сейчас за окном " + w.detailed_status + ", температура около " + str(temp) + "\n"
        if temp < 10:
            answer += "а это ужасная дюдя, " + frozensmile + "одевайся как капуста, ато простудишься!"
        elif temp < 12:
            answer += "а это прохладно, одень куртку и свитерок!"
        elif temp<22:
            answer += "а это комфортная температура, одевайся как хочешь"
        else: answer += "а это страшная жара, срочно снимай одежду и окунайся куYes-то, или ищи кондиционер"
        bot.send_message(message.chat.id,
                         "Я и так знаю что ты в Гиресуне, если No то напиши другой город. " + answer)
    elif message.text == "Дима":
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place("Калининград")
        w = observation.weather
        temp = (w.temperature('celsius')["temp"])

        answer = "Сейчас за окном " + w.detailed_status + ", температура около " + str(temp) + "\n"
        if temp < 10:
            answer += "а это ужасная дюдя, " + frozensmile + "одевайся как капуста, ато простудишься!"
        elif temp < 12:
            answer += "а это прохладно, одень куртку и свитерок!"
        elif temp < 22:
            answer += "а это комфортная температура, одевайся как хочешь"
        else:
            answer += "а это страшная жара, срочно снимай одежду и окунайся куYes-то, или ищи кондиционер"
        bot.send_message(message.chat.id,
                         "Я и так знаю что ты в Калининграде, если No то напиши другой город. " + answer)
    elif message.text == "Эля":
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place("Bulancak")
        w = observation.weather
        temp = (w.temperature('celsius')["temp"])

        answer = "Сейчас за окном " + w.detailed_status + ", температура около " + str(temp) + "\n"
        if temp < 10:
            answer += "а это ужасная дюдя, " + frozensmile + "одевайся как капуста, ато простудишься!"
        elif temp < 12:
            answer += "а это прохладно, одень куртку и свитерок!"
        elif temp<22:
            answer += "а это комфортная температура, одевайся как хочешь"
        else: answer += "а это страшная жара, срочно снимай одежду и окунайся куYes-то, или ищи кондиционер"
        bot.send_message(message.chat.id,
                         "Я и так знаю что ты в Гиресуне, если No то напиши другой город. " + answer)

    elif message.text == "Саша":
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
    elif message.text == "Саня":
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
    elif message.text == "Александр":
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





    else:


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
            elif temp < 22:
                answer += "а это комфортная температура, одевайся как хочешь"
            else:
                answer += "а это страшная жара, срочно снимай одежду и окунайся куYes-то, или ищи кондиционер"
            bot.send_message(message.chat.id, answer)
        except:

                if message.text == "Настя":
                    mgr = owm.weather_manager()
                    observation = mgr.weather_at_place("Poltava")
                    w = observation.weather
                    temp = (w.temperature('celsius')["temp"])

                    answer = "Та я и так знаю что ты в Полтаве, сейчас за окном " + w.detailed_status + ", температура около " + str(temp) + "\n"
                    if temp < 10:
                        answer += "а это ужасная дюдя, " + frozensmile + "одевайся как капуста, ато простудишься!"
                    elif temp < 12:
                        answer += "а это прохладно, одень куртку и свитерок!"
                    elif temp < 22:
                        answer += "а это комфортная температура, одевайся как хочешь"
                    else:
                        answer += "а это страшная жара, срочно снимай одежду и окунайся куYes-то, или ищи кондиционер"
                    bot.send_message(message.chat.id,
                                     "Я и так знаю что ты в Полтаве, но если хочешь напиши другой город. " + answer)
                elif message.text == "Анастасия":
                    mgr = owm.weather_manager()
                    observation = mgr.weather_at_place("Poltava")
                    w = observation.weather
                    temp = (w.temperature('celsius')["temp"])

                    answer = "Та я и так знаю что ты в Полтаве, сейчас за окном " + w.detailed_status + ", температура около " + str(temp) + "\n"
                    if temp < 10:
                        answer += "а это ужасная дюдя, " + frozensmile + "одевайся как капуста, ато простудишься!"
                    elif temp < 12:
                        answer += "а это прохладно, одень куртку и свитерок!"
                    elif temp < 22:
                        answer += "а это комфортная температура, одевайся как хочешь"
                    else:
                        answer += "а это страшная жара, срочно снимай одежду и окунайся куYes-то, или ищи кондиционер"
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

                elif message.text == "Нина":
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
                                     "Я и так знаю что ты в Гиресуне, если No то напиши другой город. " + answer)
                else:
                    bot.send_message(message.chat.id, "Привет, " + message.text + ".")
                    bot.send_message(message.chat.id, "Напиши город в котором находишься")




bot.polling( none_stop=True )

















