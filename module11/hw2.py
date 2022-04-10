import math

amount = int(input('Введите кол-во чисел: '))
for num in range(amount):
  number = float(input('Введите число: '))
  if number > 0:
    number = math.ceil(number)
    print('x =', number, 'log(x) =', end = '')
    number = math.log(number)
    print(number)
  else:
    number = math.floor(number)
    print('x =', number, 'exp(x) =', end = '')
    number = math.exp(number)
    print(number)