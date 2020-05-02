import random
import pyperclip
import os, string

author = 'Пароль сгенерирован с помошью ~ Python Generator Password ~'
yes = ['Y', 'y', 'Д', 'д']

print('''
--------------------------------------
Python Generator Password - for Mac OS
Version: 1.2 | 2020 
--------------------------------------
''')


def format_password(password):
    return "-" * 30 + "\nПароль: {}\n".format(password) + "-" * 30


def num_char():
    while True:
        try:
            number_of_characters = int(input('Для генерации пароля укажите необходимое\nколичество символов: '))
            break
        except:
            print('На ввод принимаются только целые числа, попробуйте еще раз.')
            continue
    return number_of_characters


def copy_clip(copy_object):
    pyperclip.copy(copy_object)
    print('Пароль скопирован в буфер обмена')


def _random_pass():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    result = ''
    for _ in range(num_char()):
        result += random.choice(alphabet)
    print(format_password(password=result))
    copy_clip(result)
    return result


def _save_password(name_file: str, login: str, password: str):
    """
    :param login: Логин, которому принадлежит сгенерированый пароль [по умолчанию значение None]
    :param password: Сгенерированый пароль [по умолчанию значение None]
    :param name_file: Имя файла в котором будет сохранен сгенерированый пароль [имя файла по умолчанию key.txt]
    :return:
    """
    with open("{}/Desktop/{}.txt".format(os.getenv('HOME'), name_file), "a") as f:
        f.write("Логин: {}\nПароль: {}".format(login, password))
        f.close()


def run():
    password = _random_pass()
    save = str(input("Сохранить его в файл? [y/N]: "))
    if save in yes:
        name_file = input("Имя файла: ")
        login = input("Укажите логин, которому принадлежит этот пароль: ")
        if name_file and login != '':
            _save_password(name_file, login, password)
        else:
            _save_password(name_file='key', login='None', password=password)
    else:
        print("Пароль не был сохранён, но мы не рекомендуем так делать!")


if __name__ == '__main__':
    run()
