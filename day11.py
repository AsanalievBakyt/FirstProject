# dict1 = {'name':'Honda'}
# print(dict1['name'])
# dict1['model'] = 'fit'
# print(dict1)

# string1 = 'arrticle dfbjkdb  j djs njads jjajcc KJHKJHJKNJNJN jnjn'
# string1 = string1.capitalize()
# print(string1)
# string2 = string1.split()
# print(string2)









data = [
    {'dress':[
                {'name':'louis vuitton',
                'popularity':500,
                 'price':1000
                },
                {'name':'versace',
                'popularity':21,
                 'price':888
                },
                {'name':'supreme',
                'popularity':57,
                 'price':765
                },
    ]
    },
    {'jeans':[
                {'name':'adidas',
                'popularity':42,
                 'price':2300
                },
                {'name':'armani',
                'popularity':678,
                 'price':110
                },
                {'name':'casio',
                'popularity':230,
                 'price':3000
                },
    ]
    },
    {'t-shirt':[
                {'name':'tom ford',
                'popularity':999,
                 'price':5000
                },
                {'name':'lacoste',
                'popularity':777,
                 'price':230
                },
                {'name':'luxury',
                'popularity':876,
                 'price':2300
                },
    ]
    }
]


list1 = ['dress', 'jeans', 't-shirt']

i = 0

category_price = {}

for category in data:
    category_sum = 0
    key = list1[i]
    category_value = category[key]
    for product in category_value:
        category_sum += product['price']
    category_price[key] = category_sum
    i += 1

print(max(category_price.values()), category_price)

category_popular = {}
i = 0
for category in data:
    key1 = list1[i]
    category_pop = 0
    category_value = category[key1]
    for product in category_value:
        category_pop += product['popularity']
    category_popular[key1] = category_pop
    i += 1

print(max(category_popular.values()), category_popular)

i = 0
price_list = []

for category in data:
    # print(category)
    key = list1[i]
    value = category[key]
    # print(value)
    for product in value:
        print(product['price'])
        price_list.append(product['price'])
    i += 1

print(max(price_list), min(price_list))

file1 = open('test.txt', 'w')
file1.write(str(max(price_list)))
