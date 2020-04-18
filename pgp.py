import random
import pyperclip
import os, string


author = 'Пароль сгенерирован с помошью ~ Python Generator Password ~'
yes = ['Y', 'y', 'Д', 'д']
no = ['N', 'n', 'Н', 'н']

print('''
--------------------------------------
Python Generator Password - for Mac OS
Version: 0.4 | 2020 
--------------------------------------
''')


def num_char():
    while True:
        try:
            number_of_characters = int(input('Для генерации пароля укажите необходимое' + '\n' + 'количество символов: '))
            break
        except:
            print('На ввод принимаются только целые числа, попробуйте еще раз.')
            continue
    return number_of_characters


def copy_clip(copy_object):
    try:
        pyperclip.copy(copy_object)
        print('Пароль скопирован в буфер обмена')
    except:
        print('Ошибка при копировании пароля в буфер обмена')


def randpass():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    result = ''
    for _ in range(num_char()):
        result += random.choice(alphabet)
    print('''
--------------------------------------
Пароль: ''' + result + '''
--------------------------------------''')
    copy_clip(result)
    return result


def save_pass(randpass=randpass()):
    while True:
        save = str(input('Сохранить его в файл? [y/N]: '))
        if save in yes:
            input_name_file = input('Имя файла: ')
            login = input('Укажите логин которому принадлежит этот пароль: ')
            f = open(os.getenv('HOME') + '/Desktop/' + input_name_file + '.txt', 'w')
            f.write(author + '\n\n' + 'Логин: ' + login + '\n' + 'Пароль: ' + randpass)
            f.close()
            print('Готово')
            break
        elif save in no:
            print('Пароль не был сохранён, но мы не рекомендуем так делать!')
            break
        else:
            print('\n' + 'Введено не верное значение' + '\n')
            continue

save_pass()
