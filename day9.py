# numbers = [10,20,30,40,5,6,7,8,9,1,0,2]
# for number in numbers:
#     if number % 2 == 0:
#         print(number)

# try:
#     print('1'+ 1)
# except TypeError:
#     print('except')
# finally:
#     print('finally')


# names = ['vladimir', 'aliya', 'begimai', 'erbol', 'cholpon', 'jamilya', 'bakyt']
# salaries = [0, 10000,20000, None,30000, None,None]
#
# print(names.index('erbol'))
# i = 0
# while i < len(salaries):
#     try:
#         salaries[i] *= 2
#     except TypeError:
#         salaries[i] = 0
#
#     i += 1
# print(salaries)

i = 0
names = ['vladimir', 'aliya', 'begimai', 'erbol', 'cholpon', 'jamilya', 'bakyt']
salaries = [0, 10000,20000,30000]

while i < len(names):
    try:
        salaries[i] *= 2
    except IndexError:
        salaries.append(0)
    i += 1
print(salaries)