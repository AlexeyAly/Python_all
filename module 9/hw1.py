dayweek = input('Введите день недели: ')
s = 1
d='понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье'
for day in d:
    if day == dayweek:
        print('Номер дня недели:', s)
        break
    s += 1