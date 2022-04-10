import telebot
from telebot import types
from random import *
from math import *


bot = telebot.TeleBot("5230826014:AAHRZ2Jcs_x8d-JQ6bmksZ62zcxW1oR01SY")

@bot.message_handler(  commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Игры 🎮')
    #item2 = types.KeyboardButton('Погода')
    item3 = types.KeyboardButton('Стикеры 😛')


    markup.add(item1,item3)

    bot.send_message(message.chat.id, "Привет, {0.first_name}!". format(message.from_user), reply_markup= markup)
    print("Hi, {0.first_name}!".format(message.from_user))
@bot.message_handler(content_types=['text'])
def bot_mesasge(message):
    if message.chat.type == 'private':
        if message.text == "Стикеры 😛":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Кубик')
            item2 = types.KeyboardButton('Баскетбол')
            item3 = types.KeyboardButton('Кегли')
            item4 = types.KeyboardButton('Дартс')
            item5 = types.KeyboardButton('Казино')
            item6 = types.KeyboardButton('Назад')


            markup.add(item1, item2, item3, item4, item5, item6)
            bot.send_message(message.chat.id, "Другое", reply_markup=markup)

        elif message.text == "Кубик":
            bot.send_dice(message.chat.id, '🎲')
        elif message.text == "Баскетбол":
            bot.send_dice(message.chat.id, '🏀')
        elif message.text == "Кегли":
            bot.send_dice(message.chat.id, '🎳')
        elif message.text == "Дартс":
            bot.send_dice(message.chat.id, '🎯')
        elif message.text == "Казино":
            bot.send_dice(message.chat.id, '🎰')

        elif message.text == "Назад":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Игры 🎮')
            #item2 = types.KeyboardButton('Погода')
            item3 = types.KeyboardButton('Стикеры 😛')

            markup.add(item1, item3)

            bot.send_message(message.chat.id, "Назад", reply_markup=markup)

        elif message.text == "Игры 🎮":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Виселица(слова) ☠')
            item2 = types.KeyboardButton('Угадай число')
            item3 = types.KeyboardButton('Черный шар судьбы')
            item4 = types.KeyboardButton('Назад')

            markup.add(item1, item2, item3, item4)

            bot.send_message(message.chat.id, "Игры 🎮", reply_markup=markup)
        elif message.text == "Угадай число":
            bot.send_message(message.chat.id, "Давай сыграем в угадай число")
            bot.send_message(message.chat.id, "Введите правый диапазон:")
            bot.register_next_step_handler(message, get_right)
        elif message.text == "Черный шар судьбы":
            bot.send_message(message.chat.id, 'Cконцентрируйся и задай свой вопрос судьбе, {0.first_name}!'. format(message.from_user))
            bot.register_next_step_handler(message, tell_prediction)
        elif message.text == "Виселица(слова) ☠":
            bot.send_message(message.chat.id, "Сейчас попробуем тебя повесить! Справишься?")
            bot.register_next_step_handler(message, send_echo)
        elif message.text == "Погода":
            bot.send_message(message.chat.id, "Напиши свое имя")
            bot.register_next_step_handler(message, send_weather)





# угадайка чисел
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

        bot.send_message(message.chat.id, f"Если ты не Валера то угадаешь менее чем за {valera} попыток")
        bot.send_message(message.chat.id, "Теперь угадывай число в заданном диапазоне")
        bot.register_next_step_handler(message, digit_game, right_range, inp, count,n,valera )
    else:
        if message.text == "Да":
            bot.register_next_step_handler(message, guess_win)
        elif message.text == "Нет":
            bot.register_next_step_handler(message, guess_win)
        else:
            bot.send_message(message.chat.id, "Здесь нужно было вводить число! Повтори ввод!")
            bot.register_next_step_handler(message, bot_mesasge)

def digit_game(message, right_range, inp, count,n,valera):
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
                print(count)
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('Да')
                item2 = types.KeyboardButton('Нет')
                item3 = types.KeyboardButton('Не знаю')


                markup.add(item1, item2, item3)

                bot.send_message(message.chat.id, 'Хочешь сыграть еще?', reply_markup=markup)



            elif inp>n:
                bot.send_message(message.chat.id,"Слишком много, попробуйте еще раз")
            elif inp<n:
                bot.send_message(message.chat.id,"Слишком мало, попробуйте еще раз")

        elif is_valid(str(inp), right_range) == False:
            bot.send_message(message.chat.id,f'А может быть все-таки введем целое число от 1 до {right_range}?')
        bot.register_next_step_handler(message, digit_game, right_range, inp, count,n, valera)
    else:
        if message.text == "Да" or message.text == "Не знаю":
            bot.send_message(message.chat.id, "Введите правый диапазон:")
            bot.register_next_step_handler(message, get_right)

        elif message.text == "Нет":

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Игры 🎮')
            item2 = types.KeyboardButton('Погода')
            item3 = types.KeyboardButton('Стикеры 😛')

            markup.add(item1, item3)

            bot.send_message(message.chat.id, "Нет", reply_markup=markup)
            bot.register_next_step_handler(message, bot_mesasge)

# виселица
word_list=['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо',
             'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила',
             'конец',
             'вид', 'система', 'часть', 'город', 'отношение', 'женщина', 'деньги', 'земля', 'машина', 'вода', 'отец',
             'проблема', 'час', 'право', 'нога', 'решение', 'дверь', 'образ', 'история', 'власть', 'закон', 'война',
             'бог', 'голос', 'тысяча', 'книга', 'возможность', 'результат', 'ночь', 'стол', 'имя', 'область', 'статья',
             'число', 'компания', 'народ', 'жена', 'группа', 'развитие', 'процесс', 'суд', 'условие', 'средство',
             'начало', 'свет', 'пора', 'путь', 'душа', 'уровень', 'форма', 'связь', 'минута', 'улица', 'вечер',
             'качество', 'мысль', 'дорога', 'мать', 'действие', 'месяц', 'государство', 'язык', 'любовь', 'взгляд',
             'мама', 'век', 'школа', 'цель', 'общество', 'деятельность', 'организация', 'президент', 'комната',
             'порядок', 'момент', 'театр', 'письмо', 'утро', 'помощь', 'ситуация', 'роль', 'рубль', 'смысл',
             'состояние',
             'квартира', 'орган', 'внимание', 'тело', 'труд', 'сын', 'мера', 'смерть', 'рынок', 'программа', 'задача',
             'предприятие', 'окно', 'разговор', 'правительство', 'семья', 'производство', 'информация', 'положение',
             'центр', 'ответ', 'муж', 'автор', 'стена', 'интерес', 'федерация', 'правило', 'управление', 'мужчина',
             'идея', 'партия', 'совет', 'счет', 'сердце', 'движение', 'вещь', 'материал', 'неделя', 'чувство', 'глава',
             'наука', 'ряд', 'газета', 'причина', 'плечо', 'цена', 'план', 'речь', 'точка', 'основа', 'товарищ',
             'культура', 'данные', 'мнение', 'документ', 'институт', 'ход', 'проект', 'встреча', 'директор', 'срок',
             'палец', 'опыт', 'служба', 'судьба', 'девушка', 'очередь', 'лес', 'состав', 'член', 'количество',
             'событие',
             'объект', 'зал', 'создание', 'значение', 'период', 'шаг', 'брат', 'искусство', 'структура', 'номер',
             'пример', 'исследование', 'гражданин', 'игра', 'начальник', 'рост', 'тема', 'принцип', 'метод', 'тип',
             'фильм', 'край', 'гость', 'воздух', 'характер', 'борьба', 'использование', 'размер', 'образование',
             'мальчик', 'кровь', 'район', 'небо', 'армия', 'класс', 'представитель', 'участие', 'девочка', 'политика',
             'герой', 'картина', 'доллар', 'спина', 'территория', 'пол', 'поле', 'изменение', 'направление', 'рисунок',
             'течение', 'церковь', 'банк', 'сцена', 'население', 'большинство', 'музыка', 'правда', 'свобода', 'память',
             'команда', 'союз', 'врач', 'договор', 'дерево', 'факт', 'хозяин', 'природа', 'угол', 'телефон', 'позиция',
             'двор', 'писатель', 'самолет', 'объем', 'род', 'солнце', 'вера', 'берег', 'спектакль', 'фирма', 'способ',
             'завод', 'цвет', 'журнал', 'руководитель', 'специалист', 'оценка', 'регион', 'песня', 'процент',
             'родитель',
             'море', 'требование', 'основание', 'половина', 'роман', 'круг', 'анализ', 'стихи', 'автомобиль',
             'экономика', 'литература', 'бумага', 'поэт', 'степень', 'господин', 'надежда', 'предмет', 'вариант',
             'министр', 'граница', 'дух', 'модель', 'операция', 'пара', 'сон', 'название', 'ум', 'повод', 'старик',
             'миллион', 'успех', 'счастье', 'ребята', 'кабинет', 'магазин', 'пространство', 'выход', 'удар', 'база',
             'знание', 'текст', 'защита', 'руководство', 'площадь', 'сознание', 'возраст', 'участник', 'участок',
             'пункт', 'линия', 'желание', 'папа', 'доктор', 'губа', 'дочь', 'среда', 'председатель', 'представление',
             'солдат', 'художник', 'волос', 'оружие', 'соответствие', 'ветер', 'парень', 'зрение', 'генерал', 'огонь',
             'понятие', 'строительство', 'ухо', 'грудь', 'нос', 'страх', 'услуга', 'содержание', 'радость',
             'безопасность', 'продукт', 'комплекс', 'бизнес', 'сад', 'сотрудник', 'лето', 'курс', 'предложение', 'рот',
             'технология', 'реформа', 'отсутствие', 'собака', 'камень', 'будущее', 'рассказ', 'контроль', 'река',
             'продукция', 'сумма', 'техника', 'здание', 'сфера', 'необходимость', 'фонд', 'подготовка', 'лист',
             'республика', 'хозяйство', 'воля', 'бюджет', 'снег', 'деревня', 'мужик', 'элемент', 'обстоятельство',
             'немец', 'победа', 'источник', 'звезда', 'выбор', 'масса', 'итог', 'сестра', 'практика', 'проведение',
             'карман', 'слава', 'кухня', 'определение', 'функция', 'войско', 'комиссия', 'применение', 'капитан',
             'работник', 'обеспечение', 'офицер', 'фамилия', 'предел', 'выборы', 'ученый', 'бутылка', 'бой', 'теория',
             'зона', 'отдел', 'зуб', 'разработка', 'личность', 'гора', 'товар', 'метр', 'праздник', 'влияние',
             'читатель', 'удовольствие', 'актер', 'слеза', 'ответственность', 'учитель', 'акт', 'боль', 'множество',
             'особенность', 'показатель', 'корабль', 'звук', 'впечатление', 'частность', 'детство', 'вывод',
             'профессор',
             'доля', 'норма', 'прошлое', 'командир', 'коридор', 'поддержка', 'рамка', 'враг', 'этап', 'черт', 'дед',
             'собрание', 'прием', 'болезнь', 'клетка', 'кожа', 'заявление', 'попытка', 'сравнение', 'расчет', 'депутат',
             'комитет', 'знак', 'дядя', 'учет', 'хлеб', 'чай', 'режим', 'целое', 'вирус', 'выражение', 'здоровье',
             'зима', 'десяток', 'глубина', 'сеть', 'студент', 'секунда', 'скорость', 'поиск', 'суть', 'налог', 'ошибка',
             'доход', 'режиссер', 'поверхность', 'ощущение', 'карта', 'клуб', 'станция', 'революция', 'колено',
             'министерство', 'стекло', 'этаж', 'высота', 'бабушка', 'трубка', 'газ', 'мастер', 'поведение', 'столица',
             'механизм', 'передача', 'способность', 'подход', 'энергия', 'существование', 'исполнение', 'кино',
             'сожаление', 'заместитель', 'ресурс', 'акция', 'рождение', 'администрация', 'стоимость', 'улыбка',
             'артист',
             'сосед', 'фраза', 'фигура', 'субъект', 'реакция', 'список', 'фотография', 'журналист', 'май', 'нарушение',
             'заседание', 'толпа', 'больница', 'существо', 'свойство', 'долг', 'поколение', 'животное', 'схема',
             'усилие', 'отличие', 'остров', 'противник', 'волна', 'реализация', 'страница', 'формирование', 'житель',
             'красота', 'птица', 'растение', 'тень', 'явление', 'храм', 'запах', 'водка', 'наличие', 'ужас', 'одежда',
             'кресло', 'больной', 'поезд', 'университет', 'традиция', 'адрес', 'декабрь', 'ладонь', 'сведение',
             'цветок',
             'лидер', 'октябрь', 'занятие', 'сентябрь', 'помещение', 'январь', 'зритель', 'редакция', 'стиль', 'весна',
             'фактор', 'август', 'известие', 'зависимость', 'охрана', 'оборудование', 'концерт', 'отделение', 'расход',
             'выставка', 'милиция', 'переход', 'эпоха', 'запад', 'произведение', 'родина', 'собственность', 'тайна',
             'трава', 'лагерь', 'имущество', 'кровать', 'аппарат', 'середина', 'март', 'клиент', 'дама', 'фронт',
             'отрасль', 'стул', 'беседа', 'законодательство', 'продажа', 'повышение', 'музей', 'след', 'полковник',
             'сомнение', 'понимание', 'апрель', 'князь', 'рыба', 'дума', 'кодекс', 'сутки', 'чудо', 'шея', 'судья',
             'крыша', 'настроение', 'поток', 'должность', 'преступление', 'мозг', 'честь', 'пост', 'еврей', 'июнь',
             'сотня', 'дождь', 'лестница', 'дача', 'установка', 'появление', 'получение', 'образец', 'труба', 'главное',
             'осень', 'костюм', 'баба', 'ценность', 'обязанность', 'пьеса', 'таблица', 'вино', 'воспоминание', 'лошадь',
             'коллега', 'организм', 'ученик', 'учреждение', 'открытие', 'том', 'черта', 'характеристика', 'выполнение',
             'оборона', 'выступление', 'температура', 'перспектива', 'подруга', 'приказ', 'жертва', 'ресторан',
             'километр', 'спор', 'вкус', 'признак', 'промышленность', 'американец', 'лоб', 'заключение', 'восток',
             'исключение', 'ключ', 'постановление', 'слой', 'бок', 'июль', 'перевод', 'секретарь', 'кусок', 'слух',
             'польза', 'звонок', 'обстановка', 'чиновник', 'соглашение', 'деталь', 'русский', 'тишина', 'зарплата',
             'билет', 'подарок', 'тюрьма', 'ящик', 'конкурс', 'книжка', 'изучение', 'просьба', 'царь', 'публика',
             'смех',
             'сообщение', 'угроза', 'беда', 'блок', 'достижение', 'назначение', 'реклама', 'портрет', 'масло', 'стакан',
             'урок', 'часы', 'крик', 'творчество', 'телевизор', 'инструмент', 'концепция', 'лейтенант', 'экран', 'дно',
             'реальность', 'канал', 'мясо', 'знакомый', 'щека', 'конфликт', 'переговоры', 'запись', 'вагон', 'площадка',
             'последствие', 'сотрудничество', 'зеркало', 'тон', 'академия', 'палата', 'потребность', 'ноябрь',
             'увеличение', 'дурак', 'поездка', 'обед', 'потеря', 'февраль', 'мероприятие', 'парк', 'принятие',
             'устройство', 'вещество', 'категория', 'сезон', 'гостиница', 'издание', 'объединение', 'темнота',
             'человечество', 'колесо', 'опасность', 'разрешение', 'воздействие', 'коллектив', 'камера', 'запас',
             'следствие', 'длина', 'крыло', 'округ', 'фон', 'кандидат', 'родственник', 'давление', 'присутствие',
             'взаимодействие', 'доска', 'партнер', 'двигатель', 'шум', 'достоинство', 'грех', 'нож', 'полет', 'страсть',
             'испытание', 'истина', 'оплата', 'разница', 'водитель', 'пакет', 'снижение', 'формула', 'живот', 'капитал',
             'мост', 'новость', 'эффект', 'вход', 'губернатор', 'доклад', 'смена', 'убийство', 'эксперт', 'автобус',
             'платье', 'кадр', 'тетя', 'общение', 'психология', 'лев', 'порог', 'проверка', 'процедура', 'рабочий',
             'ремонт', 'обращение', 'обучение', 'ожидание', 'памятник', 'корень', 'наблюдение', 'буква',
             'доказательство', 'признание', 'постель', 'штаб', 'владелец', 'компьютер', 'инженер', 'старуха', 'лодка',
             'ракета', 'серия', 'шутка', 'вершина', 'выпуск', 'кулак', 'лед', 'торговля', 'нефть', 'молодежь', 'цифра',
             'корпус', 'недостаток', 'сапог', 'сущность', 'талант', 'эффективность', 'кофе', 'полоса', 'основное',
             'рассмотрение', 'сбор', 'штат', 'следователь', 'жилье', 'мешок', 'описание', 'куст', 'отказ', 'замок',
             'редактор', 'дворец', 'забота', 'пиво', 'диван', 'столик', 'эксперимент', 'печать', 'кольцо', 'пистолет',
             'воспитание', 'начальство', 'профессия', 'ворота', 'добро', 'дружба', 'покой', 'риск', 'окончание', 'дым',
             'брак', 'величина', 'записка', 'инициатива', 'совесть', 'активность', 'кость', 'спорт', 'кредит',
             'господь',
             'майор', 'конференция', 'потолок', 'библиотека', 'помощник', 'конструкция', 'отдых', 'ручка', 'металл',
             'молоко', 'прокурор', 'транспорт', 'поэзия', 'соединение', 'краска', 'расстояние', 'мечта', 'село', 'еда',
             'зло', 'подразделение', 'сюжет', 'рубеж', 'сигнал', 'атмосфера', 'крест', 'вес', 'взрыв', 'контакт',
             'сигарета', 'восторг', 'золото', 'почва', 'премия', 'король', 'подъезд', 'шанс', 'автомат', 'заказ',
             'мальчишка', 'очки', 'миг', 'штука', 'чтение', 'поселок', 'свидетель', 'ставка', 'сумка', 'удивление',
             'хвост', 'песок', 'поворот', 'возвращение', 'мгновение', 'статус', 'озеро', 'строй', 'параметр', 'сказка',
             'тенденция', 'вина', 'дыхание', 'версия', 'масштаб', 'монастырь', 'хозяйка', 'дочка', 'танец',
             'эксплуатация', 'коммунист', 'пенсия', 'приятель', 'объяснение', 'набор', 'производитель', 'пыль',
             'философия', 'мощность', 'обязательство', 'уход', 'горло', 'кризис', 'указание', 'плата', 'яблоко',
             'препарат', 'действительность', 'москвич', 'остаток', 'изображение', 'сделка', 'сочинение',
             'покупатель', 'танк', 'затрата', 'строка', 'единица']

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
    bot.send_message(uiper.chat.id, 'Хотя не важно, играем в угадайку слов!')

    word_completion = '-' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    bot.send_message(uiper.chat.id,display_hangman(tries))
    bot.send_message(uiper.chat.id,f"{word_completion} {len(word)} букв")
    bot.send_message(uiper.chat.id,f"У вас осталось {tries} попыток чтоб угадать слово, иначе вас повесят")
    bot.send_message(uiper.chat.id, "Введите букву, несколько букв или слово целиком: ")
    print(word)
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
                bot.send_message(message.chat.id,f"У вас осталось {tries} попыток чтоб угадать слово, иначе вас повесят")
                bot.send_message(message.chat.id, display_hangman(tries))
            if tries < 1:
                bot.send_message(message.chat.id,f"К сожалению или счастью вас повесили, но знайте что слово было {word}")
                print(f"К сожалению или счастью вас повесили, но знайте что слово было {word}")
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('Да')
                item2 = types.KeyboardButton('Нет')
                item3 = types.KeyboardButton('Не знаю')

                markup.add(item1, item2, item3)

                bot.send_message(message.chat.id, 'Хочешь сыграть еще?', reply_markup=markup)
                bot.register_next_step_handler(message, check_da)
            else:
                for i in range(len(word)):
                    if word[i] in guessed_letters:
                        W += word[i]
                    else:
                        W += "-"
                bot.send_message(message.chat.id, W)
    if W == word:
        bot.send_message(message.chat.id, "Вы угадали, вас, возможно, не повесят")
        print(f"Вы угадали, вас, возможно, не повесят{tries}")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Да')
        item2 = types.KeyboardButton('Нет')
        item3 = types.KeyboardButton('Не знаю')

        markup.add(item1, item2, item3)

        bot.send_message(message.chat.id, 'Хочешь сыграть еще?', reply_markup=markup)
        bot.register_next_step_handler(message, check_da)

    else:
        if tries>0:
            bot.register_next_step_handler(message, check_word, tries, guessed_letters,word)



def check_da(message):
    if message.text == "Да" or message.text == "Не знаю":
        bot.send_message(message.chat.id, "Опять будем вешать! Справишься?")
        bot.register_next_step_handler(message, send_echo)
    elif message.text == "Нет":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Игры 🎮')
        item2 = types.KeyboardButton('Погода')
        item3 = types.KeyboardButton('Стикеры 😛')

        markup.add(item1, item3)

        bot.send_message(message.chat.id, "Нет", reply_markup=markup)
        bot.register_next_step_handler(message, bot_mesasge)

#шар

answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

def tell_prediction(message):
    print(message.text)
    choi=choice(answers)
    bot.send_message(message.chat.id, choi)
    print(choi)


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Да')
    item2 = types.KeyboardButton('Нет')
    item3 = types.KeyboardButton('Не знаю')

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, 'Хочешь еще один вопрос?', reply_markup=markup)
    bot.register_next_step_handler(message, check_dashar)
