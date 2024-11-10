import random
import string
import time

length = int(input('Сколько символов должно быть в пароле?'))

password = ''

all_c = string.ascii_letters + string.digits

for i in range(length):
    password += random.choice(all_c)

time.sleep(1)
print('Генерация пароля... Пожалуйста подождите')
time.sleep(3)
print(f'Готово! Ваш пароль: {password}')

while True:
    mark = input('Вам нравится этот пароль?(Да или Нет)')

    if mark == 'Да' or mark == 'да':
        print('Удачного использования пароля!')
        time.sleep(1)
        print('Программа закроется через 20 секунд')
        time.sleep(1)
        print('19')
        time.sleep(1)
        print('18')
        time.sleep(1)
        print('17')
        time.sleep(1)
        print('16')
        time.sleep(1)
        print('15')
        time.sleep(1)
        print('14')
        time.sleep(1)
        print('13')
        time.sleep(1)
        print('12')
        time.sleep(1)
        print('11')
        time.sleep(1)
        print('10')
        time.sleep(1)
        print('9')
        time.sleep(1)
        print('8')
        time.sleep(1)
        print('7')
        time.sleep(1)
        print('6')
        time.sleep(1)
        print('5')
        time.sleep(1)
        print('4')
        time.sleep(1)
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(2)
        break
    if mark == 'Нет' or mark == 'нет':
        length = int(input('Сколько символов должно быть в пароле?'))
        password = ''

        for i in range(length):
            password += random.choice(all_c)

        time.sleep(1)
        print('Генерация пароля... Пожалуйста подождите')
        time.sleep(3)
        print(f'Новый пароль: {password}')            
    else:
        print('Введите Да или Нет')