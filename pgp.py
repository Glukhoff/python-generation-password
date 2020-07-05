import pyperclip
import random
import string
import os

author = 'Пароль сгенерирован с помошью ~ Python Generator Password ~'
yes = ['Y', 'y', 'Д', 'д']

print('''
--------------------------------------
Python Generator Password - for Mac OS
Version: 1.3 | 2020 
--------------------------------------
''')


def format_password(result):
    return "-" * 30 + "\nПароль: {}\n".format(result) + "-" * 30


def num_char():
    while True:
        try:
            get_number = int(input('Для генерации пароля укажите необходимое\nколичество символов: '))
            return get_number
        except TypeError:
            print('На ввод принимаются только целые числа, попробуйте еще раз.')
            continue


def copy_clip(copy_object):
    pyperclip.copy(copy_object)
    print('Пароль скопирован в буфер обмена')


def _random_pass():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    result = ''
    for _ in range(num_char()):
        result += random.choice(alphabet)
    print(format_password(result=result))
    copy_clip(result)
    return result


def _save_password(filename: str, username: str, user_password: str):
    """
    :param username: Логин, которому принадлежит сгенерированый пароль [по умолчанию значение None]
    :param user_password: Сгенерированый пароль [по умолчанию значение None]
    :param filename: Имя файла в котором будет сохранен сгенерированый пароль [имя файла по умолчанию key.txt]
    :return:
    """
    with open("{}/Desktop/{}.txt".format(os.getenv('HOME'), filename), "a") as f:
        f.write("Логин: {}\nПароль: {}".format(username, user_password))


if __name__ == '__main__':
    password = _random_pass()
    save = str(input("Сохранить его в файл? [y/N]: "))
    if save in yes:
        name_file = input("Имя файла: ")
        login = input("Укажите логин, которому принадлежит этот пароль: ")
        if name_file and login != '':
            _save_password(name_file, login, password)
        else:
            _save_password(filename='key', username='None', user_password=password)
    else:
        print("Пароль не был сохранён, но мы не рекомендуем так делать!")