def check_dashar(message):
    if message.text == "Да" or message.text == "Не знаю":

        bot.send_message(message.chat.id, "Еще раз натужся и сформулируй вопрос:")
        bot.register_next_step_handler(message, tell_prediction)
    if message.text == "Нет":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Игры 🎮')
        item2 = types.KeyboardButton('Погода')
        item3 = types.KeyboardButton('Стикеры 😛')

        markup.add(item1, item3)

        bot.send_message(message.chat.id, "Возвращайся если возникнут вопросы!", reply_markup=markup)
        bot.register_next_step_handler(message, bot_mesasge)

#Погода

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
        else: answer += "а это страшная жара, срочно снимай одежду и окунайся куда-то, или ищи кондиционер"
        bot.send_message(message.chat.id,
                         "Я и так знаю что ты в Познани, если нет то напиши другой город. " + answer)
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
        else: answer += "а это страшная жара, срочно снимай одежду и окунайся куда-то, или ищи кондиционер"
        bot.send_message(message.chat.id,
                         "Я и так знаю что ты в Гиресуне, если нет то напиши другой город. " + answer)
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
        else: answer += "а это страшная жара, срочно снимай одежду и окунайся куда-то, или ищи кондиционер"
        bot.send_message(message.chat.id,
                         "Я и так знаю что ты в Гиресуне, если нет то напиши другой город. " + answer)
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
            answer += "а это страшная жара, срочно снимай одежду и окунайся куда-то, или ищи кондиционер"
        bot.send_message(message.chat.id,
                         "Я и так знаю что ты в Калининграде, если нет то напиши другой город. " + answer)
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
        else: answer += "а это страшная жара, срочно снимай одежду и окунайся куда-то, или ищи кондиционер"
        bot.send_message(message.chat.id,
                         "Я и так знаю что ты в Гиресуне, если нет то напиши другой город. " + answer)
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
            answer += "а это страшная жара, срочно снимай одежду и окунайся куда-то, или ищи кондиционер"
        bot.send_message(message.chat.id,
                         "Я и так знаю что ты в Калининграде, если нет то напиши другой город. " + answer)
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
        else: answer += "а это страшная жара, срочно снимай одежду и окунайся куда-то, или ищи кондиционер"
        bot.send_message(message.chat.id,
                         "Я и так знаю что ты в Гиресуне, если нет то напиши другой город. " + answer)

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
                answer += "а это страшная жара, срочно снимай одежду и окунайся куда-то, или ищи кондиционер"
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
                        answer += "а это страшная жара, срочно снимай одежду и окунайся куда-то, или ищи кондиционер"
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
                        answer += "а это страшная жара, срочно снимай одежду и окунайся куда-то, или ищи кондиционер"
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
                                     "Я и так знаю что ты в Гиресуне, если нет то напиши другой город. " + answer)
                else:
                    bot.send_message(message.chat.id, "Привет, " + message.text + ".")
                    bot.send_message(message.chat.id, "Напиши город в котором находишься")




bot.polling( none_stop=True )

















