import pyperclip
import random
import string


def _random_pass():
    alphabet = string.ascii_letters + string.digits + "!@#$%&*()+<>"
    result = ""

    for _ in range(20):
        result += random.choice(alphabet)

    pyperclip.copy(result)
    return result


if __name__ == '__main__':
    password = _random_pass()
    password_length = len(password) - 3
    secret_password = password.replace(password[3:password_length], "*" * password_length)
    print("-" * 31 + "\nПароль: %s - скопирован в буфер обмена\n" % secret_password + "-" * 31)
