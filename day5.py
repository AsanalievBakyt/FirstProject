# count = 0
# summ = 0
# while count < 100:
#     count += 1
#     print(count)
#     summ += count
#     print(summ)

# str1 = 'milk'
# i = 0
# while i < len(str1):
#     print(str1[i:])
#     i += 1

# i = 0
# summ = 0
# while i < 10:
#     print(i)
#     i += 1
#     summ += i
# print(summ)

# import random
#
# i = 0
# secret = 0
# j = 0
# while i < 10:
#     secret = random.randint(1,1000)
#     print(secret)
#     if secret > j:
#         j = secret
#     i += 1
# print(j)

# money = int(input('сколько денег хотите положить: '))
# year = int(input('на какой срок хотите положить: '))
# percentage = 10
# i = 0
# if money > 0:
#     while i < year:
#         money = money + (money * percentage / 100)
#         i += 1
# print(round(money, 2))

# i = 0
# while i < 1000000:
#     i += 1
#     print(i)


# list1 = ['Vova', 2004, 'M', '18']
#
# i = 0
# while i < len(list1):
#     print(list1[i])
#     i += 1

list1 = ['Begimai', 'Johny', 'Frank', 'Obama', 'Trump', 'Boris', 'Steven', 'Cat']
criminal = input("Enter criminal's name: ")
i = 0



while i < len(list1):

    if criminal in list1:
        if criminal == list1[i]:
            print('Адрес преступника', i)

    else:
        print('Преступник не найден')
        break
        i += 1