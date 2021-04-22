# list1 = [1,2,3,4,5,6,4,6,6,7,8,12]
# # print(max(list1))
#
# def maximum_of_list(numbers):
#     return max(numbers)
#
#
# print(maximum_of_list([1,2,3,4,5]))
# print(maximum_of_list([10,20,30]))

def maximum_of_2():
    num1 = int(input())
    num2 = int(input())
    if num1 > num2:
        print(num1)
    else:
        print(num2)

# maximum_of_2()
#
# maximum_of_2()


def register(username, password, confirm_password):
    if password == confirm_password:
        return username, password
    else:
        print('Пароли не совпадают!')
username,password = register('harry', '123456', '123456')
# print(username,password)

def login(enter_username, enter_password):
    if enter_username == username and enter_password == password:
        print('successful')
    else:
        print('not ok')

login('harry', '1234567')

