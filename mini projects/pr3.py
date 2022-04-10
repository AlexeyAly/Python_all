from random import *

digits='0123456789'
lowercase_letters='abcdefghijklmnopqrstuvwxyz'
uppercase_letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation='!#$%&*+-=?@^_.'
minus="il1Lo0O?"

chars = ''

q=int(input("количество паролей: "))
l=int(input("длинна паролей: "))
ch1=int(input("Включать ли цифры 0123456789? "))
ch2=int(input("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?"))
ch3=int(input("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? "))
ch4=int(input("Включать ли символы !#$%&*+-=?@^_?"))
ch5=int(input("Исключать ли неоднозначные символы il1Lo0O?"))

if ch1 == 1:
    chars+=digits
if ch2 == 1:
    chars += lowercase_letters
if ch3 == 1:
    chars += uppercase_letters
if ch4 == 1:
    chars += punctuation
if ch5 ==1:
    chars=set(chars)-set(minus)
    chars=list(chars)



for i in range(q):
    for j in range(l):
        print(choice(chars), end="")
    print()

