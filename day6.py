my_list = ['honda','honda', 'bmw', 'mercedes', 'bugatti']
# print(my_list.index('honda'))
# print(my_list.count('honda'))
my_list.sort()
print(my_list)
# my_list.pop() удаляет последний элемент в списке или можно ввести индекс элемента и удалить
copy_my_list = my_list.copy()
print(copy_my_list)
my_list.append('volkswagen')
print(my_list)
my_list.insert(1, 'ford')
print(my_list)
# my_list.clear()
print(my_list)
# my_list.extend() добавляет содержимое одного списка в другой
my_list.extend('hello')
print(my_list)
my_list.remove('honda')
print(my_list)
print(my_list[1:3])
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[::-1])