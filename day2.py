# # x = int(input())
# # y = int(input())
# # if x > y:
# #     print(x)
# # else:
# #     print(y)
#
# # x = int(input())
# # if x % 2 == 0:
# #     print('even')
# # else:
# #     print('not even')
#
# # a = int(input())
# # b = int(input())
# # if a < b:
# #     print(a)
# # else:
# #     print(b)
#
# print(len('привет'))

# password = input('введите пароль: ')
# check_password = input('confirm password: ')
# if password == check_password:
#     print('successful')
# if len(password) >= 8:
#     print('successful')
# else:
#     print('password too short')

# x = int(input())
# y = int(input())

# if x > 0:
#     if y >0:
#         print(1)
#     else:
#         print(4)
# else:
#     if y > 0:
#         print(2)
#     else:
#         print(3)

# number1 = int(input())
# if number1 > 0:
#     print(1)
# elif number1 == 0:
#     print(0)
# else:
#     print(-1)

# a = int(input())
# b = int(input())
# c = int(input())

# if a >= b and a >= c:
#     print(a)
# elif b >= a and b >= c:
#     print(b)
# else:
#     print(c)


# step = int(input('введите число ходов: '))
# result = step % 6
# print(result)
#
# number = float(input())
# print(number - int(number))

string1 = 'fdjnvfdnfjn fjknsfdj navalnyi dvbdjsvjdv'
ban_word = 'navalnyi'

# if ban_word in string1:
#     del string1
# else:
#     print('ok')


distance = int(input('введите расстояние которое хотите пройти: '))
v_engine = 20
v_fuel = 100
result = v_fuel // v_engine * 100

if result >= distance:
    print('ok')
else:
    distance1 = distance - result
    fuel = v_engine * distance1 // 100
    print('необходимо еще: ', fuel, 'литров')

