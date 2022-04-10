import exc as exc
import pyowm
from pyowm.utils.config import get_default_config
try:
    owm = pyowm.OWM('1f0e262e15c5790f98efecb2573b959c')

    namer=input("Напиши свое имя: ")

    print(namer)

    if namer=="Алекс":
        place="Полтава"
        print("И спрашивать не буду, знаю что ты в Полтаве")

    else:
        place=input(namer + ",в каком ты городе?: ")

    config_dict = get_default_config()
    config_dict['language'] = 'ru'\

    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather



    temp=(w.temperature('celsius')["temp"])
    print("Сейчас за окном " + w.detailed_status + ", температура около " + str(temp))

except:
    pass
if temp<10:
    print("а это ужасная дюдя, одевайся как капуста, ато простудишься!")
elif temp<12:
    print("а это прохладно, одень куртку и свитерок!")
else:
    print("а это комфортная температура, одевайся как хочешь")






