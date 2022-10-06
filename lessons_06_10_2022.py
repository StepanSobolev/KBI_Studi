import string

def enter_email():
    while True:
        login = input('Please enter you email: ')
        if '@' and '.' not in login:
            print('In the login must be a symbol @ and \'.\'')
            continue
        with open('file_login.txt', 'r', encoding='utf-8') as file:
            file_login = file.read().split()
        if login in file_login:
            print('This login already exists. Come up with another.')
            continue
        else:
            with open('file_login.txt', 'a', encoding='utf-8') as file:
                file.write(login + '\n')
                print('Success')
                break
    return login


def enter_password():
    while True:
        password = input('Please enter you password: ')
        # big_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
        #                    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        big_letters = string.ascii_uppercase
        # small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
        #                      's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        small_letters = string.ascii_lowercase
        # nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        nums = string.digits
        # symbol = ['@', '!', '?', '_', '$', '%', '*', '#']
        symbol = string.punctuation

        counter_upper = 0
        counter_lower = 0
        counter_nums = 0
        counter_symbol = 0

        if len(password) >= 8:
            for i in password:
                if i in big_letters:
                    counter_upper += 1
                elif i in small_letters:
                    counter_lower += 1
                elif i in nums:
                    counter_nums += 1
                elif i in symbol:
                    counter_symbol += 1

        if  counter_upper > 0 and counter_lower > 0 and counter_nums > 0 and counter_symbol > 0:
            print('Success')
            with open('file_password.txt', 'a', encoding='utf-8') as file:
                file.write(password + '\n')
                break
        else:
            print('Incorect password')
    return password


def write_user(login, password):
    wook = {}
    wook[login] = password
    with open('file_users.txt', 'a', encoding='utf-8') as file:
        file.write(str(wook) + '\n')

write_user(enter_email(), enter_password())