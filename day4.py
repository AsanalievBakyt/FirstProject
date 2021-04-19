# print(isinstance(5, int))

# price = '500'
# if isinstance(price, int):
#     print(price, 'ok')
# else:
#     price = int(price)
#     print(price, 'not ok')

# import random
#
# secret_number = random.sample([1,10,15,4564],3)
# print(secret_number)

# print(round(5.445654212,1))

# money = float(input('сколько денег хотите положить: '))
# percentage = 10
# year = int(input('на сколько лет хотите положить: '))
#
# result = money + (money * percentage // 100)
# som = int(result)
# cent = (result - som) * 100
# cent1 = int(cent)
# print(som, 'сом', cent1, 'тыйын')


price = float(input('введите цену: '))
quantity = int(input('введите кол-во: '))

total_price = price * quantity
print(total_price)
som = int(total_price)
cent = (round(total_price - som, 2)) * 100
cent1 = int(cent)
print(som, 'сом', cent1, 'тыйын')
