from random import randint as r
from os import system as s

chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!0123456789"#$%&()*+,-./:;<=>?@[\\]^_{|}~'


def create():
    n = int(input('Введите количество символов пароля: \n'))
    password = ''
    for i in range(n):
        password = f'{password}{chars[r(0, len(chars) - 1)]}'
    print('Ваш пароль: {0}'.format(password))


prog = True
while prog:
    create()
    k = int(input('Если хотите продолжить, введите команду: (1 или 0),\n'
                  '1 - продолжить! \n'
                  '0 - не продолжать, выйти из программы! \n'))
    if k == 1:
        prog = True
    elif k == 0:
        prog = False
    s('cls')
print("До встречи ❤")
