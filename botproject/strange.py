def send_echo(uiper):
    word = get_word()

    word_completion = '-' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    bot.send_message(uiper.chat.id,display_hangman(tries))
    bot.send_message(uiper.chat.id,f"{word_completion} {len(word)} букв")
    bot.send_message(uiper.chat.id,f"У вас осталось {tries} попыток чтоб угадать слово, иначе вас повесят")
    bot.send_message(uiper.chat.id, "Введите букву, несколько букв или слово целиком: ")
    bot.send_message(uiper.chat.id, word)
    bot.register_next_step_handler(uiper, check_word,tries, guessed_letters, word)


def check_word(message, tries, guessed_letters, word):
    if message.text == "Нет":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Игры')
        item2 = types.KeyboardButton('Погода')
        item3 = types.KeyboardButton('Стикеры')

        markup.add(item1, item2, item3)

        bot.send_message(message.chat.id, "Нет", reply_markup=markup)
        bot.register_next_step_handler(message, bot_mesasge)
    if message.text == "Да" or message.text == "Не знаю":
        bot.send_message(message.chat.id, "Введите правый диапазон:")
        bot.register_next_step_handler(message, send_echo)
    else:
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
                    bot.send_message(message.chat.id,f"У вас осталось {tries} попыток чтоб угадать слово, иначе вас повесят")
                    bot.send_message(message.chat.id, display_hangman(tries))
                if tries < 1:
                    bot.send_message(message.chat.id,f"К сожалению или счастью вас повесили, но знайте что слово было {word}")

                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    item1 = types.KeyboardButton('Да')
                    item2 = types.KeyboardButton('Нет')
                    item3 = types.KeyboardButton('Не знаю')

                    markup.add(item1, item2, item3)

                    bot.send_message(message.chat.id, 'Хочешь сыграть еще?', reply_markup=markup)

                    if message.text == "Да" or message.text == "Не знаю":
                        bot.send_message(message.chat.id, "Введите правый диапазон:")
                        bot.register_next_step_handler(message, check_da)

                    elif message.text == "Нет":

                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                        item1 = types.KeyboardButton('Игры')
                        item2 = types.KeyboardButton('Погода')
                        item3 = types.KeyboardButton('Стикеры')

                        markup.add(item1, item2, item3)

                        bot.send_message(message.chat.id, "Нет", reply_markup=markup)
                        bot.register_next_step_handler(message, bot_mesasge)

                    #bot.register_next_step_handler(message, send_echo)
                else:
                    for i in range(len(word)):
                        if word[i] in guessed_letters:
                            W += word[i]
                        else:
                            W += "-"
                    bot.send_message(message.chat.id, W)
        if W == word:
            #bot.send_message(message.chat.id, "Вы угадали, вас, возможно, не повесят")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Да')
            item2 = types.KeyboardButton('Нет')
            item3 = types.KeyboardButton('Не знаю')

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, 'Вы угадали, вас, возможно, не повесят, Хочешь сыграть еще?', reply_markup=markup)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Игры')
            item2 = types.KeyboardButton('Погода')
            item3 = types.KeyboardButton('Стикеры')

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, "Нет", reply_markup=markup)

            if message.text == "Да" or message.text == "Не знаю":
                bot.send_message(message.chat.id, "Введите правый диапазон:")
                bot.register_next_step_handler(message, send_echo)

            elif message.text == "Нет":

                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('Игры')
                item2 = types.KeyboardButton('Погода')
                item3 = types.KeyboardButton('Стикеры')

                markup.add(item1, item2, item3)

                bot.send_message(message.chat.id, "Нет", reply_markup=markup)
                bot.register_next_step_handler(message, bot_mesasge)

        else:
            if message.text == "Да" or message.text == "Не знаю":
                bot.send_message(message.chat.id, "Введите правый диапазон:")
                bot.register_next_step_handler(message, send_echo)

            elif message.text == "Нет":

                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('Игры')
                item2 = types.KeyboardButton('Погода')
                item3 = types.KeyboardButton('Стикеры')

                markup.add(item1, item2, item3)

                bot.send_message(message.chat.id, "Нет", reply_markup=markup)
                bot.register_next_step_handler(message, bot_mesasge)
            else:
                if tries>0:
                    bot.register_next_step_handler(message, check_word, tries, guessed_letters,word)
    if message.text == "Да" or message.text == "Не знаю":
        bot.send_message(message.chat.id, "Введите правый диапазон:")
        bot.register_next_step_handler(message, send_echo)

    elif message.text == "Нет":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Игры')
        item2 = types.KeyboardButton('Погода')
        item3 = types.KeyboardButton('Стикеры')

        markup.add(item1, item2, item3)

        bot.send_message(message.chat.id, "Нет", reply_markup=markup)
        bot.register_next_step_handler(message, bot_mesasge)