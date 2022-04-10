height = int(input('Введите высоту пирамиды: '))
for row in range(1, height + 1):
  print(' ' * (height - row) + '#' * (1 + 2 * (row - 1)))