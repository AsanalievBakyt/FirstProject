import random

user_info = [[], []]


username = input('enter your name: ')
password = input('enter your password: ')
check_password = input('enter your password again: ')
if len(username) >= 8 and len(password) >= 6:

    if password == check_password:
        secret_num = random.randint(1000, 9999)
        print('please enter', secret_num, 'to finish registration')
        number = int(input('enter the numbers: '))
        if number == secret_num:
            user_info[0].append(username)
            user_info[1].append(password)
        else:
            print('secret number is not ok')
    else:
        print('password is not ok')
    print(user_info)


tries = 0
stop = None

while tries < 3:
    count = 0
    username = input('enter username: ')
    password = input('enter your password: ')
    while count < len(user_info[0]):

        if username == user_info[0][count] and password == user_info[1][count]:
            print('successful')
            stop = 'stop'
            break
        else:
            print('username or password is incorrect')
        count += 1
    if stop == 'stop':
        break
    tries += 1
