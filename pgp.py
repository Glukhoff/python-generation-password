import random
import pyperclip
import os

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '@', '#', '$',
            '%', '&', '*', '(', ')', '/', '|', '>', '<', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


author = 'Пароль сгенерирован с помошью ~ Python Generator Password ~'
yes = ['Y', 'y', 'Д', 'д']
no = ['N', 'n', 'Н', 'н']

print('''
--------------------------------------
Python Generator Password - for Mac OS
Version: 0.3 | 2020 
--------------------------------------
''')

print(os.uname())

while True:
    try:
        number_of_characters = int(input('Количество символов: '))
        break
    except:
        print('На ввод принимаются только целые числа, попробуйте еще раз.')
        continue

result = ''
for _ in range(number_of_characters):
    result += alphabet[random.randint(0, 74)]
try:
    pyperclip.copy(result)
except:
    print('Ошибка при копировании в буфер обмена')

print('\n' + 'Пароль: ' + result + '\n' + 'Пароль успешно скопирован в буфер обмена')

while True:
    try:
        save = str(input('Сохранить его в файл? [y/N]: '))
        if save in yes:
            input_name_file = input('Имя файла: ')
            login = input('Логин: ')
            f = open('/Users/' + os.getlogin() + '/Desktop/' + input_name_file + '.txt', 'w')
            f.write(author + '\n\n' + 'Логин: ' + login + '\n' + 'Пароль: ' + result)
            f.close()
            print("Пароль сохранен.")
            break
        elif save in no:
            print('Пароль не был сохранён, но мы не рекомендуем так делать!')
            break
        else:
            print('\n' + 'Введено не верное значение' + '\n')
    except:
        print('На ввод принимаются только целые числа, попробуйте еще раз.')
        continue



