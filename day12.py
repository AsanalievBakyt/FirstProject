# list1 = [1,2,3,4,5,6,4,6,6,7,8,12]
# # print(max(list1))
#
# def maximum_of_list(numbers):
#     return max(numbers)
#
#
# print(maximum_of_list([1,2,3,4,5]))
# print(maximum_of_list([10,20,30]))

# def maximum_of_2():
#     num1 = int(input())
#     num2 = int(input())
#     if num1 > num2:
#         print(num1)
#     else:
#         print(num2)

# maximum_of_2()
#
# maximum_of_2()


def register(username, password, confirm_password):
    if password == confirm_password and len(username) > 8 and not password.isalpha():
        return username, password

try:
    username,password = register('HarryPotter', '123456', '123456')
except TypeError:
    print('введите правильные данные!')


def login():
    for i in range(3):
        username1 = input()
        password1 = input()
        if username1 == username and password1 == password:
            print('successful')
            break
        else:
            print('not ok')

login()

